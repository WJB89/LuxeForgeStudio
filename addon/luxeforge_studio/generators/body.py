"""
LuxeForge Studio

Body Generator
"""

from __future__ import annotations

from ..geometry.path import Path
from ..geometry.extruder import Extruder
from ..geometry.mesh_builder import MeshBuilder

from ..models.bag_parameters import BagParameters


class BodyGenerator:
    """
    Generates the procedural handbag body.
    """

    def generate(self, params: BagParameters):

        w = params.width / 2
        h = params.height

        path = (
            Path()
            .move_to(-w, 0)
            .line_to(-w, h)
            .line_to(w, h)
            .line_to(w, 0)
            .close()
        )

        vertices, faces = Extruder().extrude(
            path,
            params.depth,
        )

        obj = MeshBuilder.create_mesh(
            "LFS_Bag",
            vertices,
            faces,
        )

        return obj