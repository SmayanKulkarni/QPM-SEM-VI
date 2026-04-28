# Copilot Workspace Instructions

## Skill Routing Priority

When the user asks for notes, revision material, flashcards, cheatsheets, or exam prep from any syllabus/unit/course files, use the skill at .github/skills/exam-notes-generator/SKILL.md.

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

- Keep all factual content grounded in provided files only.
- Include per-claim attribution where practical (file + page/slide/section).
- If a requested topic is not present in sources, explicitly report missing coverage.
- Do not invent formulas, definitions, or examples not present in source material.

## Preferred Command

For consistent invocation, use the slash prompt command based on .github/prompts/exam-notes.prompt.md.
