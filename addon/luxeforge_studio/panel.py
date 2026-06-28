import bpy


class LFS_PT_MainPanel(bpy.types.Panel):

    bl_label = "LuxeForge Studio"
    bl_idname = "LFS_PT_main"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LuxeForge"

    def draw(self, context):

        layout = self.layout

        layout.label(text="Hello Wesley!")

        layout.label(text="Welcome to LuxeForge Studio")


classes = (
    LFS_PT_MainPanel,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)