"""
LuxeForge Studio

Body Builder
"""

from __future__ import annotations

from ...geometry.extruder import Extruder
from ...geometry.mesh_data import MeshData
from ...geometry.path import Path
from ...models.bag_parameters import BagParameters


class BodyBuilder:
    """
    Builds a complete bag body from a 2D profile.

    Future responsibilities:

    - Apply fillets
    - Apply offsets
    - Generate wall thickness
    - Create inner shell
    - Generate piping
    - Add stitching guides
    """

    def __init__(self) -> None:

        self._extruder = Extruder()

    def build(
        self,
        profile: Path,
        params: BagParameters,
    ) -> MeshData:
        """
        Builds the complete body mesh.
        """

        #
        # Sprint 6.5
        # Extrude the profile directly.
        #

        mesh = self._extruder.extrude(
            profile,
            params.depth,
        )

        return mesh