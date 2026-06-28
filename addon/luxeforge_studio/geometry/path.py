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
    def points(self):

        return self._points

    @property
    def closed(self):

        return self._closed

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