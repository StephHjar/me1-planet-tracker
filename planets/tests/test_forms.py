from django.test import TestCase
from forms import AddPlanetForm


class TestPlanetForm(unittest.TestCase):
    def test_name_is_required(self):
        form = AddPlanetForm({'name': ''})
        self.assertFalse(form.is_valid())


unittest.main()
