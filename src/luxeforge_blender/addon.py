"""
LuxeForge Studio

Addon bootstrap.
"""

from __future__ import annotations

from .ui import operators
from .ui import panel


class LuxeForgeAddon:
    """
    Bootstrap class responsible for registering and
    unregistering the Blender add-on.
    """

    @staticmethod
    def register() -> None:
        """
        Register all Blender components.
        """

        operators.register()
        panel.register()

    @staticmethod
    def unregister() -> None:
        """
        Unregister all Blender components.
        """

        panel.unregister()
        operators.unregister()