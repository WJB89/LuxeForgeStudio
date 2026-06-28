import bpy

from .models.bag_parameters import BagParameters
from .services.bag_service import BagService
from .geometry.profile_generator import ProfileGenerator
from .utils.logger import log


class LFS_OT_GenerateBag(bpy.types.Operator):
    """Generate a bag."""

    bl_idname = "lfs.generate_bag"
    bl_label = "Generate Bag"

    def execute(self, context):

        params = BagParameters()

        profile = ProfileGenerator().generate(params)

        log("Generated profile:")
        log(str(profile))

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