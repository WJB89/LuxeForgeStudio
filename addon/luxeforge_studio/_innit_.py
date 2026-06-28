bl_info = {
    "name": "LuxeForge Studio",
    "author": "Wesley",
    "description": "Parametric luxury accessory generator",
    "blender": (5, 0, 0),
    "version": (0, 1, 0),
    "location": "View3D > Sidebar",
    "category": "Add Mesh",
}


def register():
    print("LuxeForge Studio loaded.")


def unregister():
    print("LuxeForge Studio unloaded.")