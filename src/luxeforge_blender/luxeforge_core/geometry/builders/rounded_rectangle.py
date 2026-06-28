"""
LuxeForge Studio

Rounded Rectangle Builder
"""

from __future__ import annotations

from ..path import Path
from ..point import Point

from .corner_builder import CornerBuilder


class RoundedRectangleBuilder:
    """
    Builds a rounded rectangle profile.
    """

    def build(
        self,
        width: float,
        height: float,
        shoulder_width_ratio: float,
        shoulder_height_ratio: float,
        top_radius: float,
        bottom_radius: float,
        segments: int = 8,
    ) -> Path:

        half_width = width / 2

        shoulder_half = (
            width * shoulder_width_ratio
        ) / 2

        shoulder_y = (
            height * shoulder_height_ratio
        )

        path = Path()

        #
        # Start
        #

        path.move_to(
            -half_width,
            0,
        )

        #
        # Left side
        #

        path.line_to(
            -half_width,
            shoulder_y,
        )

        #
        # Top-left corner
        #

        CornerBuilder.top_left(
            path,
            Point(
                -shoulder_half,
                shoulder_y,
            ),
            top_radius,
            segments,
        )

        #
        # Top edge
        #

        path.line_to(
            shoulder_half,
            height,
        )

        #
        # Top-right corner
        #

        CornerBuilder.top_right(
            path,
            Point(
                shoulder_half,
                shoulder_y,
            ),
            top_radius,
            segments,
        )

        #
        # Right side
        #

        path.line_to(
            half_width,
            0,
        )

        #
        # Bottom edge
        #

        path.line_to(
            -half_width,
            0,
        )

        path.close()

        return path