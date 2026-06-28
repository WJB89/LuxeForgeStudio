"""
LuxeForge Studio

Bag generation service.
"""

from __future__ import annotations

from ..generators.body import BodyGenerator
from ..models.bag_parameters import BagParameters


class BagService:
    """High-level bag generation service."""

    def generate(self, params: BagParameters):

        generator = BodyGenerator()

        return generator.generate(params)