"""Per-page WordPress draft backup via the REST API.
Adapted from gist 2, section 5. Credentials ONLY from environment
variables at run time; nothing is stored. Supports --dry-run.
Requires: requests (pip install requests) or Python 3.11+ urllib only.
This version uses only the standard library.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "result-logger"))
from app_errors import AppError, Result  # noqa: E402
from task_logger import TaskLogger  # noqa: E402


def _auth_header(user: str, app_password: str) -> str:
    token = base64.b64encode(f"{user}:{app_password}".encode()).decode()
    return f"Basic {token}"


def _request(site: str, path: str, user: str, app_password: str,
             method: str = "GET", payload: dict | None = None) -> Result[dict]:
    url = f"{site.rstrip('/')}/wp-json/wp/v2{path}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", _auth_header(user, app_password))
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return Result.ok(json.loads(resp.read().decode()))
    except urllib.error.HTTPError as ex:
        return Result.fail(AppError("HTTP_ERROR", f"{method} {path}: HTTP {ex.code}", "rest"))
    except OSError as ex:
        return Result.fail(AppError("IO_ERROR", f"{method} {path}: {ex}", "rest"))


def backup_page(site: str, user: str, app_password: str, page_id: int,
                is_dry_run: bool, logger: TaskLogger) -> Result[dict]:
    got = _request(site, f"/pages/{page_id}?context=edit", user, app_password)
    if got.has_error:
        return Result.fail(got.error)
    page = got.value
    title = page.get("title", {}).get("rendered", f"page-{page_id}")
    logger.info(f"Source page {page_id}: {title!r} (status {page.get('status')})")
    if is_dry_run:
        logger.info("[DRY-RUN] Would create draft backup and save postmeta to backups.json")
        return Result.ok({"page_id": page_id, "title": title, "dry_run": True})
    payload = {"title": f"{title} - Backup", "status": "draft",
               "content": page.get("content", {}).get("raw", ""),
               "meta": page.get("meta", {})}
    created = _request(site, "/pages", user, app_password, method="POST", payload=payload)
    if created.has_error:
        return Result.fail(created.error)
    backup = created.value
    logger.ok(f"Draft backup created: id {backup.get('id')} — {backup.get('title', {}).get('rendered')!r}")
    return Result.ok({"page_id": page_id, "title": title,
                      "backup_id": backup.get("id"),
                      "backup_link": backup.get("link")})


def main() -> int:
    p = argparse.ArgumentParser(description="WordPress per-page draft backup (REST API)")
    p.add_argument("--page-id", type=int, required=True)
    p.add_argument("--out", default="backups.json")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    site = os.environ.get("WP_SITE_URL", "")
    user = os.environ.get("WP_USER", "")
    app_password = os.environ.get("WP_APP_PASSWORD", "")
    logger = TaskLogger(log_path=Path("logs/wp-backup.log"))
    if not site or not user or not app_password:
        logger.fail("Set WP_SITE_URL, WP_USER and WP_APP_PASSWORD in the environment first.")
        return 2
    result = backup_page(site, user, app_password, args.page_id, args.dry_run, logger)
    if result.has_error:
        logger.fail(str(result.error))
        return 1
    if not args.dry_run:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        existing = json.loads(out.read_text(encoding="utf-8")) if out.exists() else []
        existing.append(result.value)
        out.write_text(json.dumps(existing, indent=2), encoding="utf-8")
        logger.ok(f"Recorded in {out}")
    logger.audit("wp-preflight-backup", "SUCCESS", result.value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
