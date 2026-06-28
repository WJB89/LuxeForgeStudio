"""
LuxeForge Studio

Arc Geometry
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, radians, sin

from .point import Point


@dataclass(slots=True)
class Arc:
    """
    Represents a circular arc.

    The arc is defined by a center point, radius,
    start angle and end angle.
    Angles are expressed in degrees.
    """

    center: Point

    radius: float

    start_angle: float

    end_angle: float

    segments: int = 8

    def generate_points(self) -> list[Point]:
        """
        Generates evenly spaced points along the arc.

        Returns
        -------
        list[Point]
            Points describing the arc.
        """

        if self.segments < 1:
            raise ValueError(
                "Arc requires at least one segment."
            )

        points: list[Point] = []

        angle_step = (
            self.end_angle - self.start_angle
        ) / self.segments

        for index in range(self.segments + 1):

            angle = self.start_angle + (
                angle_step * index
            )

            angle_rad = radians(angle)

            x = (
                self.center.x
                + cos(angle_rad) * self.radius
            )

            y = (
                self.center.y
                + sin(angle_rad) * self.radius
            )

            points.append(
                Point(
                    x=x,
                    y=y,
                )
            )

        return points