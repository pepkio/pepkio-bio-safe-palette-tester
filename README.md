# pepkio-bio-safe-palette-tester

Python client for Pepkio bio-safe-palette-tester tool.

## Installation

```bash
uv pip install -e .
```

## Usage

```python
from pepkio_bio_safe_palette_tester import PepkioClient

with PepkioClient() as client:
    manifest = client.get_manifest()
    result = client.run({
        "action": "analyze_palette",
        "colors": ["#E69F00", "#56B4E9", "#009E73"]
    })
    print(result.result)
```

## CLI

```bash
pepkio-bio-safe-palette-tester manifest --examples
pepkio-bio-safe-palette-tester run --example analyze_okabe_ito
```

## Testing

```bash
# Unit tests
uv run pytest tests/test_client.py -v

# Integration tests (against local & production APIs)
export LOCAL_PEPKIO_API_KEY="<local-key>"
export PEPKIO_API_KEY="<prod-key>"
uv run pytest tests/test_integration.py -v
```
