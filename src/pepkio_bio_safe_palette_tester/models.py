"""Typed API request/response models."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

from .exceptions import PepkioAPIError


class ToolInput(BaseModel):
    """Input payload for bio-safe-palette-tester tool."""

    model_config = ConfigDict(extra="allow")

    action: Literal[
        "analyze_palette",
        "suggest_fix",
        "build_snippet",
        "build_all_snippets",
        "parse_palette_url",
        "encode_palette_url",
        "validate_hex",
        "get_preset",
    ]
    colors: list[str] | None = None
    color_a: str | None = None
    color_b: str | None = None
    format: Literal["r", "python", "prism", "hex", "url"] | None = None
    colors_param: str | None = None
    preset_id: Literal["okabe-ito", "wong", "tol", "viridis"] | None = None
    origin: str | None = None
    pathname: str | None = None
    simulation_mode: Literal["swatches", "mini-plots"] | None = None
    background: Literal["light", "dark"] | None = None


class RunOptions(BaseModel):
    """Optional fields for POST .../run."""

    idempotency_key: str | None = None
    label: str | None = None


class RunResult(BaseModel):
    """Tool run response envelope."""

    model_config = ConfigDict(extra="allow")

    run_id: str
    status: str
    result: dict[str, Any] | None = None
    error: dict[str, Any] | str | None = None
    result_url: str | None = None
    permalink: str | None = None
    duration_ms: int | None = None

    def raise_for_error(self) -> None:
        """Raise PepkioAPIError if the run response includes an error field."""
        if self.error is None:
            return
        if isinstance(self.error, dict):
            message = self.error.get("message", "Tool run failed")
            code = self.error.get("code")
            raw_details = self.error.get("details")
            details = raw_details if isinstance(raw_details, dict) else {}
        else:
            message = str(self.error)
            code = None
            details = {}

        raise PepkioAPIError(
            message,
            code=code,
            details=details,
            response_body={"run_id": self.run_id, "status": self.status, "error": self.error},
        )


def parse_run_response(data: dict[str, Any]) -> RunResult:
    """Parse a run API JSON body into RunResult."""
    return RunResult.model_validate(data)
