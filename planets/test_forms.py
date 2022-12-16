import unittest
from django.test import TestCase
from .forms import AddPlanetForm

        # fields = 'asari_writing', 'prothean_disc', 'mineral', 'medallion',
        #           'notes',)


class TestPlanetForm(TestCase):
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
