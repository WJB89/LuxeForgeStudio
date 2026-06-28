"""
LuxeForge Studio

Line Geometry
"""

from __future__ import annotations

from dataclasses import dataclass

from .point import Point


@dataclass(slots=True, frozen=True)
class Line:
    """
    Represents a straight line segment between two points.
    """

    start: Point
    end: Point

    def generate_points(self) -> list[Point]:
        """
        Generates the points that describe this line.

        For a straight line this consists only of the
        start and end point.
        """

        return [
            self.start,
            self.end,
        ]

    @property
    def length(self) -> float:
        """
        Returns the length of the line.
        """

        return self.start.distance_to(self.end)

    @property
    def direction(self) -> tuple[float, float]:
        """
        Returns the normalized direction vector.
        """

        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y

        length = self.length

        if length == 0:
            return (0.0, 0.0)

        return (
            dx / length,
            dy / length,
        )

    def reversed(self) -> "Line":
        """
        Returns a reversed copy of the line.
        """

        return Line(
            start=self.end,
            end=self.start,
        )