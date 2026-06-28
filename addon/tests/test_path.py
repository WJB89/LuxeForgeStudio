"""
LuxeForge Studio

Path tests
"""

from __future__ import annotations

from ..geometry.path import Path


def run():

    print("=" * 40)
    print("Running Path tests")
    print("=" * 40)

    path = (
        Path()
        .move_to(0, 0)
        .line_to(100, 0)
        .line_to(100, 50)
        .line_to(0, 50)
        .close()
    )

    assert path.count == 4
    assert path.closed is True

    print("✓ Point count:", path.count)
    print("✓ Closed:", path.closed)

    print()

    for index, point in enumerate(path.points):

        print(
            f"Point {index}: "
            f"({point.x}, {point.y})"
        )

    print()
    print("All Path tests passed.")