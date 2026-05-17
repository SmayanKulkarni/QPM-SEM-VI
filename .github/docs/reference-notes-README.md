# Reference Study Notes

This directory contains example, production-ready study notes in LaTeX format. These serve as the quality standard for all note generation in this repository.

## Available References

### CV Modules 4-6 (Computer Vision)

- **File:** `cv-modules-4-6/cv-modules-4-6-complete-study-source.tex`
- **Scope:** Complete study material covering Generative Adversarial Networks (GANs), Object Segmentation, and Video Understanding
- **Size:** 468 lines of LaTeX code
- **Figures:** 26 supporting diagrams and visualizations in `cv-modules-4-6/figures/`

#### Quality Features Demonstrated

This reference LaTeX document showcases:
- ✅ Complete `\documentclass[11pt,a4paper]{article}` with full preamble
- ✅ All required packages (amsmath, amssymb, graphicx, hyperref, tcolorbox, enumitem, xcolor, float, geometry)
- ✅ Structured table of contents via `\tableofcontents`
- ✅ Deep sectioning hierarchy: `\section` → `\subsection` → `\subsubsection`
- ✅ Rich text formatting: `\textbf{}` for key terms, `\textit{}` for emphasis
- ✅ Nested lists with `\begin{itemize}` / `\begin{enumerate}` preserving source structure
- ✅ Proper equation blocks using `\[...\]` and `\begin{equation}` environments
- ✅ `tcolorbox` callout boxes with colored backgrounds for:
  - Key concept definitions and principles
  - Important formulas and theorems
  - Worked numerical problems with step-by-step solutions
- ✅ Figure inclusion with `\begin{figure}[H]` blocks, captions, and proper image referencing
- ✅ Consistent spacing and formatting via `\setlist` for list items
- ✅ Clean compilation with `pdflatex` or `xelatex` without errors or warnings

#### How to Use as a Template

When generating new study notes:

1. **Examine the preamble** in lines 1-25 — this is the required structure for all new documents
2. **Review the section structure** — note how `\section` and `\subsection` break down topics hierarchically
3. **Copy the tcolorbox styles** — use the same color schemes and formatting for callouts
4. **Follow the figure pattern** — use `\begin{figure}[H]` blocks with `\includegraphics{figures/...}` references
5. **Preserve list nesting** — do not flatten nested bullets into paragraphs
6. **Include all details** — every concept, formula, and diagram from source material should appear

---

## Adding New Reference Notes

When generating notes for a new subject or module:

1. Create a new subdirectory: `.github/reference-notes/[subject]-[range]/`
2. Generate the `.tex` file and save to: `.github/reference-notes/[subject]-[range]/[subject]-[range]-complete-study-source.tex`
3. Create a `figures/` subdirectory with all referenced figures
4. Update this README to document the new reference

---

## Usage in Note Generation Workflows

All note-generation requests should:
- Reference this file when establishing output structure: `.github/reference-notes/cv-modules-4-6/cv-modules-4-6-complete-study-source.tex`
- Match the preamble, sectioning layout, and formatting style shown here
- Ensure generated `.tex` files compile cleanly, just as this reference does
- Preserve source material detail and hierarchy, as demonstrated in this comprehensive example
