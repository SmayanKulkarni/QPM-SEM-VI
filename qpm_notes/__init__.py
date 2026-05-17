"""QPM note-generation package."""

from .workflow import (
    build_note_generation_plan,
    describe_package,
    list_source_collections,
    package_contract,
)

__all__ = [
    "build_note_generation_plan",
    "describe_package",
    "list_source_collections",
    "package_contract",
]
