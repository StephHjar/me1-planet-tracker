import unittest
from django.test import TestCase
from .models import Planet


class PlanetTestCase(TestCase):
    def test_for_planet_name(self):
        """The planet's name must be a valid
        selection from the list of planets"""
        planet = Planet.objects.create(name="Eden Prime")
        self.assertEqual(planet.name, "Eden Prime")