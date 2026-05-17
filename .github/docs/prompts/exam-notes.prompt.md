---
mode: agent
description: Generate exam notes, flashcards, or a cheatsheet from syllabus or unit folders using the exam-notes-generator skill.
---

# Exam Notes Workflow

Use the skill in .github/docs/skills/exam-notes-generator/SKILL.md.

Goal:
- Convert source materials into accurate study outputs grounded only in provided files.
- For complete study-source requests, produce exhaustive notes in **complete, compilable LaTeX format**.
- Generate actual `.tex` files (not markdown), with proper document structure, sectioning, itemization, equations, and figure blocks.

Inputs:
- Source path or files: ${input:sourcePath:Workspace folder or file list to process}
- Syllabus path (optional): ${input:syllabusPath:Optional syllabus file path}
- Output type: ${input:outputType:notes | flashcards | cheatsheet}
- Depth: ${input:depth:quick | detailed}

Execution requirements:
- Read only the specified materials and include source attribution in outputs.
- If a syllabus is provided, organize strictly by syllabus units/topics.
- For missing-topic coverage, report gaps instead of guessing.
- For scanned PDFs or image-heavy pages, follow the OCR/image strategy from the skill references.
- Make a completeness pass before finishing: every unit, slide, page, diagram, equation, table, worked example, definition, and conceptual note in the provided sources must either appear in the output or be explicitly listed as uncovered.
- OCR every PDF page and inspect every slide/page image, including handwritten pages, screenshots, diagrams, and annotations, rather than relying on the text layer alone.
- When a source contains diagrams or figures, include them in the LaTeX output as `\begin{figure}` blocks.
- Preserve source bullet structure and detail. Do not collapse nested bullets, examples, warnings, steps, or qualifiers into a shorter summary if that would drop information.
- If a source bullet list is long, preserve the full itemized structure in the notes unless doing so would duplicate an identical point already covered elsewhere.

Output:
- **Generate a complete `.tex` file**, not markdown.
- Structure must include: `\documentclass`, full preamble with packages, `\maketitle`, `\tableofcontents`, `\section`, `\subsection` with proper nesting, `\begin{itemize}` / `\begin{enumerate}` for lists, `tcolorbox` for key concepts and worked numericals, `\begin{figure}[H]` for diagrams with captions.
- **Reference example:** See `.github/reference-notes/cv-modules-4-6/cv-modules-4-6-complete-study-source.tex` in the repository for quality standard and formatting examples.
- Include figure files in `/outputs/figures/` directory, referenced via `\includegraphics{figures/...}`.
- Save the `.tex` file to `/outputs/latex/[subject]-[module-range]-complete-study-source.tex`.
- The file must compile directly with `pdflatex` or `xelatex` without modification.
- Optionally compile to PDF and preview, or provide compilation instructions.
- If a study-source request is made, the output should be **exhaustive**, not compressed — every concept, formula, diagram, and worked example from the sources must be included with full detail and hierarchy.
