from django.shortcuts import render
from django.views import generic


# Create your views here.

class PlanetList(generic.ListView):
    model = Planet
    queryset = Planet.objects.filter(status=1).order_by('-created_on')
    template_name = 'planets_list.html'


def get_planet_list(request):
    return render(request, 'planets/planets_list.html')


def home(request):
    return render(request, 'planets/base.html')
