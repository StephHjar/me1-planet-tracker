"""planet_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from planets.views import IndexView, PlanetList, AddPlanet, EditPlanet

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', IndexView.as_view(), name='home'),
    path('planet_list/', PlanetList.as_view(), name='planet_list'),
    path('accounts/', include('allauth.urls')),
    path('add_planet/', AddPlanet.as_view(), name='add_planet'),
    path('edit_planet/', EditPlanet.as_view(), name='edit_planet'),
]
