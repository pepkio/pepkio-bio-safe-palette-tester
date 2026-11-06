# Pepkio Bio-Safe Palette Tester

Run the Pepkio bio-safe-palette-tester CLI in a container to simulate color-vision deficiency, compute CIEDE2000 color differences, and export snippet-ready palettes through the hosted API.

# What It Does

The image runs `pepkio-bio-safe-palette-tester`, a client for the Pepkio Bio-Safe Palette Tester REST API. Submit palette actions (analyze, simulate CVD, suggest fixes, export snippets) and receive structured results with conflict flags and shareable permalinks. Calculator logic runs on Pepkio servers; provide a network connection and API key for `run` commands.

# Features

- CVD simulation (protanopia, deuteranopia, tritanopia, grayscale)
- CIEDE2000 pairwise contrast checks and automatic lightness adjustments
- Presets: Okabe-Ito, Wong, Paul Tol, Viridis
- Snippet export for R (`ggplot2`), Python (`matplotlib`), GraphPad Prism
- Manifest inspection without an API key

# Quick Start

```bash
docker pull pepkio/bio-safe-palette-tester:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/bio-safe-palette-tester:0.1.0 \
  pepkio-bio-safe-palette-tester run --example <example_name>
```

Manifest only (no API key):

```bash
docker run --rm pepkio/bio-safe-palette-tester:0.1.0 \
  pepkio-bio-safe-palette-tester manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Typical Use Cases

- Verify manuscript figures for colorblind-safe palettes before journal submission
- Batch-check dynamically generated palettes in bioinformatics pipelines
- Export ggplot2 or matplotlib snippets for lab-wide figure style guides

# Web Application

Web Application: https://www.pepkio.com/tools/bio-safe-palette-tester

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-bio-safe-palette-tester

PyPI Package: https://pypi.org/project/pepkio-bio-safe-palette-tester/

Web Application: https://www.pepkio.com/tools/bio-safe-palette-tester

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).
