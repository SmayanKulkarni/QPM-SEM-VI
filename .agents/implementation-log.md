# Implementation Log

## 2026-04-28
- Created Copilot prompt command at .github/docs/prompts/exam-notes.prompt.md.
- Created workspace routing instructions at .github/copilot-instructions.md.
- Wired requests for notes/flashcards/cheatsheets to .github/docs/skills/exam-notes-generator/SKILL.md.
- Executed exhaustive Unit 4-6 source ingestion (PPTX, PDF, DOCX, legacy PPT OCR) for Term Test II notes.
- Installed OCR dependency (tesseract) and re-ran extraction to include image-based content.
- Generated final markdown notes file at outputs/term-test-ii-units-4-6-exam-notes.md with citations and image coverage log.
- Generated full-length study-source document with deep explanations and expanded source-based numericals at outputs/term-test-ii-units-4-6-complete-study-source.md.
- Embedded all extracted figures (126 images) directly into the study document via markdown image links.
- Generated LaTeX counterpart at outputs/term-test-ii-units-4-6-complete-study-source.tex using pandoc.
- Added a professionally typeset equation compendium section in the LaTeX file for clean formula rendering.
- Compiled LaTeX to PDF at outputs/term-test-ii-units-4-6-complete-study-source.pdf.
- Sanitized problematic image filename references by remapping figures to outputs/figures/fig_XXXX.* for LaTeX compatibility.

## 2026-05-01
- Added a shared Python package surface at qpm_notes with CLI entrypoints for describe, sources, commands, and plan.
- Added an MCP server scaffold at integrations/mcp_server/server.py using FastMCP and the shared package contract.
- Tightened .github/docs/skills/exam-notes-generator/SKILL.md so the shared package contract is the source of truth for SKILL and MCP surfaces.
- Added a repository packaging manifest at pyproject.toml for editable installs and console scripts.
- Added workflow execution helpers in qpm_notes/runtime.py and exposed extraction/build/compile/status actions through both the CLI and MCP server.
- Fixed the extraction target paths after repo reorganization so the packaged workflow can process curriculum/units/UNIT 4-6 again.
- Fixed the build step to read the figure appendix from docs/resources and compile the study source.
- Fixed the compiler wrapper to use the sanitized figure assets from outputs/compiled/figures and validated PDF generation end to end.
- Simplified documentation to SKILL-only usage, added HOW_TO_USE.md, and removed MCP/CLI and release docs.
- Removed MCP/CLI code paths: deleted qpm_notes CLI/runtime, removed MCP server module, and stripped MCP dependencies/scripts from pyproject.
- Deleted the empty integrations/mcp_server folder after removing MCP code.
- Archived personal content to /home/smayan/Desktop/QPM-personal-backup-2026-05-01.zip and removed personal materials from the repo.
- Recreated empty template folders with .gitkeep placeholders for curriculum, subjects, study-materials, and outputs.
- Rewrote README.md to a simple step-by-step SKILL-only usage guide.
- Added a GitHub quick start section and an example folder layout to README.md.
- Clarified OS-agnostic usage in HOW_TO_USE.md and README.md.
- Tightened the .github skill contract for exhaustive study-source generation: full file inventory, OCR/image inspection, completeness checklist, and no-loose-ends requirement.
- Added mandatory OCR/raster inspection for every PDF page and every slide/page image, including handwritten and screenshot-style content.

## 2026-05-02
- Generated a new CV study notes file at study-materials/generated/exam-notes/cv-modules-4-6-exam-notes.md from the M4, M5, and M6 source decks.
- Added module-organized notes with GANs, segmentation, video understanding, motion analysis, optical flow, and stereo depth coverage.
- Recorded source attribution and a coverage note for the OCR-checked Module 4 PDFs.
