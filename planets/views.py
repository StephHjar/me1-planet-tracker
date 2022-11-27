from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView
from planets.models import Planet


class IndexView(TemplateView):
    template_name = 'index.html'


class PlanetList(generic.ListView):
    model = Planet
    queryset = Planet.objects.order_by('-created_on')
    template_name = 'planet_list.html'
