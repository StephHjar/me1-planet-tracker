from django.shortcuts import render
from django.views import generic
from .models import Planet


class PlanetList(generic.ListView):
    model = Planet
    queryset = Planet.objects.order_by('-created_on')
    template_name = 'planets_list.html'


# def get_planet_list(request):
#     return render(request, 'planets/planets_list.html')


# def home(request):
#     return render(request, 'planets/base.html')
