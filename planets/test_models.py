import unittest
from django.test import TestCase
from .models import Planet


class TestPlanet(TestCase):
    def test_fully_explored_defaults_to_false(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.fully_explored)

    def test_turian_insignia_defaults_to_false(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.turian_insignia)

    def test_asari_writing_defaults_to_false(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.asari_writing)

    def test_prothean_disc_defaults_to_false(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.prothean_disc)

    def test_mineral_defaults_to_false(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.mineral)

    def test_medallion_defaults_to_false(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.medallion)

    def test_notes_default_to_empty(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertFalse(planet.notes)

    def test_planet_string_method_returns_name(self):
        planet = Planet.objects.create(name='Virmire')
        self.assertEqual(str(planet), 'Virmire')
