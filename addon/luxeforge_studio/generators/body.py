"""
LuxeForge Studio

Body generator.
"""

from __future__ import annotations

from ..geometry.mesh_builder import MeshBuilder
from ..models.bag_parameters import BagParameters


class BodyGenerator:
    """Generates the basic bag body."""

    def generate(self, params: BagParameters):

        w = params.width / 2
        d = params.depth / 2
        h = params.height

        vertices = [

            (-w, -d, 0),
            ( w, -d, 0),
            ( w,  d, 0),
            (-w,  d, 0),

            (-w, -d, h),
            ( w, -d, h),
            ( w,  d, h),
            (-w,  d, h),

        ]

        faces = [

            (0, 1, 2, 3),
            (4, 5, 6, 7),

            (0, 1, 5, 4),
            (1, 2, 6, 5),
            (2, 3, 7, 6),
            (3, 0, 4, 7),

        ]

        return MeshBuilder.create_mesh(
            "LFS_Bag",
            vertices,
            faces,
        )