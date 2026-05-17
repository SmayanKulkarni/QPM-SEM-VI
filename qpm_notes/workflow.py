from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .paths import QPMPaths


@dataclass(frozen=True)
class NoteGenerationRequest:
    source_path: str
    syllabus_path: str | None = None
    output_type: str = "notes"
    depth: str = "detailed"


def _path_info(path: Path) -> dict[str, Any]:
    return {
        "path": str(path),
        "exists": path.exists(),
        "is_dir": path.is_dir(),
        "is_file": path.is_file(),
    }


def list_source_collections() -> list[dict[str, Any]]:
    paths = QPMPaths()
    unit_dirs = [p for p in sorted(paths.units.iterdir()) if p.is_dir()] if paths.units.exists() else []
    subject_dirs = [p for p in sorted(paths.subjects.iterdir()) if p.is_dir()] if paths.subjects.exists() else []

    return [
        {
            "name": "curriculum",
            "kind": "course_materials",
            "root": _path_info(paths.curriculum),
            "units": [_path_info(p) for p in unit_dirs],
        },
        {
            "name": "subjects",
            "kind": "subject_materials",
            "root": _path_info(paths.subjects),
            "subjects": [_path_info(p) for p in subject_dirs],
        },
        {
            "name": "study-materials",
            "kind": "generated_outputs",
            "root": _path_info(paths.study_materials),
            "generated_notes": _path_info(paths.generated_notes),
            "flashcards": _path_info(paths.flashcards),
            "revision_guides": _path_info(paths.revision_guides),
        },
    ]


def package_contract() -> dict[str, Any]:
    paths = QPMPaths()
    return {
        "package": {
            "name": "qpm-notes",
            "version": "0.1.0",
            "primary_surface": "SKILL",
        },
        "skill": {
            "root": str(paths.skill_root),
            "entry": ".github/docs/skills/exam-notes-generator/SKILL.md",
            "prompt": ".github/docs/prompts/exam-notes.prompt.md",
        },
        "source_roots": list_source_collections(),
        "outputs": {
            "notes": str(paths.generated_notes),
            "flashcards": str(paths.flashcards),
            "revision_guides": str(paths.revision_guides),
            "compiled": str(paths.outputs / "compiled"),
            "latex": str(paths.outputs / "latex"),
        },
        "grounding_rule": "Every generated fact must trace back to a source file or source page/slide.",
    }


def describe_package() -> dict[str, Any]:
    contract = package_contract()
    contract["workflow"] = {
        "note_generation_request": asdict(
            NoteGenerationRequest(source_path="<required>")
        ),
        "supported_outputs": ["notes", "flashcards", "cheatsheet"],
        "supported_sources": ["pdf", "docx", "doc", "pptx", "ppt"],
    }
    return contract


def build_note_generation_plan(
    source_path: str,
    syllabus_path: str | None = None,
    output_type: str = "notes",
    depth: str = "detailed",
) -> dict[str, Any]:
    source = Path(source_path).expanduser().resolve()
    syllabus = Path(syllabus_path).expanduser().resolve() if syllabus_path else None
    paths = QPMPaths()

    likely_surface = "general"
    if paths.units in source.parents or source == paths.units:
        likely_surface = "curriculum"
    elif paths.subjects in source.parents or source == paths.subjects:
        likely_surface = "subject"
    elif paths.skill_root in source.parents or source == paths.skill_root:
        likely_surface = "skill_bundle"

    recommended_steps = [
        "Collect source files and image assets",
        "Apply OCR and structural extraction",
        "Assemble grounded markdown notes",
        "Optionally compile to LaTeX or PDF",
    ]
    if output_type == "flashcards":
        recommended_steps[2] = "Convert facts into Q&A cards with source tags"
    elif output_type == "cheatsheet":
        recommended_steps[2] = "Condense to the most testable facts"

    return {
        "request": {
            "source_path": str(source),
            "syllabus_path": str(syllabus) if syllabus else None,
            "output_type": output_type,
            "depth": depth,
        },
        "source_context": likely_surface,
        "recommended_steps": recommended_steps,
        "delivery_targets": {
            "notes": str(paths.generated_notes),
            "flashcards": str(paths.flashcards),
            "revision_guides": str(paths.revision_guides),
        },
    }
