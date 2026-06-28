"""
LuxeForge Studio

Geometry Path
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PathPoint:
    x: float
    y: float


class Path:
    """
    Represents a 2D CAD path.
    """

    def __init__(self):

        self._points: list[PathPoint] = []
        self._closed = False

    @property
    def points(self) -> list[PathPoint]:
        """Returns all points in the path."""
        return self._points

    @property
    def closed(self) -> bool:
        """Returns True if the path is closed."""
        return self._closed

    @property
    def count(self) -> int:
        """Returns the number of points in the path."""
        return len(self._points)

    def move_to(self, x: float, y: float):

        self._points = [PathPoint(x, y)]

        return self

    def line_to(self, x: float, y: float):

        self._points.append(PathPoint(x, y))

        return self

    def close(self):

        self._closed = True

        return self

    def clear(self):

        self._points.clear()
        self._closed = False

        return self