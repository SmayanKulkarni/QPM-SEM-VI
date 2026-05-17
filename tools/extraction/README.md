# Extraction Tools

Scripts for extracting content from course materials (PDF, DOCX, PPTX) and converting to usable formats (Markdown, JSON).

## Tools Overview

### `extract_unit456.py`
Extract specific units from curriculum materials.

**Usage**:
```bash
python extract_unit456.py --units 4,5,6 --output /path/to/output
```

**Input**: Files from `curriculum/units/`
**Output**: 
- Markdown files: `study-materials/extracted-digests/`
- JSON metadata: `study-materials/extracted-digests/unit456-extraction.json`
- Images: `study-materials/extracted-digests/images/`

**Supported Formats**: PDF, DOCX, PPTX

---

### `extract_and_prep.py`
Full extraction and preparation pipeline in one command.

**Usage**:
```bash
python extract_and_prep.py --source curriculum/units/UNIT\ 1 --output study-materials/extracted-digests
```

**Input**: Any course material folder
**Output**: Cleaned, formatted content ready for compilation or AI processing

**Process**:
1. Extract text, tables, images
2. Normalize formatting
3. Identify sections and hierarchy
4. Create metadata
5. Generate JSON structure

---

### `build_complete_study_source.py`
Combine multiple extractions into a single cohesive document.

**Usage**:
```bash
python build_complete_study_source.py \
  --inputs unit1.md,unit2.md,unit3.md \
  --output outputs/latex/complete-study-source.tex
```

**Input**: Multiple extracted markdown/JSON files
**Output**: Complete LaTeX source file with:
- Unified formatting
- Proper section hierarchy
- Cross-references
- Bibliography structure

**Features**:
- Merges multiple unit extractions
- Handles missing pages/sections
- Creates table of contents
- Adds index entries
- Generates citation references

---

### `polish_tex_equations.py`
Polish and standardize mathematical equations in LaTeX.

**Usage**:
```bash
python polish_tex_equations.py outputs/latex/*.tex --inplace
```

**Fixes**:
- Standardizes equation environments (`$...$` → `\(...\)`)
- Fixes mathematical symbols
- Corrects spacing around operators
- Validates LaTeX math syntax
- Creates consistent formatting

---

## Setup

### Prerequisites
```bash
# Virtual environment
python -m venv /path/to/venv
source /path/to/venv/bin/activate

# Dependencies (see requirements.txt)
pip install -r requirements.txt
```

### Common Dependencies
- `pdf2image` - PDF to image conversion
- `pytesseract` - OCR for scanned PDFs
- `python-docx` - DOCX parsing
- `python-pptx` - PPTX parsing
- `pypdf` - PDF text extraction
- `pillow` - Image processing
- `markdown` - Markdown generation
- `PyYAML` - YAML parsing

### System Requirements

**Linux/Ubuntu**:
```bash
sudo apt-get install python3-dev tesseract-ocr poppler-utils
```

**macOS**:
```bash
brew install tesseract poppler pdftoppm
```

**Windows**:
- Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
- Download Poppler from: https://github.com/oschwartz10612/poppler-windows/releases/

---

## Common Workflows

### Extract a Single Unit
```bash
python extract_unit456.py --units 1 --format markdown
# Output: study-materials/extracted-digests/unit-1.md
```

### Extract Multiple Units → LaTeX → PDF
```bash
# 1. Extract
python extract_unit456.py --units 4,5,6

# 2. Combine
python build_complete_study_source.py \
  --inputs study-materials/extracted-digests/unit-*.md \
  --output outputs/latex/units-4-6.tex

# 3. Polish
python polish_tex_equations.py outputs/latex/units-4-6.tex --inplace

# 4. Compile (see tools/compilation/)
cd ../compilation
bash compile_latex.sh units-4-6.tex
```

### Extract with OCR (for scanned PDFs)
```bash
python extract_unit456.py --units 2 --use-ocr --confidence 0.8
# Uses Tesseract for scanned content
```

### Extract Computer Vision Materials
```bash
python extract_unit456.py \
  --source subjects/computer-vision/modules \
  --units m1,m2,m3 \
  --format json
```

---

## Troubleshooting

### OCR Not Working
**Problem**: Tesseract not found or slow
**Solution**: 
```bash
# Disable OCR and use text extraction only
python extract_unit456.py --no-ocr

# Or verify Tesseract is installed:
which tesseract  # Linux/macOS
where tesseract  # Windows
```

### PDF Extraction Issues
**Problem**: Text not extracted from PDF
**Solution**:
```bash
# Try with OCR:
python extract_unit456.py --use-ocr

# Or check PDF:
python -c "from PyPDF2 import PdfReader; pdf = PdfReader('file.pdf'); print(len(pdf.pages))"
```

### Memory Issues
**Problem**: Script crashes on large files
**Solution**:
```bash
# Process file in chunks:
python extract_unit456.py --chunk-size 100  # Process 100 pages at a time

# Or increase available memory:
python -c "import sys; print(sys.maxsize)"  # Check limit
```

### DOCX/PPTX Parsing Errors
**Problem**: Corruption or formatting issues
**Solution**:
```bash
# Extract images only:
python extract_unit456.py --extract-images-only

# Or convert to PDF first:
soffice --headless --convert-to pdf file.docx
```

---

## Output Formats

### Markdown Output
```markdown
# Unit 1: Portfolio Management

## Section A: Overview

### 1.1 Introduction to Portfolio Theory
Text content here...

### 1.2 Key Concepts
- Concept 1: Definition
- Concept 2: Definition

**Important Formula**: $E[R] = \sum p_i r_i$

[Source: Page 15, Unit 1 Portfolio Management.docx]
```

### JSON Output
```json
{
  "unit": "1",
  "title": "Portfolio Management",
  "sections": [
    {
      "title": "Overview",
      "subsections": [
        {
          "title": "Introduction",
          "content": "...",
          "page": 15,
          "source_file": "UNIT 1 Portfolio Management.docx"
        }
      ]
    }
  ],
  "extracted_images": [
    {
      "filename": "figure-1-1.png",
      "caption": "Efficient Frontier",
      "page": 18
    }
  ]
}
```

### LaTeX Output
```latex
\documentclass{report}
\usepackage{amsmath}

\begin{document}

\chapter{Portfolio Management}

\section{Overview}

\subsection{Introduction to Portfolio Theory}
Text content here...

\end{document}
```

---

## Performance Notes

Typical extraction speeds:

| Format | Pages | Time | Output Size |
|--------|-------|------|-------------|
| PDF (text) | 50 | 10s | 200KB |
| PDF (OCR) | 50 | 2-5min | 250KB |
| DOCX | 50 | 5s | 150KB |
| PPTX | 50 slides | 15s | 300KB |

For 300+ page units, expect 5-15 minutes with OCR.

---

## Development

To extend these tools:

1. **Add Format Support**: Modify `__init__.py` to register new parsers
2. **Custom Processing**: Add hooks in `build_complete_study_source.py`
3. **New Extractors**: Create `extract_myformat.py` following same pattern

See individual script headers for detailed docstrings and API.
