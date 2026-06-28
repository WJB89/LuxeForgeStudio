import bpy

VERSION = "0.1.0-alpha"


class LFS_PT_MainPanel(bpy.types.Panel):
    """Main panel for LuxeForge Studio."""

    bl_label = "LuxeForge Studio"
    bl_idname = "LFS_PT_main_panel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LuxeForge"

    def draw(self, context):
        layout = self.layout

        # Header
        box = layout.box()
        box.label(text="Welcome Wesley!", icon="FUND")

        # Version
        box.separator()
        box.label(text=f"Version {VERSION}", icon="INFO")

        layout.separator()

        # Placeholder button
        layout.operator(
            "lfs.generate_bag",
            text="Generate Bag",
            icon="MESH_CUBE",
        )

        layout.separator()

        # Status
        status = layout.box()
        status.label(text="Project Status")
        status.label(text="No bag generated")


classes = (
    LFS_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)