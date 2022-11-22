from django.shortcuts import render

# Create your views here.


def get_planet_list(request):
    return render(request, 'planets/planets_list.html')
