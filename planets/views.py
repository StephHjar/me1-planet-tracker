from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView
from .models import Planet


class IndexView(TemplateView):
    template_name = 'index.html'


# class PlanetList(TemplateView):
#     template_name = 'planet_list.html'


class PlanetList(generic.ListView):
    model = Planet
    queryset = Planet.objects.order_by('-created_on')
    template_name = 'planet_list.html'


# def get_planet_list(request):
#     return render(request, 'planets_list.html')
