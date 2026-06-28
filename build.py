from pathlib import Path
import shutil

ROOT = Path(__file__).parent

ADDON_NAME = "luxeforge_studio"

SOURCE = ROOT / "addon" / ADDON_NAME

RELEASE = ROOT / "release"

ZIP_NAME = "LuxeForgeStudio-v0.1.0-alpha"


def main():

    RELEASE.mkdir(exist_ok=True)

    temp = RELEASE / ADDON_NAME

    if temp.exists():
        shutil.rmtree(temp)

    shutil.copytree(SOURCE, temp)

    zip_file = RELEASE / ZIP_NAME

    shutil.make_archive(
        str(zip_file),
        "zip",
        RELEASE,
        ADDON_NAME,
    )

    shutil.rmtree(temp)

    print(f"Build complete: {zip_file}.zip")


if __name__ == "__main__":
    main()