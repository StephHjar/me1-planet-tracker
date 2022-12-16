from django.test import TestCase
from .forms import AddPlanetForm


class TestAddPlanetForm(TestCase):

    def test_name_is_required(self):
        form = AddPlanetForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_name_from_planet_list_is_required(self):
        form = AddPlanetForm({'name': 'testname'})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_fully_explored_is_not_required(self):
        form = AddPlanetForm({'name': 'Noveria'})
        self.assertTrue(form.is_valid())

    def test_turian_insignia_is_not_required(self):
        form = AddPlanetForm({'name': 'Jartar'})
        self.assertTrue(form.is_valid())

    def test_asari_writing_is_not_required(self):
        form = AddPlanetForm({'name': 'Wermani'})
        self.assertTrue(form.is_valid())

    def test_prothean_disc_is_not_required(self):
        form = AddPlanetForm({'name': 'Luna'})
        self.assertTrue(form.is_valid())

    def test_mineral_is_not_required(self):
        form = AddPlanetForm({'name': 'Inti'})
        self.assertTrue(form.is_valid())

    def test_medallion_is_not_required(self):
        form = AddPlanetForm({'name': 'Klensal'})
        self.assertTrue(form.is_valid())

    def test_notes_are_not_required(self):
        form = AddPlanetForm({'name': 'Paravin'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddPlanetForm()
        self.assertEqual(form.Meta.fields, ('name',
                                            'fully_explored',
                                            'turian_insignia',
                                            'asari_writing',
                                            'prothean_disc',
                                            'mineral',
                                            'medallion',
                                            'notes'))
