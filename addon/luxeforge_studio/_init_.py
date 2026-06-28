bl_info = {
    "name": "LuxeForge Studio",
    "author": "Wesley",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > LuxeForge",
    "description": "LuxeForge Studio",
    "category": "3D View",
}

import bpy
from . import panel


def register():
    panel.register()


def unregister():
    panel.unregister()


if __name__ == "__main__":
    register()