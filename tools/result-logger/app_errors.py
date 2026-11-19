"""Monadic error handling: Result[T] / AppError.
Adapted from gist 1 (python-any-task-master-prompt.md, app_errors.py).
No external dependencies. Functions are kept short on purpose.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class AppError:
    """Structured error container."""

    code: str
    message: str
    operation: str = ""
    details: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        if self.operation:
            return f"[{self.code}] {self.operation}: {self.message}"
        return f"[{self.code}] {self.message}"


class Result(Generic[T]):
    """Holds either a value or an AppError, never both, never neither."""

    def __init__(self, value: T | None, error: AppError | None, is_safe: bool) -> None:
        self._value = value
        self._error = error
        self._is_safe = is_safe

    @classmethod
    def ok(cls, value: T) -> "Result[T]":
        return cls(value=value, error=None, is_safe=True)

    @classmethod
    def fail(cls, error: AppError) -> "Result[T]":
        return cls(value=None, error=error, is_safe=False)

    @property
    def is_safe(self) -> bool:
        return self._is_safe

    @property
    def has_error(self) -> bool:
        return not self._is_safe

    @property
    def value(self) -> T:
        if self.has_error:
            raise RuntimeError(f"Unwrap of failed result: {self._error}")
        return self._value  # type: ignore[return-value]

    @property
    def error(self) -> AppError:
        if self.is_safe:
            raise RuntimeError("No error on a safe result")
        return self._error  # type: ignore[return-value]
