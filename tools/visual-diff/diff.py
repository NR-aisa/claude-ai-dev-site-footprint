"""Before/after screenshot diff with Pillow.
Adapted from gist 2, section 9. Requires Pillow: pip install Pillow
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "result-logger"))
from app_errors import AppError, Result  # noqa: E402
from task_logger import TaskLogger  # noqa: E402


def diff_images(before: Path, after: Path, logger: TaskLogger) -> Result[dict]:
    try:
        from PIL import Image, ImageChops
    except ImportError:
        return Result.fail(AppError("IMPORT_ERROR", "Pillow is not installed: pip install Pillow", "diff"))
    if not before.exists() or not after.exists():
        return Result.fail(AppError("NOT_FOUND_ERROR", "Before or after screenshot is missing", "diff"))
    img_a = Image.open(before).convert("RGB")
    img_b = Image.open(after).convert("RGB")
    if img_a.size != img_b.size:
        logger.warn(f"Size mismatch: before {img_a.size}, after {img_b.size} — comparing overlap only")
        width, height = min(img_a.width, img_b.width), min(img_a.height, img_b.height)
        img_a, img_b = img_a.crop((0, 0, width, height)), img_b.crop((0, 0, width, height))
    diff = ImageChops.difference(img_a, img_b)
    pixels = list(diff.getdata())
    total = len(pixels)
    changed = sum(1 for p in pixels if any(c > 10 for c in p))
    mse = sum(sum(c * c for c in p) for p in pixels) / (total * 3)
    result = {"mse": round(mse, 2), "rmse": round(math.sqrt(mse), 2),
              "changed_pct": round(100 * changed / total, 2), "size": list(img_a.size)}
    logger.info(f"MSE {result['mse']} | RMSE {result['rmse']} | changed {result['changed_pct']}%")
    return Result.ok(result)


def main() -> int:
    p = argparse.ArgumentParser(description="Screenshot before/after diff")
    p.add_argument("before")
    p.add_argument("after")
    p.add_argument("--threshold", type=float, default=5.0,
                   help="Changed-%% above this is reported as a big diff (exit 1)")
    args = p.parse_args()
    logger = TaskLogger(log_path=Path("logs/visual-diff.log"))
    result = diff_images(Path(args.before), Path(args.after), logger)
    if result.has_error:
        logger.fail(str(result.error))
        return 1
    logger.audit("visual-diff", "SUCCESS", result.value)
    return 1 if result.value["changed_pct"] > args.threshold else 0


if __name__ == "__main__":
    raise SystemExit(main())
