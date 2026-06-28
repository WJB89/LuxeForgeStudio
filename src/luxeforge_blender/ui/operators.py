"""
LuxeForge Studio

Generate Bag Operator.
"""

from __future__ import annotations

import bpy

from ..bridge.mesh_builder import MeshBuilder

from ..luxeforge_core.models.bag_parameters import BagParameters
from ..luxeforge_core.services.bag_service import BagService


class LFS_OT_GenerateBag(bpy.types.Operator):
    """
    Generates a LuxeForge bag.
    """

    bl_idname = "lfs.generate_bag"
    bl_label = "Generate Bag"

    def execute(
        self,
        context,
    ):

        #
        # Create default parameters
        #

        params = BagParameters()

        #
        # Generate mesh data
        #

        mesh_data = BagService().generate(params)

        #
        # Create Blender object
        #

        MeshBuilder.create_mesh(
            "LFS_ClassicBag",
            mesh_data,
        )

        self.report(
            {"INFO"},
            "Classic bag generated.",
        )

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