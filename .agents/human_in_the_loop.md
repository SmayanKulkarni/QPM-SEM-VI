# Human In The Loop

## 2026-04-28
- User requested two enhancements:
  1. Add a matching prompt command for fixed slash flow.
  2. Add workspace instructions to strongly bias auto-use of the exam-notes skill.
- Both requested enhancements were implemented.
- User requested exhaustive markdown exam notes for Term Test II syllabus topics (Units 4-6) using workspace sources and all images/docs.
- Completed with full topic coverage and source-attributed notes file generation.
- User requested deeper textbook-style explanations, more solved numericals by type, and embedding of images directly in the study document.
- Implemented by generating a complete-study version with expanded explanations and embedded figure appendix.
- User requested a LaTeX version because equations were not rendering professionally in markdown.
- Implemented with a .tex output and dedicated display-math equation compendium.
- User confirmed and requested PDF compilation of the LaTeX output.
- PDF compilation completed successfully after fixing special-character image path issues.

## 2026-05-01
- User asked to work on the SKILL package and MCP server.
- Implemented a first packaging pass with a shared Python package, CLI entrypoints, and an MCP server scaffold.
- Updated the SKILL contract to reference the shared package as the source of truth.
- Expanded the package so the CLI and MCP server can run the existing extraction/build/compile workflow, not just describe it.
- Verified the packaged extraction command after repo reorganization and repaired the old hardcoded source paths.
- Verified the build command after moving the figure appendix.
- Verified the compile command end to end with the sanitized figure assets from the previous pipeline.
- User requested SKILL-only sharing; docs updated to remove MCP/CLI and release guidance, and added HOW_TO_USE.md.
- User requested MCP/CLI code removal; removed CLI/runtime modules, MCP server module, and packaging entrypoints/dependency.
- User requested deleting the leftover MCP folder; removed integrations/mcp_server.
- User requested removing personal materials; archived and removed them, restored empty template folders, and rewrote README for SKILL-only usage.
- User requested a GitHub quick start and sample folder layout; added both to README.md.
- User requested OS-agnostic support; updated HOW_TO_USE.md and README.md to state Windows/macOS/Linux usage.
- User requested exhaustive LaTeX-ready study-source output; updated .github instructions to force full-source inventory, OCR/image review, and completeness checks.
- User requested OCR on every page of every document, including handwritten and screenshot-style pages; updated .github instructions accordingly.

## 2026-05-02
- User asked to generate notes from the attached subjects/CV folder.
- I extracted the Module 4, 5, and 6 slide/PDF content into a markdown study file and kept the structure module-based.
- I preserved source attribution and noted that the scanned Module 4 PDFs were OCR-checked but noisy.
