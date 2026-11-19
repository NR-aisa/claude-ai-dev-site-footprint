# Source prompts — reference ONLY

These two files are verbatim copies of public gists by alimtvnetwork,
saved here so the tools in `tools/` can be traced back to their source.

- `python-any-task-master-prompt.md` — "Universal Python Task Automation &
  System Execution Engine", v2.0.0.
  https://gist.github.com/alimtvnetwork/fd0953a5f2bfbbc91ae6e3666c5f7c37
- `wordpress-elementor-modernization-prompt.md` — "Universal WordPress
  Modernization & Elementor Conversion Engine", v4.0.0.
  https://gist.github.com/alimtvnetwork/11900295ef222d921bd646923fbcff3d

## NOT adopted

Neither file is adopted as a global instruction set, and neither governs
this project. In particular, do NOT follow from them:

- the 400-step self-loop budget, 3 concurrent subagents, 30-tool-call
  reporting rule;
- the "run the Python prompt first or halt" gate in the WordPress prompt;
- the "never run ad-hoc shell commands" rule;
- any credential-storage machinery (temp SQLite credential store,
  RSA-OAEP-encrypted JSON) — this project uses Secure Vault and the
  existing `gh` auth, and stores no credential anywhere;
- pushing raw `_elementor_data` JSON via the REST API as the normal edit
  method — edits here are made in Elementor's own editor and verified
  live as a logged-out visitor.

## What WAS taken from them

Only the pieces extracted into `tools/`, each with its own README stating
what was taken, what was left out, and why:

- `tools/result-logger/` — Result[T] + structured logger + `--dry-run`
  (from gist 1).
- `tools/wp-preflight-backup/` — per-page draft backup before editing
  (from gist 2, §5).
- `tools/elementor-schemas/` — Flexbox container + widget schemas,
  semantic IDs, scoped CSS (from gist 2, §6).
- `tools/visual-diff/` — Pillow before/after screenshot diffing
  (from gist 2, §9).
