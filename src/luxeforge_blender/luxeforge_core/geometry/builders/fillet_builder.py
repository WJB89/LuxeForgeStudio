"""
LuxeForge Studio

Fillet Builder
"""

from __future__ import annotations

from ..arc import Arc
from ..point import Point


class FilletBuilder:
    """
    Creates circular fillets between two line segments.

    This class will become the central geometry builder
    for rounded corners throughout LuxeForge Studio.

    Future versions will calculate:

    - tangent points
    - arc center
    - start/end angles
    - trimmed line segments
    """

    def build(
        self,
        center: Point,
        radius: float,
        start_angle: float,
        end_angle: float,
        segments: int = 8,
    ) -> Arc:
        """
        Creates an Arc representing a fillet.

        Current implementation is a thin wrapper around Arc.
        Future versions will calculate the Arc automatically
        from three connected points.
        """

        return Arc(
            center=center,
            radius=radius,
            start_angle=start_angle,
            end_angle=end_angle,
            segments=segments,
        )