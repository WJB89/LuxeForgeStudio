"""
LuxeForge Studio

Professional Blender add-on for creating
parametric luxury-inspired 3D printable accessories.

Author:
    Wesley

Architecture:
    ForgeCore
"""

from __future__ import annotations

import importlib

import bpy

from . import operators
from . import panel
from . import properties

bl_info = {
    "name": "LuxeForge Studio",
    "author": "Wesley",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > LuxeForge",
    "description": "Professional parametric luxury accessory generator.",
    "category": "Add Mesh",
}


# ----------------------------------------------------------------------
# Hot Reload
# ----------------------------------------------------------------------

if "bpy" in locals():
    importlib.reload(properties)
    importlib.reload(operators)
    importlib.reload(panel)


# ----------------------------------------------------------------------
# Registration
# ----------------------------------------------------------------------

MODULES = (
    properties,
    operators,
    panel,
)


def register() -> None:
    """Register LuxeForge Studio."""

    for module in MODULES:
        module.register()

    print("[LuxeForge] Registered")


def unregister() -> None:
    """Unregister LuxeForge Studio."""

    for module in reversed(MODULES):
        module.unregister()

    print("[LuxeForge] Unregistered")


if __name__ == "__main__":
    register()