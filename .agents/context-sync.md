# Context Sync

## 2026-04-28
- Active skill bundle: .github/docs/skills/exam-notes-generator/.
- New prompt command: .github/docs/prompts/exam-notes.prompt.md.
- New workspace instructions: .github/copilot-instructions.md.
- Source utility assets remain in files/; runtime-discoverable assets are in .github/.
- Extraction artifacts generated:
	- extracted/unit456_extraction.json
	- extracted/unit456_extraction.md
	- extracted/unit456_digest.md
- Final notes generated:
	- outputs/term-test-ii-units-4-6-exam-notes.md
- New deep-study artifacts generated:
	- extracted/figure_appendix.md
	- extracted/build_complete_study_source.py
	- outputs/term-test-ii-units-4-6-complete-study-source.md
- Additional output generated:
	- outputs/term-test-ii-units-4-6-complete-study-source.tex
- Final compiled deliverables:
	- outputs/term-test-ii-units-4-6-complete-study-source.pdf
	- outputs/figures/ (sanitized image assets used by LaTeX compile)

## 2026-05-01
- Shared package surface added: qpm_notes.
- CLI entrypoints added: qpm-notes, qpm-notes-mcp.
- MCP server scaffold added under integrations/mcp_server/.
- SKILL file now treats qpm_notes.workflow as the canonical contract for both SKILL and MCP surfaces.
- Workflow execution helpers now expose the existing extraction, study-source build, and LaTeX compilation steps through the package contract.
- The current packaged workflow supports the reorganized curriculum layout and can regenerate the Units 4-6 extraction, build source, and compiled PDF.
- Documentation now emphasizes SKILL-only usage; HOW_TO_USE.md added; MCP/CLI and release docs removed.
- MCP/CLI code removed: qpm_notes CLI/runtime deleted, MCP server module deleted, and pyproject scripts/dependencies cleaned.
- MCP server folder removed: integrations/mcp_server deleted.
- Personal materials archived to /home/smayan/Desktop/QPM-personal-backup-2026-05-01.zip and removed from repo.
- Template folders restored with .gitkeep placeholders under curriculum/, subjects/, study-materials/, and outputs/.
- README.md now provides a step-by-step SKILL-only usage guide.
- README.md now includes a GitHub quick start section and example folder layout.
- HOW_TO_USE.md and README.md now explicitly state Windows/macOS/Linux support.
- .github instructions now require exhaustive study-source coverage, OCR/image inspection, and a final completeness audit before answering.
- .github instructions now require OCR on every PDF page and inspection of every slide/page image, including handwritten and screenshot-style content.

## 2026-05-02
- Generated a CV notes deliverable at study-materials/generated/exam-notes/cv-modules-4-6-exam-notes.md.
- Source coverage used the attached subjects/CV/M4, M5, and M6 folders.
- The notes include a coverage note that the Module 4 PDFs were OCR-checked page by page and were partially garbled.
