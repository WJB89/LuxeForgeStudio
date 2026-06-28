"""
LuxeForge Studio

Logger
"""

DEBUG = True


def log(message: str):

    if DEBUG:
        print(f"[LuxeForge] {message}")