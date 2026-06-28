"""
LuxeForge Studio

Operators.
"""

from __future__ import annotations

import bpy

from .generators.body import BodyGenerator


class LFS_OT_GenerateBag(bpy.types.Operator):
    """Generate a new bag."""

    bl_idname = "lfs.generate_bag"
    bl_label = "Generate Bag"
    bl_description = "Generate a new LuxeForge bag"

    def execute(self, context):

        settings = context.scene.lfs

        generator = BodyGenerator()

        generator.generate(
            width=settings.bag_width,
            height=settings.bag_height,
            depth=settings.bag_depth,
            wall=settings.wall_thickness,
            radius=settings.corner_radius,
            flap_length=settings.flap_length,
            flap_thickness=settings.flap_thickness,
        )

        self.report({"INFO"}, "Bag generated")

        return {"FINISHED"}


CLASSES = (
    LFS_OT_GenerateBag,
)


def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)