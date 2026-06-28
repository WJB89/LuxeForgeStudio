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

    def __init__(self) -> None:

        self._points: list[Point] = []
        self._closed = False

    @property
    def points(self) -> list[Point]:
        """
        Returns all points.
        """

        return self._points

    @property
    def closed(self) -> bool:
        """
        Returns True if the path is closed.
        """

        return self._closed

    @property
    def count(self) -> int:
        """
        Returns the number of points.
        """

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
            Point(x, y),
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

        self._points.append(
            Point(x, y),
        )

        return self

    def add_points(
        self,
        points: list[Point],
    ) -> "Path":
        """
        Adds multiple points.

        The first point is skipped to avoid duplicate
        vertices.
        """

        if not points:
            return self

        self._points.extend(points[1:])

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
        """

        arc = Arc(
            center=center,
            radius=radius,
            start_angle=start_angle,
            end_angle=end_angle,
            segments=segments,
        )

        self.add_points(
            arc.generate_points(),
        )

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

    def __len__(self) -> int:
        """
        Returns the number of points.
        """

        return len(self._points)

    def __iter__(self):
        """
        Iterates over all points.
        """

        return iter(self._points)

    def __repr__(self) -> str:
        """
        Returns a readable representation.
        """

        return (
            f"Path(points={len(self)}, "
            f"closed={self.closed})"
        )