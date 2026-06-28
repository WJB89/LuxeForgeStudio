"""
LuxeForge Studio

Profile Generator
"""

from __future__ import annotations

from ..models.bag_parameters import BagParameters


class ProfileGenerator:
    """
    Generates the 2D outline of the handbag body.
    """

    def generate(self, params: BagParameters) -> list[tuple[float, float]]:

        w = params.width / 2
        h = params.height
        r = params.corner_radius

        profile = [

            (-w, 0.0),

            (-w, h - r),

            (-w + r, h),

            (w - r, h),

            (w, h - r),

            (w, 0.0),

        ]

        return profile