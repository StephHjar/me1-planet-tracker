import unittest
from django.test import TestCase
from .forms import AddPlanetForm


class TestAddPlanetForm(TestCase):
    def test_name_is_required(self):
        form = AddPlanetForm({'name': ''})
        self.assertFalse(form.is_valid())

    def test_name_from_planet_list_is_required(self):
        form = AddPlanetForm({'name': 'testname'})
        self.assertFalse(form.is_valid())

    def test_fully_explored_is_not_required(self):
        form = AddPlanetForm({'name': 'Noveria', 'fully_explored': False})
        self.assertTrue(form.is_valid())

    def test_turian_insignia_is_not_required(self):
        form = AddPlanetForm({'name': 'Jartar', 'turian_insignia': False})
        self.assertTrue(form.is_valid())

    def test_asari_writing_is_not_required(self):
        form = AddPlanetForm({'name': 'Wermani', 'asari_writing': False})
        self.assertTrue(form.is_valid())

    def test_prothean_disc_is_not_required(self):
        form = AddPlanetForm({'name': 'Luna', 'prothean_disc': False})
        self.assertTrue(form.is_valid())

    def test_mineral_is_not_required(self):
        form = AddPlanetForm({'name': 'Inti', 'mineral': False})
        self.assertTrue(form.is_valid())

    def test_medallion_is_not_required(self):
        form = AddPlanetForm({'name': 'Klensal', 'medallion': False})
        self.assertTrue(form.is_valid())

    def test_notes_are_not_required(self):
        form = AddPlanetForm({'name': 'Paravin', 'notes': ''})
        self.assertTrue(form.is_valid())
