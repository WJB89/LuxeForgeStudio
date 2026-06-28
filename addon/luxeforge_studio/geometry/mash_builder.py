"""
LuxeForge Studio

Mesh Builder
"""

from __future__ import annotations

import bpy


class MeshBuilder:

    @staticmethod
    def create_mesh(
        name: str,
        vertices: list,
        faces: list,
    ) -> bpy.types.Object:

        mesh = bpy.data.meshes.new(name)

        mesh.from_pydata(vertices, [], faces)

        mesh.update()

        obj = bpy.data.objects.new(name, mesh)

        bpy.context.collection.objects.link(obj)

        return obj