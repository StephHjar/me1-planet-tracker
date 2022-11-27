from django.test import TestCase
from planets.models import Planet


class PlanetTestCase(TestCase):
    def setUp(self):
        Planet.objects.create(name="Eden Prime")

    def test_for_planet_name(self):
        """The planet's name must be a valid
        selection from the list of planets"""
        planet = Planet.objects.get(name="Eden Prime")
        self.assertEqual(planet.name, "Eden Prime")
