"""
LuxeForge Studio

Build Tool

Creates a distributable Blender add-on ZIP archive.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


# -------------------------------------------------
# Repository paths
# -------------------------------------------------

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

SOURCE_DIR = REPOSITORY_ROOT / "src" / "luxeforge_blender"

RELEASE_DIR = REPOSITORY_ROOT / "release"


# -------------------------------------------------
# Helpers
# -------------------------------------------------

def print_header():

    print("=" * 50)
    print("LuxeForge Studio Build Tool")
    print("=" * 50)
    print()


def get_version() -> str:
    """
    Reads the version from utils/version.py.
    Falls back to 'dev' if unavailable.
    """

    version_file = (
        SOURCE_DIR
        / "utils"
        / "version.py"
    )

    namespace = {}

    try:

        exec(version_file.read_text(encoding="utf8"), namespace)

        return namespace.get("VERSION_STRING", "dev")

    except Exception:

        return "dev"


def validate():

    if not SOURCE_DIR.exists():

        raise FileNotFoundError(
            f"Add-on folder not found:\n{SOURCE_DIR}"
        )


def prepare_release_folder():

    if RELEASE_DIR.exists():

        shutil.rmtree(RELEASE_DIR)

    RELEASE_DIR.mkdir(parents=True)


def build_zip():

    version = get_version()

    zip_name = f"LuxeForgeStudio-v{version}.zip"

    zip_path = RELEASE_DIR / zip_name

    with ZipFile(
        zip_path,
        "w",
        compression=ZIP_DEFLATED,
    ) as archive:

        for file in SOURCE_DIR.rglob("*"):

            if file.is_dir():
                continue

            archive_name = file.relative_to(SOURCE_DIR)

            archive.write(
                file,
                archive_name.as_posix(),
            )

    return zip_path


# -------------------------------------------------
# Main
# -------------------------------------------------

def main():

    print_header()

    try:

        validate()

        print("✓ Repository validated")

        prepare_release_folder()

        print("✓ Release folder prepared")

        zip_path = build_zip()

        print("✓ Build completed")
        print()
        print("Output:")
        print(zip_path)

        return 0

    except Exception as error:

        print()
        print("Build failed")
        print(error)

        return 1


if __name__ == "__main__":

    sys.exit(main())