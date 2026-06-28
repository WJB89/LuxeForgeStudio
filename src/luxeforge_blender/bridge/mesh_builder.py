"""
LuxeForge Studio

Mesh Builder

Converts MeshData into a Blender mesh.
"""

from __future__ import annotations

import bpy

from ..luxeforge_core.geometry.mesh_data import MeshData


class MeshBuilder:
    """
    Creates Blender mesh objects from MeshData.
    """

    @staticmethod
    def create_mesh(
        name: str,
        mesh_data: MeshData,
    ) -> bpy.types.Object:
        """
        Creates a Blender object from MeshData.
        """

        mesh = bpy.data.meshes.new(name)

        mesh.from_pydata(
            mesh_data.vertices,
            [],
            mesh_data.faces,
        )

        mesh.update()

        obj = bpy.data.objects.new(
            name,
            mesh,
        )

        bpy.context.collection.objects.link(obj)

        bpy.context.view_layer.objects.active = obj

        obj.select_set(True)

        return obj