"""
LuxeForge Studio

Mesh Builder
"""

from __future__ import annotations

import bpy

from ..luxeforge_core.geometry.mesh_data import MeshData


class MeshBuilder:
    """
    Converts MeshData into a Blender object.
    """

    @staticmethod
    def create_mesh(
        name: str,
        mesh_data: MeshData,
    ) -> bpy.types.Object:

        #
        # Create mesh datablock
        #

        mesh = bpy.data.meshes.new(name)

        mesh.from_pydata(
            mesh_data.vertices,
            [],
            mesh_data.faces,
        )

        mesh.update()

        #
        # Create object
        #

        obj = bpy.data.objects.new(
            name,
            mesh,
        )

        bpy.context.collection.objects.link(obj)

        #
        # Make active
        #

        bpy.ops.object.select_all(action="DESELECT")

        obj.select_set(True)

        bpy.context.view_layer.objects.active = obj

        #
        # Smooth shading
        #

        try:

            mesh.shade_smooth()

        except AttributeError:

            for polygon in mesh.polygons:
                polygon.use_smooth = True

        #
        # Bevel modifier
        #

        bevel = obj.modifiers.new(
            "LFS_Bevel",
            "BEVEL",
        )

        bevel.width = 0.5
        bevel.segments = 2
        bevel.limit_method = "ANGLE"

        #
        # Subdivision Surface
        #

        subdivision = obj.modifiers.new(
            "LFS_Subdivision",
            "SUBSURF",
        )

        subdivision.levels = 1
        subdivision.render_levels = 2

        #
        # Auto smooth (Blender version dependent)
        #

        try:

            mesh.use_auto_smooth = True
            mesh.auto_smooth_angle = 1.0472

        except AttributeError:

            # Blender 5.x may use Smooth by Angle instead.
            pass

        return obj