# visual-diff — Pillow before/after screenshot diffing

Taken from: `prompts/source/wordpress-elementor-modernization-prompt.md`,
§9 "Visual Screenshot Diffing with Pillow".

## What it is

A small script that compares a before and an after screenshot of the
same page/section and reports mean squared error (MSE) and the
percentage of pixels that differ. It makes "did this edit break
anything else on the page?" measurable instead of eyeballed.

## What was taken, what was left out

- Taken: Pillow `ImageChops.difference`, MSE + pixel-mismatch %,
  the before/after capture discipline.
- Left out: the automated-rollback-on-threshold rule (a human judges
  whether a diff is a break or an intended change — a redesign
  *should* differ by a lot); the headless-browser capture machinery
  (screenshots here come from the operator's browser / the live
  logged-out check).

## Usage

```sh
pip install Pillow
python3 diff.py before.png after.png [--threshold 5.0]
```

- Same viewport size for both shots, same scroll position.
- A high % is expected after a deliberate redesign; a high % in an
  *unchanged* section means something leaked.
- Save both screenshots in the footprint folder under
  `evidence/screenshots/` with dates in the filename.

## Files

- `diff.py` — the diff script (Result + logger pattern from
  `tools/result-logger/`).
