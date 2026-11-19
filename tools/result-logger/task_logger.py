"""Dual-channel logger: ANSI badges on console, JSON audit lines to file.
Adapted from gist 1 (python-any-task-master-prompt.md, task_logger.py).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RESET = "\033[0m"
BOLD = "\033[1m"
COLORS = {"green": "\033[32m", "red": "\033[31m", "yellow": "\033[33m",
          "blue": "\033[34m", "cyan": "\033[36m"}
BADGES = {"ok": "[  OK  ]", "fail": "[ FAIL ]", "warn": "[ WARN ]",
          "info": "[ INFO ]", "skip": "[ SKIP ]"}


class TaskLogger:
    """Log to console and to a JSON-lines audit file."""

    def __init__(self, log_path: Path | str | None = None, is_verbose: bool = False) -> None:
        self.is_verbose = is_verbose
        self.enable_ansi = sys.stdout.isatty()
        self.log_path = Path(log_path) if log_path else Path("logs/task.log")
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def _strip_ansi(self, text: str) -> str:
        return re.sub(r"\033\[[0-9;]*m", "", text)

    def _write(self, line: str) -> None:
        try:
            with open(self.log_path, "a", encoding="utf-8", newline="\n") as h:
                h.write(self._strip_ansi(line) + "\n")
        except OSError:
            pass

    def log(self, level: str, message: str, details: dict[str, Any] | None = None) -> None:
        badge = BADGES[level]
        color = COLORS[{"ok": "green", "fail": "red", "warn": "yellow",
                        "info": "blue", "skip": "cyan"}[level]]
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        console = f"{color}{BOLD}{badge}{RESET} {message}" if self.enable_ansi else f"{badge} {message}"
        print(console)
        self._write(f"[{now}] {badge} {message}")
        if details and self.is_verbose:
            self._write(f"[{now}] DETAILS: {json.dumps(details, default=str)}")

    def ok(self, m: str, d: dict[str, Any] | None = None) -> None:
        self.log("ok", m, d)

    def fail(self, m: str, d: dict[str, Any] | None = None) -> None:
        self.log("fail", m, d)

    def warn(self, m: str, d: dict[str, Any] | None = None) -> None:
        self.log("warn", m, d)

    def info(self, m: str, d: dict[str, Any] | None = None) -> None:
        self.log("info", m, d)

    def skip(self, m: str, d: dict[str, Any] | None = None) -> None:
        self.log("skip", m, d)

    def audit(self, operation: str, status: str, details: dict[str, Any] | None = None) -> None:
        payload = {"timestamp": datetime.now(timezone.utc).isoformat(),
                   "operation": operation, "status": status, "details": details or {}}
        self._write(f"JSON_AUDIT: {json.dumps(payload, default=str)}")
