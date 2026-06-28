"""
LuxeForge Studio

Build Tool

Packages the Blender add-on into a distributable ZIP archive.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


# -------------------------------------------------
# Repository paths
# -------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

ADDON_DIR = ROOT / "src" / "luxeforge_blender"

RELEASE_DIR = ROOT / "release"


# -------------------------------------------------
# Console
# -------------------------------------------------

def title():

    print("=" * 60)
    print("LuxeForge Studio Build Tool")
    print("=" * 60)
    print()


def info(message: str):

    print(f"✓ {message}")


# -------------------------------------------------
# Version
# -------------------------------------------------

def get_version() -> str:

    version_file = (
        ADDON_DIR
        / "luxeforge_core"
        / "utils"
        / "version.py"
    )

    namespace = {}

    try:

        exec(
            version_file.read_text(
                encoding="utf8"
            ),
            namespace,
        )

        return namespace.get(
            "VERSION_STRING",
            "dev",
        )

    except Exception:

        return "dev"


# -------------------------------------------------
# Validation
# -------------------------------------------------

def validate():

    if not ADDON_DIR.exists():

        raise RuntimeError(
            "Blender add-on folder not found."
        )

    if not (ADDON_DIR / "__init__.py").exists():

        raise RuntimeError(
            "__init__.py missing."
        )

    info("Repository validated")


# -------------------------------------------------
# Release folder
# -------------------------------------------------

def prepare_release():

    RELEASE_DIR.mkdir(exist_ok=True)

for file in RELEASE_DIR.glob("*.zip"):

    try:

        file.unlink()

    except PermissionError:

        print()
        print("WARNING")
        print(f"Cannot remove {file.name}")
        print("Close Blender or Explorer and try again.")
        raise


# -------------------------------------------------
# Build ZIP
# -------------------------------------------------

def build_zip():

    version = get_version()

    zip_name = f"LuxeForgeStudio-v{version}.zip"

    zip_path = RELEASE_DIR / zip_name

    with ZipFile(
        zip_path,
        "w",
        ZIP_DEFLATED,
    ) as archive:

        for file in ADDON_DIR.rglob("*"):

            if file.is_dir():
                continue

            archive_name = (
                Path("luxeforge_blender")
                / file.relative_to(ADDON_DIR)
            )

            archive.write(
                file,
                archive_name.as_posix(),
            )

    info("ZIP archive created")

    return zip_path


# -------------------------------------------------
# Main
# -------------------------------------------------

def main():

    title()

    try:

        validate()

        prepare_release()

        output = build_zip()

        print()
        print("Build completed successfully.")
        print()
        print(output)

        return 0

    except Exception as error:

        print()
        print("BUILD FAILED")
        print()
        print(error)

        return 1


if __name__ == "__main__":

    sys.exit(main())