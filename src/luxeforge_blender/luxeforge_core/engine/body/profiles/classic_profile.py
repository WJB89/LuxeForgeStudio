"""
LuxeForge Studio

Classic Body Profile
"""

from __future__ import annotations

from ....geometry.path import Path
from ....models.bag_parameters import BagParameters


class ClassicProfile:
    """
    Generates the 2D outline of the Classic bag.

    This class is responsible only for generating
    the 2D profile. It does not create meshes or
    interact with Blender.
    """

    #
    # Design constants
    #

    SHOULDER_HEIGHT = 0.80
    SHOULDER_WIDTH = 0.90

    def build(
        self,
        params: BagParameters,
    ) -> Path:
        """
        Builds the classic bag profile.

        Parameters
        ----------
        params
            Bag dimensions.

        Returns
        -------
        Path
            Closed 2D outline.
        """

        half_width = params.width / 2
        height = params.height

        shoulder_y = height * self.SHOULDER_HEIGHT
        shoulder_x = half_width * self.SHOULDER_WIDTH

        path = Path()

        (
            path
            .move_to(-half_width, 0)
            .line_to(-half_width, shoulder_y)
            .line_to(-shoulder_x, height)
            .line_to(shoulder_x, height)
            .line_to(half_width, shoulder_y)
            .line_to(half_width, 0)
            .close()
        )

        return path