"""
LuxeForge Studio

2D Vector Geometry
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(slots=True)
class Vector2:
    """
    Represents a 2D vector.
    """

    x: float
    y: float

    def length(self) -> float:
        """
        Returns the vector length.
        """

        return sqrt(
            self.x * self.x +
            self.y * self.y
        )

    def normalized(self) -> "Vector2":
        """
        Returns a normalized copy.
        """

        length = self.length()

        if length == 0:
            return Vector2(0.0, 0.0)

        return Vector2(
            self.x / length,
            self.y / length,
        )

    def perpendicular(self) -> "Vector2":
        """
        Returns a left-hand perpendicular vector.
        """

        return Vector2(
            -self.y,
            self.x,
        )

    def dot(
        self,
        other: "Vector2",
    ) -> float:
        """
        Dot product.
        """

        return (
            self.x * other.x +
            self.y * other.y
        )

    def scale(
        self,
        factor: float,
    ) -> "Vector2":
        """
        Scales the vector.
        """

        return Vector2(
            self.x * factor,
            self.y * factor,
        )

    def __add__(
        self,
        other: "Vector2",
    ) -> "Vector2":

        return Vector2(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(
        self,
        other: "Vector2",
    ) -> "Vector2":

        return Vector2(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(
        self,
        factor: float,
    ) -> "Vector2":

        return self.scale(factor)

    def __truediv__(
        self,
        factor: float,
    ) -> "Vector2":

        if factor == 0:
            raise ZeroDivisionError(
                "Cannot divide vector by zero."
            )

        return Vector2(
            self.x / factor,
            self.y / factor,
        )

    def __repr__(self) -> str:

        return (
            f"Vector2("
            f"x={self.x:.3f}, "
            f"y={self.y:.3f})"
        )