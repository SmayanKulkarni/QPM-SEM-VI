# Copilot Workspace Instructions

## Skill Routing Priority

When the user asks for notes, revision material, flashcards, cheatsheets, or exam prep from any syllabus/unit/course files, use the skill at .github/docs/skills/exam-notes-generator/SKILL.md.

If the user asks for a complete study source, exhaustive notes, or a LaTeX-ready document, route to the same skill and require a full coverage pass over every provided file.

For any notes request, treat LaTeX as the default output format: produce LaTeX-first structure with sectioning, itemize/enumerate lists, equations, and figure callouts, even if the file is saved as markdown for convenience.

## Trigger Phrases

Strongly prefer the exam-notes-generator skill when requests include phrases such as:
- make notes
- create notes
- study notes
- exam notes
- summarize lecture
- notes from slides
- notes from pdf
- prepare for exam
- revise topic
- make a cheatsheet
- flashcards from these files

## Scope Detection

Auto-detect relevant source content from these workspace areas unless the user specifies a narrower set:
- UNIT 1/
- UNIT 2/
- UNIT 3/
- UNIT 4/
- UNIT 5/
- UNIT 6/
- any syllabus PDF in the workspace root

## Output Policy

### Format Requirements
- **ALL notes output must be complete `.tex` (LaTeX) documents**, not markdown or markdown-in-disguise.
- The output `.tex` file must include:
  - Full preamble: `\documentclass{article}` with required packages (amsmath, amssymb, graphicx, hyperref, tcolorbox, enumitem, etc.)
  - `\tableofcontents` with proper sectioning
  - `\section`, `\subsection` hierarchy matching source depth
  - Proper `\begin{itemize}` / `\begin{enumerate}` with nested lists where source material uses nesting
  - Text emphasis: `\textbf{}` for key terms, `\textit{}` where appropriate
  - Equations in proper LaTeX environments (`\[ \]` or `\begin{equation}`)
  - `tcolorbox` environments for key concept callouts, important formulas, and worked numericals
  - `\begin{figure}[H]` blocks with `\includegraphics` and `\caption{}` for all diagrams
  - Proper spacing and formatting (e.g., `\setlist` for consistent list spacing)
- The file is production-ready and can be compiled directly with `pdflatex` or `xelatex` without modification.
- Store output as `.tex` file in `/outputs/latex/` with corresponding figures in `/outputs/figures/`.
- **Reference example:** See `.github/reference-notes/cv-modules-4-6/cv-modules-4-6-complete-study-source.tex` for the quality standard and formatting style to match.

### Content Requirements
- Keep all factual content grounded in provided files only.
- Include per-claim attribution where practical (file + page/slide/section).
- If a requested topic is not present in sources, explicitly report missing coverage.
- Do not invent formulas, definitions, or examples not present in source material.
- For study-source requests, require exhaustive coverage: every theory concept, every mathematical concept, every diagram, and every explicit example visible in the sources must be mentioned in the notes or called out as missing.
- For study-source requests, OCR every PDF page and inspect every slide/page image, including handwritten pages and screenshot-style content, rather than trusting the text layer alone.
- If the source set is incomplete for an exhaustive output, state the gap clearly instead of silently skipping it.
- **Do NOT compress source bullet lists.** Preserve the original bullet depth, sub-points, caveats, examples, step ordering, and qualifiers in the notes. If the source uses nested bullets or sub-bullets, keep that hierarchy in the output.

## Preferred Command

For consistent invocation, use the slash prompt command based on .github/docs/prompts/exam-notes.prompt.md.
