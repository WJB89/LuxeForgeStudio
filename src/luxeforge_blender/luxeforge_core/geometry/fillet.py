"""
LuxeForge Studio

Fillet Geometry
"""

from __future__ import annotations

from dataclasses import dataclass
from math import acos, degrees, tan

from .arc import Arc
from .point import Point
from .vector2 import Vector2


@dataclass(slots=True)
class Fillet:
    """
    Represents a rounded corner (fillet)
    between two connected line segments.
    """

    start: Point
    corner: Point
    end: Point
    radius: float

    def _vector(
        self,
        start: Point,
        end: Point,
    ) -> Vector2:

        return Vector2(
            end.x - start.x,
            end.y - start.y,
        )

    def angle(self) -> float:
        """
        Returns the interior angle in degrees.
        """

        v1 = self._vector(
            self.corner,
            self.start,
        ).normalized()

        v2 = self._vector(
            self.corner,
            self.end,
        ).normalized()

        dot = max(
            -1.0,
            min(
                1.0,
                v1.dot(v2),
            ),
        )

        return degrees(
            acos(dot)
        )

    def tangent_distance(self) -> float:
        """
        Distance from the corner
        to the tangent points.
        """

        angle = self.angle()

        if angle == 0:
            return 0.0

        return (
            self.radius /
            tan(
                (angle / 2) * 3.141592653589793 / 180
            )
        )

    def create_arc(self) -> Arc:
        """
        Placeholder.

        Sprint 6.5 will calculate:

        - tangent points
        - arc center
        - start angle
        - end angle

        and return a real Arc.
        """

        return Arc(
            center=self.corner,
            radius=self.radius,
            start_angle=0,
            end_angle=90,
            segments=8,
        )

    def __repr__(self) -> str:

        return (
            f"Fillet("
            f"radius={self.radius}, "
            f"angle={self.angle():.1f})"
        )