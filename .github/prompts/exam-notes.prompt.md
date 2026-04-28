---
mode: agent
description: Generate exam notes, flashcards, or a cheatsheet from syllabus or unit folders using the exam-notes-generator skill.
---

# Exam Notes Workflow

Use the skill in .github/skills/exam-notes-generator/SKILL.md.

Goal:
- Convert source materials into accurate study outputs grounded only in provided files.

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

Output:
- Return structured markdown in chat and offer to save a file in outputs/ when requested.
