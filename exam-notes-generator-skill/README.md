# exam-notes-generator-skill

> Npx-installable AI skill for generating exam-ready LaTeX study notes from course materials (PDF, DOCX, PPTX). Includes diagram extraction, OCR, worked numericals, and complete compilation-ready `.tex` output.

## What This Is

This package scaffolds a **Windsurf / Copilot-compatible agent skill** into any project. The skill turns lecture slides, PDFs, and Word documents into:

- **Complete, compilable LaTeX** (`.tex`) documents with proper preamble, TOC, sectioning, equations, and diagrams
- **Exhaustive study notes** that preserve every concept, formula, and worked example from your sources
- **Diagram extraction & embedding** with semantic filenames and proper figure placement
- **Augmented worked numericals** — every taught method gets at least 3 solved examples (source + agent-constructed)
- **Flashcards & cheatsheets** as alternative outputs

## Quick Start

### One-shot (no install)

```bash
npx exam-notes-generator init
```

This scaffolds the skill into your current directory under `.github/docs/skills/exam-notes-generator/`.

### Install locally (for repeated use)

```bash
npm install -g exam-notes-generator-skill
exam-notes-generator init ./my-course-project
```

## What Gets Installed

```
.github/
  docs/
    copilot-instructions.md          # AI workspace routing rules
    prompts/
      exam-notes.prompt.md           # Slash-prompt template
    skills/
      exam-notes-generator/
        SKILL.md                      # Full skill specification (~1000 lines)
        references/
          flashcard-format.md         # Q&A card output format
          ocr-strategy.md             # Scanned PDF handling
          soffice-convert.md          # Legacy .doc/.ppt conversion
  reference-notes/
    (placeholder for reference .tex examples)
```

## Skill Workflow (After Install)

1. **Place your course materials** in the project (e.g., `subjects/ML 3/Module 1/`, `UNIT 1/`)
2. **Ask your AI assistant**:
   - *"Make complete study notes from subjects/ML 3/"*
   - *"Generate exam notes for UNIT 1 and UNIT 2"*
   - *"Create flashcards from these slides"*
3. **The skill automatically**:
   - Inventories all source files
   - Extracts text, tables, and embedded images
   - Rasterizes every page and runs OCR
   - Classifies diagrams (architecture, flowcharts, plots, etc.)
   - Builds a numerical inventory and augments with extra examples
   - Produces a production-ready `.tex` file in `/outputs/latex/`

## Key Design Principles

| Principle | Enforcement |
|---|---|
| **Grounded only** | Every fact must trace to a specific source file |
| **LaTeX-first** | Output is compilable `.tex`, not markdown-in-disguise |
| **Diagrams are content** | Every significant figure is extracted, OCR'd, renamed semantically, and embedded |
| **No compression** | Source bullet hierarchy, sub-points, and caveats are preserved |
| **Numericals mandatory** | Every method gets ≥3 worked examples (source + constructed) |
| **Semantic placement** | Diagrams live in the same section as the theory they illustrate |

## Example Invocation

After installing the skill into a project, trigger it via:

```
/exam-notes sourcePath=subjects/QPM/ outputType=notes depth=detailed
```

Or simply ask your AI:

> "Generate complete study-source LaTeX for all units in this workspace."

## Requirements

- Node.js >= 18 (for the CLI scaffold tool)
- The AI skill itself runs inside your agent environment (Windsurf, Copilot, etc.)
- Optional but recommended for full functionality: `pymupdf`, `pdfplumber`, `python-pptx`, `python-docx`, `tesseract`

## License

MIT
