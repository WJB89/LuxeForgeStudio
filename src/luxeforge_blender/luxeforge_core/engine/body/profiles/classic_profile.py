"""
LuxeForge Studio

Classic Body Profile
"""

from __future__ import annotations

from ....geometry.builders.rounded_rectangle import (
    RoundedRectangleBuilder,
)
from ....geometry.path import Path
from ....models.bag_parameters import BagParameters


class ClassicProfile:
    """
    Generates the Classic bag profile.

    The profile delegates the actual geometry creation
    to the RoundedRectangleBuilder.
    """

    def __init__(self) -> None:

        self._builder = RoundedRectangleBuilder()

    def build(
        self,
        params: BagParameters,
    ) -> Path:
        """
        Builds the Classic bag outline.
        """

        return self._builder.build(
            width=params.width,
            height=params.height,
            shoulder_width_ratio=params.shoulder_width_ratio,
            shoulder_height_ratio=params.shoulder_height_ratio,
            top_radius=params.top_corner_radius,
            bottom_radius=params.bottom_corner_radius,
            segments=12,
        )