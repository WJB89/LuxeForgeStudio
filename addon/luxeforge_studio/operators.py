import bpy

from luxeforge_studio.models.bag_parameters import BagParameters
from luxeforge_studio.services.bag_service import BagService


class LFS_OT_GenerateBag(bpy.types.Operator):
    """Generate a bag."""

    bl_idname = "lfs.generate_bag"
    bl_label = "Generate Bag"

    def execute(self, context):

        params = BagParameters()

        service = BagService()

        service.generate(params)

        self.report({"INFO"}, "Bag generated.")

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