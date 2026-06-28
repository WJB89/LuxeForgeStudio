"""
LuxeForge Studio

Main UI Panel
"""

from __future__ import annotations

import bpy


class LFS_PT_MainPanel(bpy.types.Panel):
    """Main LuxeForge Studio panel."""

    bl_label = "LuxeForge Studio"
    bl_idname = "LFS_PT_main_panel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LuxeForge"

    def draw(self, context):

        layout = self.layout

        settings = context.scene.lfs

        # ----------------------------------------------------
        # Dimensions
        # ----------------------------------------------------

        box = layout.box()

        box.label(text="Dimensions", icon="MESH_CUBE")

        box.prop(settings, "bag_width")
        box.prop(settings, "bag_height")
        box.prop(settings, "bag_depth")

        # ----------------------------------------------------
        # Construction
        # ----------------------------------------------------

        box = layout.box()

        box.label(text="Construction", icon="MOD_SOLIDIFY")

        box.prop(settings, "wall_thickness")
        box.prop(settings, "corner_radius")

        # ----------------------------------------------------
        # Flap
        # ----------------------------------------------------

        box = layout.box()

        box.label(text="Flap", icon="MOD_BEVEL")

        box.prop(settings, "flap_length")
        box.prop(settings, "flap_thickness")

        # ----------------------------------------------------
        # Actions
        # ----------------------------------------------------

        layout.separator()

        layout.operator(
            "lfs.generate_bag",
            icon="MESH_CUBE"
        )


CLASSES = (
    LFS_PT_MainPanel,
)


def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)