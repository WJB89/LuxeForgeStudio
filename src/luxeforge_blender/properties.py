"""
LuxeForge Studio

Property definitions for the add-on.
"""

from __future__ import annotations

import bpy

from bpy.props import (
    FloatProperty,
    PointerProperty,
)

from bpy.types import (
    PropertyGroup,
    Scene,
)


class LFS_Settings(PropertyGroup):
    """Main settings for LuxeForge Studio."""

    bag_width: FloatProperty(
        name="Width",
        description="Bag width in millimeters",
        default=120.0,
        min=40.0,
        max=500.0,
        unit='LENGTH'
    )

    bag_height: FloatProperty(
        name="Height",
        description="Bag height in millimeters",
        default=90.0,
        min=40.0,
        max=500.0,
        unit='LENGTH'
    )

    bag_depth: FloatProperty(
        name="Depth",
        description="Bag depth in millimeters",
        default=45.0,
        min=10.0,
        max=300.0,
        unit='LENGTH'
    )

    wall_thickness: FloatProperty(
        name="Wall",
        description="Wall thickness",
        default=2.0,
        min=0.8,
        max=10.0,
        precision=2,
        unit='LENGTH'
    )

    corner_radius: FloatProperty(
        name="Corner Radius",
        description="Radius of rounded corners",
        default=8.0,
        min=0.0,
        max=50.0,
        unit='LENGTH'
    )

    flap_length: FloatProperty(
        name="Flap Length",
        description="Length of the flap",
        default=55.0,
        min=10.0,
        max=250.0,
        unit='LENGTH'
    )

    flap_thickness: FloatProperty(
        name="Flap Thickness",
        description="Thickness of the flap",
        default=2.5,
        min=0.8,
        max=20.0,
        precision=2,
        unit='LENGTH'
    )


CLASSES = (
    LFS_Settings,
)


def register() -> None:

    for cls in CLASSES:
        bpy.utils.register_class(cls)

    Scene.lfs = PointerProperty(type=LFS_Settings)


def unregister() -> None:

    del Scene.lfs

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)