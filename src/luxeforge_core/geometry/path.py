"""
LuxeForge Studio

Geometry Path
"""

from __future__ import annotations

from .arc import Arc
from .point import Point


class Path:
    """
    Represents a 2D CAD path.
    """

    def __init__(self):

        self._points: list[Point] = []
        self._closed = False

    @property
    def points(self) -> list[Point]:
        """Returns all points."""

        return self._points

    @property
    def closed(self) -> bool:
        """Returns True if the path is closed."""

        return self._closed

    @property
    def count(self) -> int:
        """Returns the number of points."""

        return len(self._points)

    def move_to(
        self,
        x: float,
        y: float,
    ) -> "Path":
        """
        Starts a new path.
        """

        self._points = [
            Point(x, y)
        ]

        return self

    def line_to(
        self,
        x: float,
        y: float,
    ) -> "Path":
        """
        Adds a straight line.
        """

     def add_points(
         self,
         points: list[Point],
     ) -> "Path":
    """
    Adds multiple points to the path.

    The first point is skipped to avoid duplicate
    vertices when connecting geometry.
    """

    if not points:
        return self

    self._points.extend(points[1:])

    return self
        self._points.append(
            Point(x, y)
        )

        return self

    def arc_to(
        self,
        center: Point,
        radius: float,
        start_angle: float,
        end_angle: float,
        segments: int = 8,
    ) -> "Path":
        """
        Adds a circular arc.

        The first generated point is skipped to prevent
        duplicate vertices.
        """

        arc = Arc(
            center=center,
            radius=radius,
            start_angle=start_angle,
            end_angle=end_angle,
            segments=segments,
        )

        points = arc.generate_points()

        if points:

            self._points.extend(points[1:])

        return self

    def close(self) -> "Path":
        """
        Closes the path.
        """

        self._closed = True

        return self

    def clear(self) -> "Path":
        """
        Clears the path.
        """

        self._points.clear()

        self._closed = False

        return self