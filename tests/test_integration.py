"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_bio_safe_palette_tester.client import PepkioClient
from pepkio_bio_safe_palette_tester.config import TOOL_ID

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", os.getenv("PEPKIO_API_BASE_URL_LOCAL", "https://tools.localtest.me")),
    ("production", os.getenv("PEPKIO_API_BASE_URL_PROD", "https://tools.pepkio.com")),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY") or os.getenv("PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == TOOL_ID
    names = live_client.list_examples()
    assert "analyze_okabe_ito" in names


def test_run_analyze_okabe_ito(live_client: PepkioClient):
    inp = live_client.get_example_input("analyze_okabe_ito")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert "colors" in result.result


def test_run_suggest_fix(live_client: PepkioClient):
    inp = live_client.get_example_input("suggest_fix")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None


def test_run_build_python_snippet(live_client: PepkioClient):
    inp = live_client.get_example_input("build_python_snippet")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("format") == "python"


def test_get_run(live_client: PepkioClient):
    inp = live_client.get_example_input("analyze_okabe_ito")
    result = live_client.run(inp)
    assert result.run_id
    fetch_res = live_client.get_run(result.run_id)
    assert fetch_res.run_id == result.run_id
    assert fetch_res.status == "completed"
