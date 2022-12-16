from django.test import TestCase
from planets.forms import AddPlanetForm


class TestPlanetForm(TestCase):
    def test_name_is_required(self):
        form = AddPlanetForm({'name': ''})
        self.assertFalse(form.is_valid())


unittest.main()
