"""Demo of the Result + logger + --dry-run pattern.
Usage: python3 demo.py --dry-run   (previews only, changes nothing)
       python3 demo.py             (writes demo files into a temp dir)
"""
from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from app_errors import AppError, Result
from task_logger import TaskLogger


def purge_file(path: Path, is_dry_run: bool, logger: TaskLogger) -> Result[bool]:
    if is_dry_run:
        logger.info(f"[DRY-RUN] Would remove: {path}")
        return Result.ok(True)
    try:
        path.unlink(missing_ok=True)
        logger.ok(f"Purged: {path}")
        return Result.ok(True)
    except OSError as ex:
        return Result.fail(AppError("IO_ERROR", f"Failed to delete {path}: {ex}", "purge"))


def main() -> int:
    args = argparse.ArgumentParser()
    args.add_argument("--dry-run", action="store_true")
    parsed = args.parse_args()
    logger = TaskLogger(log_path=Path(tempfile.gettempdir()) / "result-logger-demo.log")
    with tempfile.TemporaryDirectory() as tmp:
        demo = Path(tmp) / "demo.txt"
        demo.write_text("demo", encoding="utf-8")
        result = purge_file(demo, parsed.dry_run, logger)
        if result.has_error:
            logger.fail(str(result.error))
            return 1
        logger.audit("purge", "SUCCESS", {"path": str(demo), "dry_run": parsed.dry_run})
        logger.ok("Demo complete")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
