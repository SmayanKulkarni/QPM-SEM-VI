# Automation Workflows

Complete documentation of automated workflows and manual procedures in the QPM repository.

## 🎯 Workflow Overview

```
┌──────────────────────┐
│  Copilot Triggers    │  (User requests study materials)
└──────────┬───────────┘
           │
    ┌──────▼─────────┐
    │ Skill Router   │  (Check trigger phrases)
    └──────┬─────────┘
           │
      ┌────▼────────────────────────────────┐
      │ exam-notes-generator Skill Invoked   │
      └────┬─────────────────────────────────┘
           │
      ┌────▼─────────────────┐
      │ Content Extraction   │  → tools/extraction/
      └────┬─────────────────┘
           │
      ┌────▼─────────────────┐
      │ AI Generation        │  (Process extracted content)
      └────┬─────────────────┘
           │
      ┌────▼──────────────────────────────┐
      │ study-materials/generated         │  (Output)
      └─────────────────────────────────────┘
```

---

## 1️⃣ Exam Notes Generation Workflow

### Trigger Phrases
Copilot automatically invokes the exam-notes-generator skill when you use phrases like:

- "make notes from Unit 1"
- "create exam notes for Computer Vision"
- "prepare study notes"
- "summarize lecture slides"
- "revision material from these files"
- "notes from pdf"
- "make a cheatsheet"
- "prepare flashcards"

### Source Detection
The skill automatically scans these locations for source material:
```
✓ curriculum/units/UNIT-1/ through UNIT-6/
✓ subjects/computer-vision/
✓ Any uploaded syllabus PDFs
✓ Files explicitly specified by user
```

### Step-by-Step Process

#### Step 1: Request Analysis
```
User: "Make exam notes for unit 1-3 portfolio management"
  ↓
Copilot detects trigger phrase → exam-notes-generator skill invoked
  ↓
Skill loads from: .github/docs/skills/exam-notes-generator/SKILL.md
```

#### Step 2: Content Extraction
```
Source files identified:
  • curriculum/units/UNIT-1/
  • curriculum/units/UNIT-2/
  • curriculum/units/UNIT-3/
  
Extract from:
  - PDF files (.pdf)
  - Word documents (.docx)
  - PowerPoint slides (.pptx)
  - Markdown files (.md)
  
Processing:
  - OCR for scanned content (see docs/resources/ocr-strategy.md)
  - Text extraction
  - Metadata parsing
```

#### Step 3: Content Structuring
```
Organize by:
  1. Topics/Chapters (from source structure)
  2. Key concepts
  3. Definitions
  4. Examples
  5. Important formulas/theorems
  
Output structure:
  # Topic Title
  ## Subtopic
  ### Key Concepts
  - Concept: Definition
  
  ### Examples
  ...
  
  ### Key Formulas
  ...
```

#### Step 4: AI Generation
```
Using the extracted and structured content:
  ✓ Generate clear, concise notes
  ✓ Add explanations for complex topics
  ✓ Include important formulas and theorems
  ✓ Create learning objectives
  ✓ Extract key points for each section
```

#### Step 5: Citation & Attribution
```
For each claim/statement:
  ✓ Source file attribution (e.g., "Unit 1: Portfolio Management")
  ✓ Page/slide reference where available
  ✓ Section/chapter information
  
Format: [Concept] - Source: Unit 1, Page 25
```

#### Step 6: Output Generation
```
Output location: study-materials/generated/exam-notes/
Filename: {topic}-{unit}.md

Examples:
  - unit-1-3-portfolio-notes.md
  - cv-m1-m3-vision-notes.md
  - term-test-2-revision.md
```

### Example Invocation

**User Request:**
```
Create exam notes from Computer Vision modules 4-6
```

**System Response:**
1. Scans `subjects/computer-vision/modules/m4/`, `m5/`, `m6/`
2. Extracts content from `.pptx`, `.pdf`, `.md` files
3. Structures by topics (Architectures, Training, Applications, etc.)
4. Generates comprehensive notes with examples
5. Saves to `study-materials/generated/exam-notes/cv-m4-m6-notes.md`

### Quality Guidelines

✅ **DO**:
- Ground all content in provided materials
- Include source attribution for each major claim
- Organize hierarchically (H1 → H2 → H3)
- Use examples from source material
- Define key terms clearly
- Include formulas and important concepts

❌ **DON'T**:
- Invent content not in source material
- Skip citations/attributions
- Create unstructured dumps of text
- Mix unrelated topics
- Omit important formulas or theorems

---

## 2️⃣ Flashcard Generation Workflow

### Trigger
```
User: "Make flashcards from Unit 2 materials"
  ↓
Same as exam-notes workflow, but:
  - Output format: JSON (Anki-compatible)
  - Each concept = one flashcard
  - Front: Question/Concept
  - Back: Definition/Answer
```

### Format Specification
See: [docs/resources/flashcard-format.md](resources/flashcard-format.md)

```json
{
  "cards": [
    {
      "front": "What is expected return?",
      "back": "The weighted average of all possible returns, weighted by their probabilities",
      "source": "Unit 1: Expected Risk and Returns",
      "tags": ["definitions", "unit-1"]
    }
  ]
}
```

### Output Location
```
study-materials/generated/flashcards/{topic}-flashcards.json
```

---

## 3️⃣ Content Extraction Pipeline

Manual workflow for extracting and processing raw course materials.

### Prerequisites
```bash
cd /home/smayan/Desktop/QPM
source .venv/bin/activate
```

### Step 1: Basic Extraction
```bash
cd tools/extraction
python extract_unit456.py
```

**Input**: Raw PDFs/DOCX in `curriculum/units/`
**Output**: 
- Markdown: `study-materials/extracted-digests/`
- JSON: `study-materials/extracted-digests/unit456-extraction.json`
- Images: `study-materials/extracted-digests/images/`

**What it does**:
- Extracts text from PDFs (handles images/scans with OCR)
- Parses DOCX formatting
- Preserves document structure
- Extracts figures and diagrams
- Generates JSON with metadata

### Step 2: Complete Source Building
```bash
python build_complete_study_source.py
```

**Input**: Extracted content
**Output**: 
- `outputs/latex/{course}-complete-study-source.tex`
- `outputs/compiled/{course}-complete-study-source.md`

**What it does**:
- Combines multiple extractions
- Normalizes formatting
- Adds cross-references
- Prepares for compilation

### Step 3: Processing & Refinement
```bash
cd ../processing
python polish_tex_equations.py {input_file}
```

**Input**: LaTeX or Markdown with equations
**Output**: Cleaned version with:
- Standardized equation formatting
- Fixed mathematical symbols
- Corrected spacing

```bash
python reformat_latex.py {input_file} --output {output_file}
```

**Input**: Raw LaTeX
**Output**: 
- Proper indentation
- Section hierarchy
- Bibliography formatting

### Full Pipeline Example

```bash
# 1. Extract units 4-6
python extract_unit456.py --units 4,5,6

# 2. Build complete source
python build_complete_study_source.py --input-dir study-materials/extracted-digests

# 3. Polish equations
python tools/processing/polish_tex_equations.py outputs/latex/*.tex

# 4. Reformat
python tools/processing/reformat_latex.py outputs/latex/*.tex

# 5. Compile to PDF
cd tools/compilation
bash compile_latex.sh
```

---

## 4️⃣ LaTeX Compilation Workflow

### Prerequisites
```bash
# Requires: pdflatex, xelatex, or lualatex
# On Ubuntu/Debian:
sudo apt-get install texlive-full

# On macOS:
brew install basictex
```

### Compilation Steps
```bash
cd tools/compilation
bash compile_latex.sh --input outputs/latex/myfile.tex
```

**What the script does**:
1. Runs `pdflatex` (or configured engine)
2. Handles bibliography with `bibtex` if needed
3. Manages figure/image paths
4. Generates cross-references
5. Creates final PDF in `outputs/compiled/`

### Manual Compilation
```bash
cd outputs/latex

# First pass
pdflatex -interaction=nonstopmode cv-modules-4-6-complete-study-source.tex

# Handle bibliography if needed
bibtex cv-modules-4-6-complete-study-source.aux

# Second pass (rebuild references)
pdflatex -interaction=nonstopmode cv-modules-4-6-complete-study-source.tex

# Third pass (finalize)
pdflatex -interaction=nonstopmode cv-modules-4-6-complete-study-source.tex

# Output will be: cv-modules-4-6-complete-study-source.pdf
```

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "Package not found" | Run `texdoc {package}` to check, may need additional texlive packages |
| Figure not found | Check image paths in LaTeX, verify files in `outputs/compiled/images/` |
| Encoding errors | Use `xelatex` instead of `pdflatex` for Unicode |
| Memory exceeded | Remove temporary files: `rm *.aux *.log *.out` |

### Cleanup
```bash
# Keep only PDF and source .tex
rm *.aux *.log *.out *.toc

# Or automated:
cd tools/compilation
bash compile_latex.sh --clean
```

---

## 5️⃣ File Conversion Workflow

For converting Office formats → Markdown/LaTeX

### Prerequisites
```bash
# LibreOffice headless mode
sudo apt-get install libreoffice

# Or macOS:
brew install libreoffice
```

### PPTX → PDF → Markdown
```bash
# See: docs/resources/soffice-convert.md

# Step 1: Convert to PDF
soffice --headless --convert-to pdf subjects/computer-vision/modules/m1/*.pptx

# Step 2: Extract with OCR if needed
python tools/extraction/extract_unit456.py --input *.pdf --format markdown

# Step 3: Polish and refine
python tools/processing/polish_tex_equations.py output.md
```

### DOCX → Markdown
```bash
# Using pandoc (if installed):
pandoc curriculum/units/UNIT\ 1/*.docx -o study-materials/extracted-digests/unit-1.md

# Or using python-docx:
python -c "from docx import Document; ..."
```

---

## 6️⃣ Adding New Workflows

### Template for Custom Extraction Tool

```python
# tools/extraction/extract_newcontent.py

import sys
from pathlib import Path

def extract_content(source_dir, output_dir):
    """
    Extract content from source_dir → output_dir
    
    Args:
        source_dir: Path to content (PDF, DOCX, PPTX, etc.)
        output_dir: Path to write Markdown/JSON
        
    Returns:
        dict: Metadata about extraction
    """
    # Implementation
    pass

if __name__ == "__main__":
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    output = Path("study-materials/extracted-digests")
    
    metadata = extract_content(source, output)
    print(f"✓ Extracted to {output}")
    print(metadata)
```

### Register with Copilot (Optional)
Add to `.github/docs/copilot-instructions.md`:
```markdown
## Custom Workflow: [Name]

When user says: "[trigger phrase]"
1. Run tool: tools/extraction/extract_newcontent.py
2. Output to: study-materials/generated/[type]/
3. Format: [format spec]
```

---

## 🔄 Typical User Journeys

### Journey 1: Quick Exam Prep
```
User: "I need notes for Unit 2 exam tomorrow"
  ↓
Copilot: Triggers exam-notes-generator
  ↓
Skill extracts Unit 2 → generates notes → study-materials/generated/exam-notes/
  ↓
User: Reviews notes, exports to phone
  ↓
Outcome: ✓ 20-min exam prep complete
```

### Journey 2: Deep Study Material
```
User: "Create comprehensive study guide for CV modules 1-6"
  ↓
Step 1: AI generates notes (exam-notes-generator)
  ↓
Step 2: AI generates flashcards (same workflow, different output)
  ↓
Step 3: Manual: Polish notes, add examples
  ↓
Step 4: Compile to PDF for printing
  ↓
Outcome: ✓ Complete study package
```

### Journey 3: Content Processing
```
User: "Extract and compile Unit 4-6 into a PDF"
  ↓
Step 1: Manual extraction: python extract_unit456.py --units 4,5,6
  ↓
Step 2: Build source: python build_complete_study_source.py
  ↓
Step 3: Polish: python polish_tex_equations.py
  ↓
Step 4: Compile: bash compile_latex.sh
  ↓
Outcome: ✓ PDF in outputs/compiled/
```

---

## 📊 Workflow Metrics

Typical performance:

| Workflow | Input | Time | Output |
|----------|-------|------|--------|
| Exam Notes | 100-page unit | 2-5 min | 5-10 page markdown |
| Flashcards | 50-page chapter | 1-3 min | 50-100 card JSON |
| Full Extraction | 6 units (300+ pages) | 10-15 min | Complete digests |
| LaTeX Compile | ~50 pages | 30-60 sec | PDF |

---

## 🔍 Troubleshooting

### Notes not generating?
1. Check `.github/docs/copilot-instructions.md` trigger phrases
2. Verify curriculum/subjects files exist
3. Check file format (PDF, DOCX, PPTX supported)

### Extraction failing?
1. Check Python environment: `python --version`
2. Verify dependencies installed
3. Check source file integrity

### PDF compilation errors?
1. Check LaTeX syntax
2. Verify image paths
3. See Common Issues table above

---

## 📝 Required Improvements / TODOs

- [ ] Add support for direct image extraction
- [ ] Implement automatic LaTeX → HTML conversion
- [ ] Add workflow for creating mind maps
- [ ] Support for handwriting OCR in scanned notes
- [ ] Automated cross-referencing between units
