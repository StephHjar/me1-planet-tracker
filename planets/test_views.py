from django.contrib.auth.models import User
from .models import Planet
from .forms import AddPlanetForm
from django.test import TestCase, Client


class TestViews(TestCase):
    """
    Unit testing for all views
    """
    def test_get_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_planet_list_view(self):
        client = Client()
        response = client.get('/planet/list/', follow=True, secure=True)
        self.assertRedirects(response, '/accounts/login/?next=/planet/list/')

        User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        client.login(username='testuser', password='testpass')
        response = client.get('/planet/list/', follow=True, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planets/planet_list.html')

    def test_get_add_planet_page(self):
        response = self.client.get('/planet/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planets/add_planet.html')

    def test_get_edit_planet_page(self):
        planet = Planet.objects.create(name='Virmire')
        response = self.client.get(f'/planet/edit/{planet.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planets/planet_form.html')

    def test_get_delete_planet_page(self):
        planet = Planet.objects.create(name='Luna')
        response = self.client.get(f'/planet/delete/{planet.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planets/planet_confirm_delete.html')

    def test_can_add_planet(self):
        User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/planet/add/',
                                    {'name': 'Xawin', 'user': 'testuser'})
        self.assertRedirects(response, '/planet/list/')

    def test_add_planet_form_redirects_if_invalid(self):
        User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser',
                          password='testpass')
        response = self.client.post('/planet/add/',
                                    {'name': '', 'user': 'testuser'})
        add_planet_form = AddPlanetForm(data=response)
        self.assertFalse(add_planet_form.is_valid())

    def test_can_edit_planet(self):
        User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        planet = Planet.objects.create(name='Luna')
        response = self.client.post(f'/planet/edit/{planet.id}')
        self.assertRedirects(response, '/planet/list/')

    def test_can_delete_planet(self):
        User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        planet = Planet.objects.create(name='Luna')
        response = self.client.post(f'/planet/delete/{planet.id}')
        self.assertRedirects(response, '/planet/list/')
        existing_planets = Planet.objects.filter(id=planet.id)
        self.assertEqual(len(existing_planets), 0)
