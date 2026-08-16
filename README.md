# Pepkio Bio-Safe Palette Tester

Test, simulate, and optimize scientific color palettes for colorblind accessibility, grayscale print readiness, and CIEDE2000 perceptual contrast in Python and via web interface.

# Overview

Scientific figures in biology, bioinformatics, medicine, and chemistry rely heavily on color coding to communicate categorical variables across heatmaps, UMAP embeddings, flow cytometry gates, survival curves, and multi-channel fluorescence microscopy. However, approximately 8% of men and 0.5% of women worldwide have Color Vision Deficiency (CVD)—most commonly deuteranomaly (red-green green-weak), protanomaly (red-green red-weak), or tritanopia (blue-yellow).

When scientific figures use problematic color combinations (such as traditional red-green heatmaps or rainbow/jet colormaps), data points become indistinguishable to CVD readers and fail in black-and-white or grayscale printing. Furthermore, subtle contrast differences between adjacent swatches can lead to misinterpretation of high-stakes clinical and biological results.

The **Pepkio Bio-Safe Palette Tester** provides a complete accessibility testing and optimization toolkit for scientific color palettes. It performs real-time CVD simulations (protanopia, deuteranopia, tritanopia, and grayscale/monochrome conversion) using validated projection matrices (Viénot 1999, Brettel 1997 via libDaltonLens). It evaluates pairwise perceptual color distances using the industry-standard CIEDE2000 $\Delta E$ algorithm, flags contrast conflicts ($\Delta E < 10$), suggests automatic CIELAB lightness/hue corrections, and exports ready-to-use code snippets for R (`ggplot2`), Python (`matplotlib`/`seaborn`), and GraphPad Prism.

The interactive web tool is available at the [Pepkio Bio-Safe Palette Tester](https://www.pepkio.com/tools/bio-safe-palette-tester) web application for instant browser-based palette evaluation and sharing. A programmatic Python client and CLI are maintained in this repository for automated visualization pipelines.

Common search terms and alternative names for this tool include bio-safe palette tester, colorblind safe palette checker, scientific figure accessibility tool, CIEDE2000 color difference calculator, protanopia deuteranopia simulator, Okabe-Ito palette exporter, ggplot2 colorblind palette generator, matplotlib accessible colormap, and grayscale figure readiness tester.

# Features

- **Multi-Type Color Vision Deficiency (CVD) Simulation**:
  - *Protanopia* (red-blind) and *Protanomaly* (red-weak)
  - *Deuteranopia* (green-blind) and *Deuteranomaly* (green-weak)
  - *Tritanopia* (blue-blind) and *Tritanomaly* (blue-weak)
  - *Achromatopsia / Grayscale* (monochrome luminance simulation for journal print readiness).
- **Rigorous CIEDE2000 $\Delta E$ Conflict Detection**:
  - Calculates perceptual distance between all color pairs in normal vision and simulated CVD conditions.
  - Automatically flags severe indistinguishability ($\Delta E < 5.0$, Error) and low contrast ($\Delta E < 10.0$, Warning).
- **Intelligent Auto-Fix Engine**: Automatically resolves low-contrast pairs by adjusting lightness ($L^*$) and chroma ($C^*$) in CIELAB color space while preserving the hue identity of the palette.
- **Curated Standard Scientific Presets**:
  - *Okabe-Ito* (standard 8-color universal palette)
  - *Wong* (Nature Methods colorblind-safe palette)
  - *Paul Tol* (high-contrast categorical palettes)
  - *Viridis* (perceptually uniform sequential colormap).
- **Multi-Language Code Snippet Generation**: Direct export to R (`scale_color_manual(values = ...)`), Python (`ListedColormap`, `matplotlib`, `seaborn`), GraphPad Prism XML/text, and raw HEX lists.
- **Shareable URL Encoding**: Encodes custom palettes into URL query parameters (`?colors=E69F00,56B4E9,...`) for effortless collaboration across research labs.
- **Python Library & CLI**: Integrate palette accessibility verification into automated script pipelines, Jupyter notebooks, or continuous integration (CI) figure generation.

# Common Use Cases

- **Scientific Manuscript Figure Preparation**: Verify that multi-panel scatter plots, boxplots, UMAP/t-SNE single-cell clusters, and bar charts comply with journal accessibility guidelines (e.g., Nature, Cell, Science, PLOS).
- **Grayscale Print Legibility Verification**: Ensure figures remain completely readable when printed in black and white by journal reviewers or conference attendees.
- **Clinical Trial Data Visualization**: Design accessible survival curves (Kaplan-Meier), patient stratification plots, and diagnostic biomarkers to avoid critical data misinterpretation.
- **Automated Bioinformatic Pipelines**: Programmatically check custom dynamically generated color palettes in RNA-seq, proteomics, or GWAS visualization scripts.
- **GraphPad Prism & R Workflow Standardization**: Export standardized color hex definitions into lab protocols and shared ggplot2 themes.

# Why This Tool Exists

Many scientific figure guidelines instruct authors to "use colorblind-safe colors," yet researchers often lack accessible tools to test their specific custom combinations or adapt existing institutional color schemes. Generic online color pickers typically rely on naive RGB Euclidean distances, which do not reflect non-linear human visual perception.

Furthermore, manual adjustments often create new conflicts with other colors in the palette. 

The **Pepkio Bio-Safe Palette Tester** bridges this gap by combining psychophysically validated CVD simulation algorithms (Viénot 1999, Brettel 1997) with the CIEDE2000 perceptual difference standard. Researchers can visually inspect simulated figure swatches online via the [bio-safe palette web tester](https://www.pepkio.com/tools/bio-safe-palette-tester) or validate palettes programmatically using the Python client.

# Installation

Install the Python client package from PyPI using `pip`:

```bash
pip install pepkio-bio-safe-palette-tester
```

Or using `uv`:

```bash
uv add pepkio-bio-safe-palette-tester
```

Package metadata is tracked on [PyPI](https://pypi.org/project/pepkio-bio-safe-palette-tester/).

# Quick Start

### Python API Usage

Set your API key as an environment variable:

```bash
export PEPKIO_API_KEY="your_pepkio_api_key"
```

Analyze palettes, simulate CVD, and generate code snippets in Python:

```python
from pepkio_bio_safe_palette_tester import PepkioClient

with PepkioClient() as client:
    # 1. Analyze an 8-color palette for accessibility conflicts
    analysis = client.run({
        "action": "analyze_palette",
        "colors": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]
    })

    result = analysis.result
    print("Palette Status:", result.get("banner", "OK"))
    print("Detected Conflicts:", len(result.get("conflicts", [])))
    
    # 2. Automatically suggest a fix for conflicting color pairs
    fix = client.run({
        "action": "suggest_fix",
        "color_a": "#E69F00",
        "color_b": "#D55E00"
    })
    print("Suggested Adjusted Hex:", fix.result.get("hex"))

    # 3. Export a ggplot2 (R) snippet
    r_snippet = client.run({
        "action": "build_snippet",
        "format": "r",
        "colors": ["#E69F00", "#56B4E9", "#009E73"]
    })
    print("\nggplot2 Code Snippet:\n", r_snippet.result.get("content"))
```

### Command Line Interface (CLI)

The package includes a built-in CLI executable `pepkio-bio-safe-palette-tester`:

```bash
# View tool manifest and actions
pepkio-bio-safe-palette-tester manifest

# Run analysis on the built-in Okabe-Ito example
pepkio-bio-safe-palette-tester run --example analyze_okabe_ito

# Analyze custom hex colors from the command line
pepkio-bio-safe-palette-tester run --input-json '{
  "action": "analyze_palette",
  "colors": ["#1b9e77", "#d95f02", "#7570b3", "#e7298a"]
}'
```

# Example Output

Representative JSON response for palette accessibility analysis:

```json
{
  "colors": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00"],
  "conflicts": [],
  "conflict_labels": [],
  "banner": "Safe: No colorblind or grayscale conflicts detected.",
  "simulations": [
    {
      "type": "protanopia",
      "colors": ["#9A9100", "#8FA2E9", "#949473", "#E3DE42", "#476CB2", "#8E6E00"]
    },
    {
      "type": "deuteranopia",
      "colors": ["#BA8500", "#6EB2E9", "#999073", "#F6DD42", "#007CB2", "#AA6200"]
    },
    {
      "type": "tritanopia",
      "colors": ["#EB9390", "#4DB7BC", "#009FA0", "#F7E1EA", "#007577", "#D45E5E"]
    },
    {
      "type": "grayscale",
      "colors": ["#A3A3A3", "#B1B1B1", "#8C8C8C", "#E0E0E0", "#676767", "#6C6C6C"]
    }
  ]
}
```

# Scientific Background

### Color Vision Deficiency (CVD) Models

Human trichromatic color vision relies on three retinal cone photopigments: L-cones (long wavelength, red), M-cones (medium wavelength, green), and S-cones (short wavelength, blue).

- **Protanopia**: Absence of functional L-cones. Simulated via Viénot et al. (1999) projection onto the dichromatic confusion line plane in LMS color space.
- **Deuteranopia**: Absence of functional M-cones. Simulated using the modified Viénot/Brettel algorithm via libDaltonLens transformation matrices.
- **Tritanopia**: Absence of functional S-cones. Simulated using Brettel et al. (1997) piecewise planar projections.

### CIEDE2000 Perceptual Color Difference ($\Delta E_{00}$)

The CIE standard $\Delta E_{00}$ quantifies perceived differences between two color stimuli in the $L^*a^*b^*$ color space, incorporating corrections for lightness ($S_L$), chroma ($S_C$), hue ($S_H$), and a rotation term ($R_T$) for the blue region:

$$\Delta E_{00} = \sqrt{\left(\frac{\Delta L'}{k_L S_L}\right)^2 + \left(\frac{\Delta C'}{k_C S_C}\right)^2 + \left(\frac{\Delta H'}{k_H S_H}\right)^2 + R_T \left(\frac{\Delta C'}{k_C S_C}\right)\left(\frac{\Delta H'}{k_H S_H}\right)}$$

- $\Delta E_{00} \ge 10.0$: High discriminability (Safe for all users).
- $5.0 \le \Delta E_{00} < 10.0$: Moderate discriminability (Warning — distinct in large areas, risky for thin lines or small scatter points).
- $\Delta E_{00} < 5.0$: Severe conflict (Indistinguishable for individuals with CVD).

# Frequently Asked Questions

### What is the most universally recommended colorblind-safe palette?
The **Okabe-Ito** palette (Okabe & Ito, 2008) is widely recognized as the gold standard 8-color universal categorical palette for scientific figures, maintaining high $\Delta E$ across normal vision, protanopia, deuteranopia, and tritanopia.

### Why is red-green problematic in scientific figures?
Protanopia and deuteranopia affect the red-green visual axis. Pure red (#FF0000) and pure green (#00FF00) collapse into nearly identical shades of yellow-brown under protan and deutan simulations.

### What is CIEDE2000 $\Delta E$?
CIEDE2000 ($\Delta E_{00}$) is the International Commission on Illumination standard for calculating human perceptual color differences. Unlike simple RGB distance, $\Delta E_{00}$ matches non-linear biological cone perception.

### How does the auto-fix feature work?
When two colors conflict ($\Delta E < 10$), the auto-fix algorithm converts the hex values into CIELAB ($L^*, a^*, b^*$), adjusts the luminance ($L^*$) and saturation ($C^*$) while preserving the hue angle ($h^\circ$), and re-evaluates $\Delta E$ until an optimal non-conflicting separation is achieved.

### Can this tool test palettes for grayscale printing?
Yes. The grayscale simulation converts color swatches to perceived photometric luminance ($Y = 0.2126R + 0.7152G + 0.0722B$ in linear sRGB space), allowing you to verify that colors remain distinguishable on black-and-white printouts.

### How many colors can I test simultaneously?
The tool supports 2 to 8 colors per custom palette. In scientific data visualization, using more than 8 categorical colors in a single plot is generally discouraged to maintain cognitive clarity.

### What export formats are supported?
You can export snippets directly for R (`ggplot2::scale_color_manual`), Python (`matplotlib.colors.ListedColormap`, `seaborn`), GraphPad Prism (XML), and raw HEX arrays.

### Is the tool compliant with journal accessibility standards?
Yes. The simulations adhere to established scientific publishing guidelines from Nature, Cell Press, Science, and the Web Content Accessibility Guidelines (WCAG).

# Web Application

For visual drag-and-drop palette tweaking, real-time simulated plot swatches, and interactive sharing, visit the hosted web application:

Web Application:
https://www.pepkio.com/tools/bio-safe-palette-tester

The web version provides an interactive interface, shareable links, protocol generation, printable worksheets, and visualization tools.

# Related Resources

- GitHub Repository: https://github.com/pepkio/pepkio-bio-safe-palette-tester
- PyPI Package: https://pypi.org/project/pepkio-bio-safe-palette-tester/
- Web Application: https://www.pepkio.com/tools/bio-safe-palette-tester

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

# Citation

If you use the Pepkio Bio-Safe Palette Tester in research publications, please cite:

```bibtex
@software{pepkio_bio_safe_palette_tester,
  author = {{Pepkio Open Science}},
  title = {Pepkio Bio-Safe Palette Tester: Color Vision Deficiency Simulation and Accessibility Optimization for Scientific Figures},
  url = {https://www.pepkio.com/tools/bio-safe-palette-tester},
  year = {2026}
}
```

# License

Distributed under the MIT License. See `LICENSE` for details.

# Keywords

bio-safe palette tester, colorblind safe palette, scientific figure accessibility, CIEDE2000 delta E, protanopia simulation, deuteranopia simulation, tritanopia simulation, grayscale figure check, Okabe-Ito palette, Wong palette, Paul Tol palette, viridis colormap, ggplot2 scale_color_manual, matplotlib ListedColormap, seaborn accessible palette, GraphPad Prism color palette, scientific data visualization, UMAP color palette, single-cell cluster colors, flow cytometry gating colors, heatmap accessibility, CIE LAB color difference, perceptual color contrast, laboratory figure design, manuscript figure preparation, Nature methods colorblind, journal figure guidelines, open science accessibility, bioinformatic visualization tool, hex color palette tester, colorblind conflict detector
