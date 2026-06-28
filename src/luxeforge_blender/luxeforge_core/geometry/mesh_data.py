"""
LuxeForge Studio

Mesh Data
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class MeshData:
    """
    Represents generated mesh data.

    This class is Blender independent.
    """

    vertices: list[tuple[float, float, float]] = field(default_factory=list)

    faces: list[tuple[int, ...]] = field(default_factory=list)