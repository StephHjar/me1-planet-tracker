from django.test import TestCase
from planets.models import Planet


class PlanetTestCase(TestCase):
    def setUp(self):
        Planet.objects.create(name="Invalid")
