"""
LuxeForge Studio

Bag Service
"""

from __future__ import annotations

from luxeforge_core.engine.body.classic_body import ClassicBodyEngine
from luxeforge_core.geometry.mesh_data import MeshData
from luxeforge_core.models.bag_parameters import BagParameters


class BagService:
    """
    High-level service responsible for generating bags.

    The service orchestrates the different engines that
    make up a bag. At the moment only the body is generated.
    """

    def generate(
        self,
        params: BagParameters,
    ) -> MeshData:
        """
        Generates a bag.
        """

        body_engine = ClassicBodyEngine()

        mesh = body_engine.build(params)

        return mesh