"""
LuxeForge Studio

Body generator.

Version:
    v0.1.0-alpha.2
"""

from __future__ import annotations

import bpy


class BodyGenerator:
    """Generates the basic bag body."""

    OBJECT_NAME = "LFS_Bag"

    def generate(
        self,
        *,
        width: float,
        height: float,
        depth: float,
        wall: float,
        radius: float,
        flap_length: float,
        flap_thickness: float,
    ) -> bpy.types.Object:
        """
        Generate the base body.

        Parameters are currently stored for future use.
        Version alpha.2 creates only a scaled body.
        """

        # --------------------------------------------------
        # Remove old generated object
        # --------------------------------------------------

        existing = bpy.data.objects.get(self.OBJECT_NAME)

        if existing:
            bpy.data.objects.remove(existing, do_unlink=True)

        # --------------------------------------------------
        # Create cube
        # --------------------------------------------------

        bpy.ops.mesh.primitive_cube_add(
            location=(0.0, 0.0, height / 2.0)
        )

        obj = bpy.context.active_object
        obj.name = self.OBJECT_NAME

        # Blender cube = 2x2x2
        obj.scale = (
            width / 2.0,
            depth / 2.0,
            height / 2.0,
        )

        # --------------------------------------------------
        # Apply scale
        # --------------------------------------------------

        bpy.ops.object.transform_apply(
            location=False,
            rotation=False,
            scale=True,
        )

        # --------------------------------------------------
        # Shade smooth
        # --------------------------------------------------

        bpy.ops.object.shade_smooth()

        # --------------------------------------------------
        # Future:
        #
        # - Bevel Modifier
        # - Solidify
        # - Flap
        # - Quilting
        # --------------------------------------------------

        return obj