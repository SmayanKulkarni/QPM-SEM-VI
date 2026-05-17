from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class QPMPaths:
    root: Path = Path(__file__).resolve().parent.parent

    @property
    def curriculum(self) -> Path:
        return self.root / "curriculum"

    @property
    def units(self) -> Path:
        return self.curriculum / "units"

    @property
    def subjects(self) -> Path:
        return self.root / "subjects"

    @property
    def study_materials(self) -> Path:
        return self.root / "study-materials"

    @property
    def generated_notes(self) -> Path:
        return self.study_materials / "generated" / "exam-notes"

    @property
    def flashcards(self) -> Path:
        return self.study_materials / "generated" / "flashcards"

    @property
    def revision_guides(self) -> Path:
        return self.study_materials / "generated" / "revision-guides"

    @property
    def outputs(self) -> Path:
        return self.root / "outputs"

    @property
    def skill_root(self) -> Path:
        return self.root / ".github" / "skills" / "exam-notes-generator"
