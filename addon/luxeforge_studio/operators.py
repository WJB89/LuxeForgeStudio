import bpy


class LFS_OT_GenerateBag(bpy.types.Operator):
    """Temporary Generate Bag operator."""

    bl_idname = "lfs.generate_bag"
    bl_label = "Generate Bag"

    def execute(self, context):
        self.report({"INFO"}, "Generate Bag clicked!")
        print("Generate Bag clicked!")

        return {"FINISHED"}


classes = (
    LFS_OT_GenerateBag,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)