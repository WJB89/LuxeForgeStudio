"""
LuxeForge Studio

Classic Body Engine
"""

from __future__ import annotations

from luxeforge_core.engine.body.profiles.classic_profile import ClassicProfile
from luxeforge_core.geometry.extruder import Extruder
from luxeforge_core.models.bag_parameters import BagParameters
from luxeforge_core.geometry.mesh_data import MeshData


class ClassicBodyEngine:
    """
    Generates the 3D body of the Classic bag.
    """

    def build(
        self,
        params: BagParameters,
    ) -> MeshData:
        """
        Builds the Classic bag body.
        """

        profile = ClassicProfile().build(params)

        mesh = Extruder().extrude(
            profile,
            params.depth,
        )

        return mesh