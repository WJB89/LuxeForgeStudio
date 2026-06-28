"""
LuxeForge Studio

2D Geometry Point
"""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot


@dataclass(slots=True, frozen=True)
class Point:
    """
    Represents a 2D point.

    This class is Blender independent and is used throughout the
    LuxeForge Core geometry engine.
    """

    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        """
        Returns the distance to another point.
        """

        return hypot(
            other.x - self.x,
            other.y - self.y,
        )

    def translate(
        self,
        dx: float,
        dy: float,
    ) -> "Point":
        """
        Returns a translated copy of this point.
        """

        return Point(
            self.x + dx,
            self.y + dy,
        )

    def as_tuple(self) -> tuple[float, float]:
        """
        Returns the point as a tuple.
        """

        return (
            self.x,
            self.y,
        )