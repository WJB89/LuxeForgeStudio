from .addon import LuxeForgeAddon

bl_info = {
    "name": "LuxeForge Studio",
    "author": "Wesley",
    "version": (0, 3, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > LuxeForge",
    "description": "Procedural luxury accessories engine.",
    "category": "3D View",
}


def register():
    LuxeForgeAddon.register()


def unregister():
    LuxeForgeAddon.unregister()


if __name__ == "__main__":
    register()