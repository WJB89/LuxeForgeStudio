"""
LuxeForge Studio

Bag parameter model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class BagParameters:
    """Parameters describing a handbag."""

    width: float = 120.0
    height: float = 90.0
    depth: float = 45.0

    wall: float = 2.0

    corner_radius: float = 8.0

    flap_length: float = 55.0
    flap_thickness: float = 2.5