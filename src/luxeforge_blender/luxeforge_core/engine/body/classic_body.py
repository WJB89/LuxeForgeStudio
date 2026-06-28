"""
LuxeForge Studio

Classic Body Engine
"""

from __future__ import annotations

from ...geometry.mesh_data import MeshData
from ...models.bag_parameters import BagParameters

from .body_builder import BodyBuilder
from .profiles.classic_profile import ClassicProfile


class ClassicBodyEngine:
    """
    Generates the body of the Classic bag.
    """

    def __init__(self) -> None:

        self._profile = ClassicProfile()
        self._builder = BodyBuilder()

    def build(
        self,
        params: BagParameters,
    ) -> MeshData:
        """
        Generates a complete body mesh.
        """

        profile = self._profile.build(params)

        return self._builder.build(
            profile,
            params,
        )