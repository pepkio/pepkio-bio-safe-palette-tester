# Pepkio Bio-Safe Palette Tester

Scientific color palette accessibility tester and CIEDE2000 colorblind simulator for research figures and publications.

# What It Does

The `pepkio-bio-safe-palette-tester` Python package tests categorical color palettes for color vision deficiency (CVD) accessibility and grayscale print legibility. It performs real-time protanopia, deuteranopia, and tritanopia simulations, detects perceptual contrast conflicts ($\Delta E < 10$), provides automated CIELAB hue/lightness fixes, and exports code snippets for R (`ggplot2`), Python (`matplotlib`/`seaborn`), and GraphPad Prism.

# Features

- **CVD Simulation Engine**: Models protanopia, deuteranopia, tritanopia, and grayscale monochrome conversion.
- **CIEDE2000 Metric**: Calculates exact perceptual color distance ($\Delta E_{00}$) between all color pairs.
- **Automated Palette Correction**: Auto-adjusts lightness and saturation in CIELAB space to resolve low-contrast conflicts.
- **Standard Scientific Presets**: Built-in support for Okabe-Ito, Wong, Paul Tol, and Viridis palettes.
- **Code Export**: Direct code snippet generation for ggplot2, matplotlib, seaborn, and Prism.
- **CLI & Python API**: Usable as a command-line utility or scriptable Python library.

# Installation

```bash
pip install pepkio-bio-safe-palette-tester
```

Or using `uv`:

```bash
uv add pepkio-bio-safe-palette-tester
```

# Quick Example

```python
from pepkio_bio_safe_palette_tester import PepkioClient

with PepkioClient() as client:
    analysis = client.run({
        "action": "analyze_palette",
        "colors": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00"]
    })

    print("Status:", analysis.result.get("banner"))
    print("Simulated Protanopia Colors:", analysis.result["simulations"][0]["colors"])
```

# Typical Use Cases

- **Journal Figure Preparation**: Validate that UMAP, scatter plots, and survival curves comply with journal accessibility standards.
- **Grayscale Verification**: Ensure figures remain legible when printed in black and white.
- **Theme Standardization**: Standardize colorblind-safe color palettes across research teams.

# Scientific Background

CVD simulations use psychophysically validated projection algorithms (Viénot 1999, Brettel 1997 via libDaltonLens). Color distances are evaluated using the CIE standard $\Delta E_{00}$ equation; pairs with $\Delta E_{00} < 10.0$ are flagged as perceptual hazards.

# Web Application

For interactive swatch testing and sharing, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/bio-safe-palette-tester

# Documentation and Resources

- GitHub Repository: https://github.com/pepkio/pepkio-bio-safe-palette-tester
- Web Application: https://www.pepkio.com/tools/bio-safe-palette-tester
- PyPI Package: https://pypi.org/project/pepkio-bio-safe-palette-tester/

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

# Keywords

bio-safe palette, colorblind safe, figure accessibility, CIEDE2000, protanopia, deuteranopia, tritanopia, grayscale figure, Okabe-Ito, Wong, Paul Tol, viridis, ggplot2 scale_color_manual, matplotlib colormap, seaborn accessible palette, GraphPad Prism color, scientific data visualization, UMAP colors, flow cytometry colors, heatmap accessibility, CIE LAB color difference, perceptual color contrast, laboratory figure design, manuscript figure, journal figure guidelines, open science accessibility, bioinformatic visualization tool
