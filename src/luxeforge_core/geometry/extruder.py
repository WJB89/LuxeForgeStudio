"""
LuxeForge Studio

Profile Extruder
"""
from luxeforge_core.geometry.mesh_data import MeshData

from __future__ import annotations

from .path import Path


class Extruder:
    """
    Extrudes a 2D path into vertices and faces.
    """

    def extrude(self, path: Path, depth: float):

        if len(path.points) < 3:
            raise ValueError("Path requires at least three points.")

        half_depth = depth / 2

        vertices = []

        #
        # Front face
        #
        for point in path.points:
            vertices.append(
                (
                    point.x,
                    -half_depth,
                    point.y,
                )
            )

        #
        # Back face
        #
        for point in path.points:
            vertices.append(
                (
                    point.x,
                    half_depth,
                    point.y,
                )
            )

        count = len(path.points)

        faces = []

        #
        # Front face
        #
        faces.append(tuple(range(count)))

        #
        # Back face
        #
        faces.append(tuple(range(count, count * 2)))

        #
        # Side faces
        #
        for i in range(count):

            j = (i + 1) % count

            faces.append(
                (
                    i,
                    j,
                    j + count,
                    i + count,
                )
            )

        return MeshData(
    vertices=vertices,
    faces=faces,
)