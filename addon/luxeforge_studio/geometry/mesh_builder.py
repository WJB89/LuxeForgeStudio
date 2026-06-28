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

        # Verwijder oud object
        existing = bpy.data.objects.get(name)

        if existing:
            bpy.data.objects.remove(existing, do_unlink=True)

        # Maak mesh
        mesh = bpy.data.meshes.new(name)
        mesh.from_pydata(vertices, [], faces)
        mesh.update()

        obj = bpy.data.objects.new(name, mesh)

        # Link aan actieve collectie
        bpy.context.collection.objects.link(obj)

        # Selecteer object
        bpy.ops.object.select_all(action="DESELECT")

        obj.select_set(True)

        bpy.context.view_layer.objects.active = obj

        return obj