# Copilot Study Notes Generator

A production-ready GitHub Copilot skill for generating **professional-grade LaTeX study notes** from your course materials (PDFs, slides, documents).

Generate exhaustive, well-formatted study guides, revision materials, and LaTeX documents from any lecture content. No setup hassles — just clone, add your files, and ask Copilot.

---

## Prerequisites

Before you start, you'll need:

1. **GitHub Copilot subscription** — [Sign up or check eligibility](https://github.com/copilot)
2. **Visual Studio Code** — [Download here](https://code.visualstudio.com/)
3. **Copilot extension for VS Code** — Install from the Extensions Marketplace
4. **LaTeX distribution** (for compiling generated `.tex` files into PDFs):
   - **macOS:** `brew install texlive`
   - **Ubuntu/Debian:** `sudo apt-get install texlive-latex-full`
   - **Windows:** [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

> **Note:** You can generate `.tex` files without LaTeX installed; LaTeX is only needed if you want to compile them to PDF.

---

## Installation

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/[your-username]/QPM.git
cd QPM

# Or use "Use this template" on GitHub to create your own version
```

### 2. Open in VS Code

```bash
code .
```

### 3. Enable Copilot

- Make sure the GitHub Copilot extension is installed and active
- Sign in with your GitHub account
- Accept the terms of service

### 4. Verify the Skill is Loaded

- Open any markdown file (e.g., `README.md`)
- Ask Copilot: "what skills are available?"
- You should see the `exam-notes-generator` skill listed

---

## Quick Start (5 minutes)

### Step 1: Add Your Course Materials

Place your study files into the source folders:

```
QPM/
├── UNIT 1/
│   ├── Lecture slides.pptx
│   └── Chapter 1.pdf
├── UNIT 2/
│   ├── Module 2 notes.pdf
│   └── Slides.pptx
└── subjects/
    └── Computer Vision/
        ├── M1.pptx
        ├── M2.pptx
        └── ...
```

Supported formats: **PDF, PPTX, PPT, DOCX, DOC**

### Step 2: Ask Copilot to Generate Notes

Open any file and ask Copilot in the chat:

```
make notes from UNIT 1

// Or for more control:
generate study notes from subjects/Computer Vision/M1.pptx
generate notes from UNIT 2, UNIT 3, UNIT 4
prepare exam revision from all subjects
```

### Step 3: Get Your LaTeX Notes

Copilot will generate complete, compilable LaTeX documents in:

```
outputs/latex/
├── unit-1-complete-study-source.tex
├── unit-2-complete-study-source.tex
└── ...
```

Each `.tex` file includes:
- Full LaTeX document structure (`\documentclass`, preamble, sections, etc.)
- Exhaustive content from your source materials (no compression)
- Formatted equations, diagrams, and figures
- Colored callout boxes for key concepts and worked examples
- Proper sectioning and nested lists preserving source hierarchy

### Step 4: Compile to PDF (Optional)

```bash
cd outputs/latex
pdflatex unit-1-complete-study-source.tex

# Or use your LaTeX editor (Overleaf, TeXShop, etc.)
```

The result: A professional, ready-to-study PDF with full source attribution.

---

## Output Format: LaTeX

All generated notes are **production-ready LaTeX documents**. This means:

✅ **Complete compilation** — File compiles directly with `pdflatex` or `xelatex` without modification  
✅ **Full preamble** — All required packages included (amsmath, graphicx, tcolorbox, hyperref, etc.)  
✅ **Rich formatting** — Sections, subsections, nested lists, equations, figures with captions  
✅ **Key concept boxes** — Colored `tcolorbox` callouts for important definitions and worked examples  
✅ **No information loss** — Exhaustive source material preservation (no bullet compression)  
✅ **Professional appearance** — Ready for study, revision, or sharing  

---

## Quality Standard

See the reference example at `.github/reference-notes/cv-modules-4-6/cv-modules-4-6-complete-study-source.tex` to understand the quality standard:

- 468 lines of structured LaTeX
- 15 pages of complete, professional notes
- 26 supporting diagrams and figures
- Full module coverage (GANs, Segmentation, Video Understanding)
- Styled callout boxes, nested lists, and formatted equations

**All generated notes will match this quality level.**

---

## Example Copilot Commands

### Basic Notes
```
make notes from UNIT 1
```

### Multiple sources
```
generate study notes from UNIT 4, UNIT 5, UNIT 6
create exam revision from subjects/Computer Vision/
```

### Specific file
```
make notes from UNIT 1/Lecture slides.pptx
```

### From PDF + images
```
prepare study material from subjects/Math/Calculus textbook.pdf
```

---

## Where Your Files End Up

After generation, check these folders:

**LaTeX output:** `outputs/latex/`
- `.tex` files (compilable source)
- Intermediate files (`.aux`, `.log`, `.toc`)

**Figures:** `outputs/figures/`
- Images referenced in the `.tex` files
- Automatically linked from the LaTeX document

---

## Customization

### Modify the Skill

To change how notes are generated, edit:
```
.github/docs/skills/exam-notes-generator/SKILL.md
```

Examples:
- Add new output formats
- Change the LaTeX template
- Modify extraction rules for specific file types

### Adjust Copilot Instructions

To change when the skill is triggered, edit:
```
.github/docs/copilot-instructions.md
```

Example:
- Add new trigger phrases like "summarize this course"
- Change which folders are auto-detected

---

## Troubleshooting

### "Copilot skill not found"
- Ensure `.github/docs/skills/exam-notes-generator/SKILL.md` exists
- Reload VS Code (`Cmd/Ctrl + Shift + P` → "Reload Window")
- Check that Copilot extension is enabled

### "Input files not found"
- Make sure files are in `UNIT X/`, `subjects/`, or their subdirectories
- Supported formats: PDF, PPTX, DOCX (check file extensions)
- Try a full file path: `make notes from ./UNIT 1/slides.pptx`

### "LaTeX compilation fails"
- Ensure a LaTeX distribution is installed (see Prerequisites)
- Check for missing figure files in `outputs/figures/`
- Review the `.log` file for specific errors

### "Output looks compressed/incomplete"
- The skill is designed to preserve all source detail — this is intentional
- Check `.tex` file size (should be proportional to source material)
- See `.github/docs/reference-notes-README.md` for quality guidelines

---

## Documentation

- **[HOW_TO_USE.md](HOW_TO_USE.md)** — One-page quick reference
- **[GETTING_STARTED.md](GETTING_STARTED.md)** — Detailed setup guide
- **[NOTES-QUALITY-STANDARD.md](NOTES-QUALITY-STANDARD.md)** — Output format and quality requirements
- **[docs/WORKFLOWS.md](docs/WORKFLOWS.md)** — Technical workflow documentation
- **[REPO-SETUP.md](REPO-SETUP.md)** — Repository structure and path information
- **[.github/docs/](.github/docs/)** — Skill implementation and configuration files
- **[.github/reference-notes/](.github/reference-notes/)** — Example reference notes (CV Modules 4-6)

---

## How It Works

1. **You provide:** Course materials (PDFs, slides, documents)
2. **Copilot reads:** Every page, slide, image, and table
3. **Copilot generates:** LaTeX document with:
   - Complete preamble and document structure
   - All content organized by section
   - Equations, figures, and diagrams formatted
   - Key concepts highlighted in colored boxes
   - Full source attribution
4. **You get:** A professional, compilable `.tex` file ready for study or sharing

---

## Features

✨ **Automated extraction** — Reads slides, PDFs, documents automatically  
✨ **No information loss** — Preserves all source detail and hierarchy  
✨ **OCR-ready** — Handles scanned PDFs and image-heavy materials  
✨ **Rich formatting** — LaTeX equations, nested lists, colored callouts  
✨ **Professional output** — Publication-ready study documents  
✨ **Portable** — Works on Windows, macOS, Linux  
✨ **Zero setup** — No CLI, servers, or dependencies (except LaTeX for compilation)  
✨ **Extensible** — Easy to modify the skill for your workflow  

---

## For Developers

This repository uses GitHub Copilot Skills to define the note generation workflow.

**Key files:**
- `.github/docs/skills/exam-notes-generator/SKILL.md` — Skill definition
- `.github/docs/prompts/exam-notes.prompt.md` — Workflow prompt
- `.github/docs/copilot-instructions.md` — Routing and policies

To fork and customize:
1. Clone the repository
2. Modify the SKILL.md file
3. Test with your own course materials
4. Push your version

---

## License

This repository is provided as-is for personal and educational use. See LICENSE for details.

---

## Need Help?

- Check [HOW_TO_USE.md](HOW_TO_USE.md) for common questions
- Review [GETTING_STARTED.md](GETTING_STARTED.md) for detailed setup
- See [docs/WORKFLOWS.md](docs/WORKFLOWS.md) for technical details
- Ask Copilot directly in the chat for clarification
