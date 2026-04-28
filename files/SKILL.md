---
name: exam-notes-generator
description: >
  Use this skill whenever the user wants to generate study notes, revision material, 
  summaries, cheatsheets, flashcards, or any exam-prep content from course material files.
  Triggers on phrases like: "make notes", "create notes", "study notes", "exam notes",
  "summarize my lecture", "notes from slides", "notes from PDF", "notes from this file",
  "prepare me for exam", "revise this topic", "make a cheatsheet", or any request to
  understand and extract structured knowledge from uploaded DOCX, PPTX, PPT, or PDF files.

  This skill MUST be used when:
  - User uploads any course material (lecture slides, textbook chapters, handouts) and
    asks for notes, summaries, or exam prep
  - User provides a syllabus and wants topic-by-topic notes organized to it
  - User asks to "go through" a folder or set of files and create notes
  - All note content must come ONLY from the actual files — never hallucinated or assumed

  Supports: PDF (including scanned/image-based), DOCX, DOC, PPTX, PPT
  Extracts: Text, embedded images (diagrams, charts, figures), tables
  Outputs: Structured Markdown notes, optionally saved as .md or .docx
---

# Exam Notes Generator

A skill for reading course material files (PDF, DOCX, PPTX) — including embedded images —
and producing accurate, well-structured study notes aligned to a syllabus.

**Golden rule: Every fact in the notes must trace back to a specific file.
If it isn't in the material, it does not go in the notes.**

---

## Step 0 — Understand the request

Before touching any file, clarify (from context or by asking):

1. **What files are the source material?** (path(s) under `/mnt/user-data/uploads/` or a folder)
2. **Is there a syllabus?** If yes, use it to structure and scope the notes.
3. **What output format is needed?** (Markdown in chat, `.md` file, `.docx` file, flashcards, cheatsheet)
4. **Depth level?** (Quick bullet summary vs. detailed notes with examples)

If the syllabus is already in context (e.g., from the current conversation), extract unit/topic
structure from it immediately — do not ask again.

---

## Step 1 — Inventory all source files

List and stat every uploaded file before reading:

```bash
ls -lh /mnt/user-data/uploads/
file /mnt/user-data/uploads/*
```

Build a dispatch plan using the table below:

| Extension          | Reading strategy                              | Image extraction?           |
|--------------------|-----------------------------------------------|-----------------------------|
| `.pdf`             | pypdf text + pdfplumber tables + rasterize    | Yes — see PDF Images section |
| `.docx`            | extract-text (markdown) + python-docx images  | Yes — see DOCX Images section |
| `.doc` (legacy)    | Convert to .docx via LibreOffice first        | Yes after conversion        |
| `.pptx`            | extract-text (slide text) + python-pptx images| Yes — see PPTX Images section |
| `.ppt` (legacy)    | Convert to .pptx via LibreOffice first        | Yes after conversion        |

---

## Step 2 — Read each file

### 2A — PDF Files

**Text extraction (text-based PDFs):**
```python
import pdfplumber

with pdfplumber.open("/mnt/user-data/uploads/lecture.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n--- Page {i+1} ---")
        text = page.extract_text()
        if text:
            print(text)
        # Extract tables too
        for table in page.extract_tables():
            print("\n[TABLE]")
            for row in table:
                print(" | ".join(str(c) for c in row if c))
```

**Fallback for scanned/image PDFs** (no text layer):
```bash
# Check if text is extractable
pdftotext /mnt/user-data/uploads/scan.pdf - | head -30
```
If output is empty or garbled → it is a scanned PDF. Use OCR path (see `references/ocr-strategy.md`).

#### PDF Images

Rasterize pages and pass to vision for diagrams, charts, and figures:
```python
import fitz  # PyMuPDF — install: pip install pymupdf --break-system-packages

doc = fitz.open("/mnt/user-data/uploads/lecture.pdf")
for page_num in range(len(doc)):
    page = doc[page_num]
    # Extract embedded images from page
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        img_bytes = base_image["image"]
        img_ext = base_image["ext"]
        out_path = f"/tmp/pdf_img_p{page_num+1}_{img_index}.{img_ext}"
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"Saved: {out_path}")  # Then load with vision
```

For full-page rasterization (when image-heavy or layout matters):
```python
mat = fitz.Matrix(2, 2)  # 2x zoom for clarity
pix = page.get_pixmap(matrix=mat)
pix.save(f"/tmp/pdf_page_{page_num+1}.png")
```
Then use the `view` tool on each `/tmp/pdf_page_N.png` to read diagrams visually.

---

### 2B — DOCX Files

**Text + structure:**
```bash
extract-text /mnt/user-data/uploads/notes.docx
```
This emits proper Markdown with headings, bold, lists, and tables preserved.

**Images embedded in the DOCX:**
```python
from docx import Document
import os, shutil

doc = Document("/mnt/user-data/uploads/notes.docx")
out_dir = "/tmp/docx_images"
os.makedirs(out_dir, exist_ok=True)

for i, rel in enumerate(doc.part.rels.values()):
    if "image" in rel.reltype:
        img_part = rel.target_part
        ext = img_part.content_type.split("/")[-1]
        out_path = f"{out_dir}/img_{i}.{ext}"
        with open(out_path, "wb") as f:
            f.write(img_part.blob)
        print(f"Saved: {out_path}")
```
Then use the `view` tool on each extracted image to read diagrams, charts, or annotated figures.

**Legacy .doc files** — convert first:
```python
# Use the soffice wrapper (bare soffice hangs in this sandbox)
import subprocess
subprocess.run([
    "python3", "/mnt/skills/public/pptx/scripts/office/soffice.py",
    "--convert-to", "docx",
    "--outdir", "/tmp",
    "/mnt/user-data/uploads/old_notes.doc"
], check=True)
# Then read /tmp/old_notes.docx normally
```

---

### 2C — PPTX Files

**Slide text:**
```bash
extract-text /mnt/user-data/uploads/slides.pptx
```
Output format: `## Slide N` headers with all text boxes under each.

**Images embedded in slides (diagrams, charts, photos):**
```python
from pptx import Presentation
from pptx.util import Inches
import os

prs = Presentation("/mnt/user-data/uploads/slides.pptx")
out_dir = "/tmp/pptx_images"
os.makedirs(out_dir, exist_ok=True)

for slide_num, slide in enumerate(prs.slides, 1):
    for shape_num, shape in enumerate(slide.shapes):
        if shape.shape_type == 13:  # MSO_SHAPE_TYPE.PICTURE
            image = shape.image
            ext = image.ext
            out_path = f"{out_dir}/slide{slide_num}_img{shape_num}.{ext}"
            with open(out_path, "wb") as f:
                f.write(image.blob)
            print(f"Saved: {out_path}")
```
Use the `view` tool to visually interpret each image.

**Legacy .ppt files** — convert first (same soffice wrapper as .doc above, `--convert-to pptx`).

---

## Step 3 — Annotate images in context

After extracting images, for each one:

1. Use `view` tool: `view /tmp/pdf_img_p3_0.png`
2. Describe what you see: *"Figure on page 3: Efficient Frontier curve showing risk vs. return trade-off with GMV and Max Sharpe portfolios labelled."*
3. Weave this description into the notes at the correct location (same topic section).

**Do not skip images.** Diagrams in lecture slides and textbook PDFs often contain
key exam content (formulas, decision trees, process flows, labelled graphs).

---

## Step 4 — Build notes aligned to the syllabus

Once all files are read and images annotated:

### Structure rules

- **One section per syllabus unit/topic** — use the syllabus numbering if provided.
- **Within each section:**
  - Key concept definitions (bolded term, one-line definition)
  - Formulas/equations (in code blocks or LaTeX if complex)
  - How-to / step-by-step where applicable
  - Diagrams described with `> 📊 Figure: ...` blockquotes
  - Tables for comparisons
  - Source attribution: `*(Source: slides.pptx, Slide 12)*`

### Syllabus mapping protocol

For each syllabus topic:
1. Search all extracted content for matching keywords.
2. Extract only the relevant passages — do not copy entire pages verbatim.
3. Synthesize into concise notes in your own words, preserving accuracy.
4. If a syllabus topic has **zero coverage** in the provided files, explicitly note:
   `> ⚠️ No source material found for this topic in the provided files.`
   — Never fill gaps by guessing.

### Output format (default)

```markdown
# [Subject Name] — Exam Notes
**Syllabus:** [course code / name]
**Source files:** [list of files used]
**Generated:** [date]

---

## Unit 1: [Title from syllabus]

### [Sub-topic]
**Definition:** ...
**Key formula:** `E(R) = Σ wᵢ × Rᵢ`
**How it works:** ...
> 📊 Figure: [description of diagram from slide/page]
*(Source: lecture_slides.pptx, Slide 4)*

...
```

---

## Step 5 — Output delivery

| User asked for           | What to produce                                      |
|--------------------------|------------------------------------------------------|
| Notes in chat            | Render Markdown directly in conversation             |
| Downloadable `.md` file  | `create_file` → `/mnt/user-data/outputs/notes.md`   |
| Word doc (`.docx`)       | Read `/mnt/skills/public/docx/SKILL.md` first        |
| Flashcards               | See `references/flashcard-format.md`                |
| Cheatsheet (1-2 pages)   | Condense to most testable facts; same output options |

Always state which files were used and which syllabus topics had no matching source material.

---

## Guardrails

- **No hallucination.** If content is not in the files, it does not appear in the notes.
- **No paraphrasing that changes meaning.** Formulas and definitions must be exact.
- **No merging unrelated sources.** Keep attribution per claim when files conflict.
- **Images are mandatory, not optional.** Skipping embedded images risks missing exam content.
- **Scanned PDFs need OCR.** If pdftotext returns empty, do not silently skip — use rasterize + vision or flag to user.

---

## Reference files

- `references/ocr-strategy.md` — How to handle scanned/image-only PDFs
- `references/flashcard-format.md` — Q&A flashcard output format
- `references/soffice-convert.md` — Converting legacy .doc / .ppt files safely
