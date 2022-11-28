from django.shortcuts import render, reverse
from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from planets.models import Planet


class IndexView(TemplateView):
    template_name = 'index.html'


class PlanetList(LoginRequiredMixin, ListView):
    model = Planet
    template_name = 'planet_list.html'

    def get_queryset(self):
        return Planet.objects.filter(user=self.request.user). \
            order_by('-created_on')


class AddPlanet(CreateView):
    model = Planet
    template_name = 'add_planet.html'
    fields = ['name', 'fully_explored', 'turian_insignia',
              'asari_writing', 'prothean_disc', 'mineral', 'medallion',
              'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPlanet, self).form_valid(form)

    def get_success_url(self):
        return reverse('planet_list')
