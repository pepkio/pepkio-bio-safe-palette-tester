# Pepkio Bio-Safe Palette Tester

Python client for the Pepkio Bio-Safe Palette Tester API: test color palettes for colorblind accessibility (CVD simulation), grayscale print readiness, conflict detection, auto-fix suggestions, and export code snippets from Python or command line.

## Installation

```bash
pip install pepkio-bio-safe-palette-tester
```

Set an API key with `tools:run` scope before calling `run()`:

```bash
export PEPKIO_API_KEY="your-api-key"
```

## Quick Start (Python API)

```python
from pepkio_bio_safe_palette_tester import PepkioClient

with PepkioClient() as client:
    # 1. Fetch manifest and examples
    manifest = client.get_manifest()
    examples = client.list_examples()

    # 2. Analyze color palette for colorblind safety
    result = client.run({
        "action": "analyze_palette",
        "colors": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00"]
    })
    print("Status:", result.status)
    print("Simulations:", result.result.get("simulations"))
    print("Conflicts:", result.result.get("conflicts"))

    # 3. Get auto-fix suggestion for ambiguous colors
    fix_res = client.run({
        "action": "suggest_fix",
        "color_a": "#E69F00",
        "color_b": "#D55E00"
    })
    print("Auto-fix suggestion:", fix_res.result)
```

## Quick Start (CLI)

```bash
# View manifest
pepkio-bio-safe-palette-tester manifest --examples

# Run named manifest example
pepkio-bio-safe-palette-tester run --example analyze_okabe_ito

# Run with JSON input
pepkio-bio-safe-palette-tester run --input-json '{"action": "suggest_fix", "color_a": "#E69F00", "color_b": "#D55E00"}'
```
