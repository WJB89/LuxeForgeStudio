"""
LuxeForge Studio

Classic Body Engine
"""

from __future__ import annotations

from .profiles.classic_profile import ClassicProfile
from ...geometry.extruder import Extruder
from ...models.bag_parameters import BagParameters
from ...geometry.mesh_data import MeshData


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