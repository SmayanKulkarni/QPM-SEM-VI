# Compilation Tools

Scripts and utilities for compiling extracted content into professional PDF documents using LaTeX.

## Tools Overview

### `compile_latex.sh`
Bash script to compile LaTeX files to PDF with automatic dependency handling.

**Usage**:
```bash
bash compile_latex.sh --input outputs/latex/myfile.tex
```

**Features**:
- Automatic multi-pass compilation
- Bibliography support (bibtex)
- Cross-reference resolution
- Figure/image path handling
- Error reporting
- Cleanup mode

**Supported Engines**:
- `pdflatex` (default)
- `xelatex` (for Unicode/complex fonts)
- `lualatex` (for OpenType fonts)

---

## Prerequisites

### Linux/Ubuntu
```bash
sudo apt-get install texlive-full
# or minimal:
sudo apt-get install texlive texlive-latex-extra texlive-fonts-recommended
```

### macOS
```bash
# Full installation
brew install basictex

# Additional packages (run as needed):
sudo tlmgr install amsmath amssymb babel geometry hyperref
```

### macOS (Alternative - MacTeX)
```bash
# Download from: https://tug.org/mactex/
# Large download (~4GB) but all-inclusive
```

### Windows
1. Download and install MiKTeX: https://miktex.org/download
2. Or: TeXLive on Windows: https://tug.org/texlive/

---

## Usage

### Basic Compilation
```bash
bash compile_latex.sh --input outputs/latex/complete-study-source.tex
```

**Output**: `outputs/latex/complete-study-source.pdf`

### With Custom Output Directory
```bash
bash compile_latex.sh \
  --input outputs/latex/myfile.tex \
  --output outputs/compiled/myfile.pdf
```

### Using Specific LaTeX Engine
```bash
bash compile_latex.sh \
  --input outputs/latex/myfile.tex \
  --engine xelatex  # for Unicode/complex fonts
```

### Multiple Files
```bash
bash compile_latex.sh \
  --input outputs/latex/*.tex \
  --output outputs/compiled/
```

### With Bibliography
```bash
bash compile_latex.sh \
  --input outputs/latex/myfile.tex \
  --bibtex  # Enable bibliography processing
```

### Cleanup (Remove Intermediate Files)
```bash
bash compile_latex.sh \
  --input outputs/latex/myfile.tex \
  --cleanup  # Delete .aux, .log, .out, etc.
```

---

## Manual Compilation

If you prefer manual control:

### Single-Pass (Simple Documents)
```bash
cd outputs/latex
pdflatex -interaction=nonstopmode myfile.tex
```

### Multi-Pass (With References/TOC)
```bash
cd outputs/latex

# First pass: initial compilation
pdflatex -interaction=nonstopmode myfile.tex

# Second pass: resolve references
pdflatex -interaction=nonstopmode myfile.tex

# Final pass: ensure all references correct
pdflatex -interaction=nonstopmode myfile.tex
```

### With Bibliography (Full Process)
```bash
cd outputs/latex

# Step 1: Initial compilation
pdflatex -interaction=nonstopmode myfile.tex

# Step 2: Extract bibliography references
bibtex myfile.aux

# Step 3: Recompile with bibliography
pdflatex -interaction=nonstopmode myfile.tex

# Step 4: Final pass
pdflatex -interaction=nonstopmode myfile.tex
```

### Using XeLaTeX (for Unicode)
```bash
cd outputs/latex
xelatex -interaction=nonstopmode myfile.tex
xelatex -interaction=nonstopmode myfile.tex  # Second pass
```

---

## Common Issues & Solutions

### Issue: "PDF is not finalized" in viewer
**Solution**: Run compilation 3 times:
```bash
pdflatex myfile.tex
pdflatex myfile.tex
pdflatex myfile.tex
```

### Issue: "I can't find file 'image.png'" 
**Solution**: Check image paths in LaTeX:
```latex
% Relative to myfile.tex location:
\includegraphics{images/figure-1.png}

% Or absolute:
\includegraphics{/home/user/outputs/compiled/images/figure-1.png}
```

Then verify files exist:
```bash
ls outputs/compiled/images/
```

### Issue: "Package '[packagename]' not found"
**Solution**: Install missing package:
```bash
# Ubuntu:
sudo apt-get install texlive-latex-extra-recommended

# macOS:
sudo tlmgr install {packagename}

# Or from CTAN:
texdoc {packagename}
```

### Issue: "! LaTeX Error: Something's wrong--perhaps a missing \item"
**Solution**: Check LaTeX syntax:
```latex
% Must have at least one item:
\begin{itemize}
  \item First item
  \item Second item
\end{itemize}

# Not:
\begin{itemize}
  \end{itemize}
```

### Issue: Encoding errors (strange characters)
**Solution**: Use XeLaTeX instead:
```bash
xelatex -interaction=nonstopmode myfile.tex
```

Or ensure UTF-8 in preamble:
```latex
\usepackage[utf8]{inputenc}
```

### Issue: Bibliography not appearing
**Solution**: Ensure `.bib` file exists and bibtex ran:
```bash
pdflatex myfile.tex
bibtex myfile.aux  # Creates .bbl file
pdflatex myfile.tex
pdflatex myfile.tex
```

### Issue: Out of memory error
**Solution**: Reduce document complexity or increase memory:
```bash
# In preamble:
\usepackage{fix-cm}

# Or configure TeX:
texmf.cnf: main_memory = 10000000  # 10GB
```

### Issue: "Overfull \hbox" warnings
**Solution**: This is usually harmless but can be fixed:
```latex
% Add flexibility:
\usepackage{ragged2e}

% Or adjust margins:
\usepackage[margin=1in]{geometry}
```

---

## Workflow Examples

### Generate CV Study Notes (Complete)
```bash
# 1. Extract
cd tools/extraction
python extract_unit456.py --source subjects/computer-vision/modules --units m1,m2,m3,m4,m5,m6

# 2. Build source
python build_complete_study_source.py \
  --inputs study-materials/extracted-digests/cv-*.md \
  --output outputs/latex/cv-complete.tex

# 3. Polish equations
python tools/processing/polish_tex_equations.py outputs/latex/cv-complete.tex --inplace

# 4. Compile to PDF
cd tools/compilation
bash compile_latex.sh --input outputs/latex/cv-complete.tex --output outputs/compiled/cv-complete.pdf

# 5. View
open outputs/compiled/cv-complete.pdf
```

### Generate Term Test II Study Guide
```bash
# Extract Units 4-6
cd tools/extraction
python extract_unit456.py --units 4,5,6

# Build combined source
python build_complete_study_source.py \
  --inputs study-materials/extracted-digests/unit-*.md \
  --title "Term Test II: Units 4-6" \
  --output outputs/latex/tt2-units456.tex

# Compile
cd ../compilation
bash compile_latex.sh \
  --input outputs/latex/tt2-units456.tex \
  --cleanup

# Result in: outputs/compiled/tt2-units456.pdf
```

### Batch Compile All LaTeX Files
```bash
cd tools/compilation
for file in outputs/latex/*.tex; do
  bash compile_latex.sh --input "$file" --cleanup
done

# All PDFs now in: outputs/compiled/
```

---

## LaTeX Preamble Templates

### Minimal (Exam Notes)
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\title{Study Notes}
\author{}
\date{}

\begin{document}
\maketitle
\tableofcontents

% Content here

\end{document}
```

### Comprehensive (Full Study Guide)
```latex
\documentclass[12pt,oneside]{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, mathtools}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{listings}

\geometry{margin=1in}
\pagestyle{fancy}
\fancyhf{}
\rhead{Portfolio Management}
\lhead{\leftmark}
\cfoot{\thepage}

% Define colors
\definecolor{darkblue}{rgb}{0,0,0.5}
\hypersetup{colorlinks=true, linkcolor=darkblue}

\title{Complete Study Guide}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

% Content here

\end{document}
```

---

## Troubleshooting Checklist

Before asking for help:

- [ ] Verify `.tex` file is valid (opens in text editor)
- [ ] Run: `pdflatex -interaction=nonstopmode myfile.tex` (check error line)
- [ ] Check image paths: `\includegraphics{path/to/image.pdf}`
- [ ] Verify all required packages installed: `tlmgr list --installed`
- [ ] Try XeLaTeX: `xelatex -interaction=nonstopmode myfile.tex`
- [ ] Check for syntax errors: `\documentclass{} \begin{document} \end{document}`
- [ ] Ensure `.tex` file encoding is UTF-8

---

## Performance

Typical compilation times:

| Document | Pages | Time |
|----------|-------|------|
| Simple exam notes | 20 | 5-10s |
| Complete study guide | 100 | 30-60s |
| Large with many figures | 200+ | 1-2min |

---

## Advanced Configuration

### Configure Default Engine
Edit in compile_latex.sh:
```bash
# Find this line:
ENGINE="${engine:-pdflatex}"

# Change to:
ENGINE="${engine:-xelatex}"  # Use XeLaTeX by default
```

### Custom LaTeX Configuration
Create `texmf.cnf` for system-wide settings:
```bash
mkdir -p ~/.texmf-var/tex/latex/myconfig
# Add custom sty files here
```

### Continuous Compilation (Watch Mode)
```bash
# Install latexmk:
sudo apt-get install latexmk

# Use watch mode:
latexmk -pvc myfile.tex  # Recompile on save, auto-viewer
```

---

## See Also

- [Extraction Tools README](../extraction/README.md)
- [Processing Tools README](../processing/README.md)
- [LaTeX Documentation](https://www.latex-project.org/help/)
- [Overleaf Tutorials](https://www.overleaf.com/learn)
