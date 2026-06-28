bl_info = {
    "name": "LuxeForge Studio",
    "author": "Wesley",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > LuxeForge",
    "description": "Professional parametric luxury accessory generator.",
    "category": "3D View",
}

from . import panel
from . import operators


def register():
    operators.register()
    panel.register()


def unregister():
    panel.unregister()
    operators.unregister()


if __name__ == "__main__":
    register()