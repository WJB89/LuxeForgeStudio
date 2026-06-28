"""
LuxeForge Studio

Geometry Builder
"""

from __future__ import annotations


class GeometryBuilder:
    """
    Builds 2D geometry.
    """

    def __init__(self):

        self._points = []

    @property
    def points(self):

        return self._points

    def move_to(self, x: float, y: float):

        self._points = [(x, y)]

        return self

    def line_to(self, x: float, y: float):

        self._points.append((x, y))

        return self

    def close(self):

        if self._points and self._points[0] != self._points[-1]:
            self._points.append(self._points[0])

        return self

    def clear(self):

        self._points.clear()

        return self