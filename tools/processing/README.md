# Processing Tools

Utilities for post-processing extracted and generated content to improve formatting, readability, and compilation compatibility.

## Tools Overview

### `polish_tex_equations.py`
Standardize and improve mathematical equations in LaTeX and Markdown.

**Usage**:
```bash
python polish_tex_equations.py documents/myfile.tex
```

**Input Formats**: LaTeX `.tex`, Markdown `.md`

**Output**: Cleaned file with standardized math formatting

**What It Does**:
- Converts inline math: `$...$` → `\(...\)`
- Converts display math: `$$...$$` → `\[...\]`
- Fixes mathematical symbol formatting
- Standardizes spacing around operators
- Validates LaTeX math syntax
- Improves readability

**Examples**:

Before:
```latex
The formula is $E[R] = \sum p_i * r_i$ where
$$
\text{Var}(R) = E[R^2] - E[R]^2
$$
```

After:
```latex
The formula is \(E[R] = \sum p_i \cdot r_i\) where
\[
\text{Var}(R) = E[R^2] - E[R]^2
\]
```

---

### `reformat_latex.py`
Restructure and improve LaTeX document formatting and organization.

**Usage**:
```bash
python reformat_latex.py outputs/latex/myfile.tex --output formatted_myfile.tex
```

**Input**: Raw LaTeX file
**Output**: Reformatted LaTeX with consistent style

**What It Does**:
- Fixes indentation and spacing
- Normalizes section hierarchy
- Formats package declarations
- Improves readability
- Validates structure
- Creates consistent formatting

**Examples**:

Before:
```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[utf8]{inputenc}
\title{My Document}

\begin{document}
\chapter{First}
\section{Subsection}
Lots         of     spacing
\end{document}
```

After:
```latex
\documentclass{article}

\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}

\title{My Document}

\begin{document}

\chapter{First}

\section{Subsection}

Lots of spacing

\end{document}
```

---

## Setup

### Prerequisites
```bash
cd /path/to/QPM
source .venv/bin/activate
```

### Dependencies
```bash
pip install sympy  # For equation parsing
pip install regex  # For advanced pattern matching
```

---

## Detailed Usage

### Polish Equations Only
```bash
python polish_tex_equations.py myfile.tex --math-only
```

### Dry Run (Show Changes Without Saving)
```bash
python polish_tex_equations.py myfile.tex --dry-run
```

### Reformat LaTeX Structure
```bash
python reformat_latex.py myfile.tex --output formatted.tex
```

### Fix In Place (Overwrite Original)
```bash
python polish_tex_equations.py myfile.tex --inplace
python reformat_latex.py myfile.tex --inplace
```

### Verbose Mode (Show All Changes)
```bash
python polish_tex_equations.py myfile.tex --verbose
python reformat_latex.py myfile.tex --verbose
```

---

## Common Workflows

### Complete Processing Pipeline
```bash
# 1. Extract content
cd tools/extraction
python extract_unit456.py --units 4,5,6

# 2. Build combined source
python build_complete_study_source.py \
  --inputs study-materials/extracted-digests/unit-*.md \
  --output outputs/latex/units-456.tex

# 3. Polish equations
cd ../processing
python polish_tex_equations.py outputs/latex/units-456.tex --inplace

# 4. Reformat structure
python reformat_latex.py outputs/latex/units-456.tex --inplace

# 5. Compile to PDF
cd ../compilation
bash compile_latex.sh --input outputs/latex/units-456.tex
```

### Batch Process Equations in Multiple Files
```bash
cd tools/processing
for file in outputs/latex/*.tex; do
  python polish_tex_equations.py "$file" --inplace
done

echo "All files processed!"
```

### Fix Specific Elements
```bash
# Only fix spacing issues
python polish_tex_equations.py myfile.tex --fix-spacing

# Only fix symbols
python polish_tex_equations.py myfile.tex --fix-symbols

# Only convert environments
python polish_tex_equations.py myfile.tex --fix-environments
```

---

## Equation Transformations

### Inline Math Conversions

| Input | Output | Context |
|-------|--------|---------|
| `$E[R]$` | `\(E[R]\)` | Text |
| `$ E[R] $` | `\(E[R]\)` | With spaces |
| `\$...\$` | `\(...\)` | Escaped |

### Display Math Conversions

| Input | Output | Context |
|-------|--------|---------|
| `$$E = mc^2$$` | `\[E = mc^2\]` | Centered |
| `\[...\]` | `\[...\]` | Already correct |
| `align*` | `align*` | Alignment env |

### Symbol Fixes

| Input | Output | Note |
|-------|--------|------|
| `*` (between variables) | `\cdot` | Multiplication |
| `x^{2}` | `x^{2}` | Correct |
| `{1 \over 2}` | `\frac{1}{2}` | Modern form |
| `\_` (underscore) | `\_` | Escaped |

### Spacing Fixes

| Input | Output |
|-------|--------|
| `x   y` | `x y` |
| `{ x}` | `{x}` |
| `x} y` | `x} y` |

---

## Configuration

### Custom Rules File
Create `polish_config.yaml`:
```yaml
conversions:
  inline_math: true
  display_math: true
  symbols: true
  spacing: true

symbol_mappings:
  '*': '\cdot'
  '/': '\frac'

preserve_patterns:
  - 'url\{'
  - 'href\{'
```

Use with:
```bash
python polish_tex_equations.py myfile.tex --config polish_config.yaml
```

---

## Troubleshooting

### Issue: Equations Not Converting
**Problem**: Regex not matching your format
**Solution**: Check format:
```bash
python polish_tex_equations.py myfile.tex --dry-run --verbose
# See what patterns are found
```

### Issue: Spaces Removed from Important Areas
**Problem**: Spacing fix too aggressive
**Solution**: Add preserve patterns:
```bash
python polish_tex_equations.py myfile.tex \
  --preserve-spaces-in "{\LaTeX}"
```

### Issue: Symbols Changed Incorrectly
**Problem**: Context misunderstood
**Solution**: Use custom mapping:
```bash
python reformat_latex.py myfile.tex \
  --preserve-patterns "url\{|href\{"
```

### Issue: Structure Reformatting Breaks Document
**Problem**: Custom packages or unusual structure
**Solution**: Use dry-run first:
```bash
python reformat_latex.py myfile.tex --dry-run --verbose
# Review changes before applying
```

---

## Performance

Typical processing times:

| File Size | Type | Time |
|-----------|------|------|
| 20 pages | Equations | 2-5s |
| 20 pages | Full reformat | 5-10s |
| 100 pages | Equations + reformat | 30-60s |

---

## Advanced Features

### Custom Transformation Rules
Extend `polish_tex_equations.py`:

```python
# Add custom transformation
def my_transform(text):
    """Custom transformation logic"""
    return transformed_text

# Register:
CUSTOM_TRANSFORMS = {
    'my_fix': my_transform
}
```

### Preserve Regions
Prevent transformation in specific areas:

```bash
python polish_tex_equations.py myfile.tex \
  --preserve-between "\\begin{verbatim}" "\\end{verbatim}"
```

### Format Hooks
After transformation, apply formatting:

```python
# In reformat_latex.py
POST_PROCESSES = [
    fix_indentation,
    add_blank_lines,
    sort_imports,
]
```

---

## Best Practices

1. **Always Dry Run First**
   ```bash
   python polish_tex_equations.py myfile.tex --dry-run
   ```

2. **Keep Original**
   ```bash
   cp myfile.tex myfile.backup.tex
   # Then process
   ```

3. **Batch Process with Care**
   ```bash
   # Test on one file first
   python polish_tex_equations.py test.tex --inplace
   
   # Then batch
   for file in *.tex; do python polish_tex_equations.py "$file" --inplace; done
   ```

4. **Review Changes**
   ```bash
   git diff outputs/latex/myfile.tex  # See all changes
   ```

5. **Validate After Processing**
   ```bash
   pdflatex -interaction=nonstopmode myfile.tex  # Check for errors
   ```

---

## Related Tools

- [Extraction Tools](../extraction/README.md) - Extract raw content
- [Compilation Tools](../compilation/README.md) - Compile to PDF
- [Building Study Sources](../extraction/build_complete_study_source.py) - Combine extracts

---

## Examples

### Example 1: Polish and Reformat a Study Guide

```bash
# Original: raw extracted LaTeX
cat outputs/latex/raw-units-456.tex | head -20
# Messy formatting, inconsistent equations

# Process it
python tools/processing/polish_tex_equations.py \
  outputs/latex/raw-units-456.tex --inplace

python tools/processing/reformat_latex.py \
  outputs/latex/raw-units-456.tex --inplace

# Result: clean, formatted file ready for PDF
cat outputs/latex/raw-units-456.tex | head -20
# Proper spacing, standard equation format
```

### Example 2: Fix Specific Equation Environment

Before (Markdown):
```markdown
The return is calculated as:
$$R = \sum p_i * r_i$$

where:
- R is total return
- $p_i$ is probability
```

After:
```markdown
The return is calculated as:
\[R = \sum p_i \cdot r_i\]

where:
- \(R\) is total return
- \(p_i\) is probability
```

Process:
```bash
python polish_tex_equations.py study-notes.md --inplace
```

---

## Future Enhancements

- [ ] Support for MathML conversion
- [ ] Automatic formula simplification
- [ ] Cross-reference validation
- [ ] Bibliography formatting
- [ ] TikZ diagram optimization
