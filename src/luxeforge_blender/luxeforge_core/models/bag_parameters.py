"""
LuxeForge Studio

Bag parameter model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BagParameters:
    """
    Parameters describing a handbag.
    """

    #
    # Overall dimensions (mm)
    #

    width: float = 120.0
    height: float = 90.0
    depth: float = 45.0

    #
    # Construction
    #

    wall_thickness: float = 2.0

    #
    # Profile
    #

    shoulder_height_ratio: float = 0.80
    shoulder_width_ratio: float = 0.90

    side_taper: float = 8.0

    top_corner_radius: float = 12.0
    bottom_corner_radius: float = 8.0

    #
    # Flap
    #

    flap_length: float = 55.0
    flap_thickness: float = 2.5