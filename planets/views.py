from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from planets.models import Planet


class IndexView(TemplateView):
    template_name = 'index.html'


class PlanetList(LoginRequiredMixin, ListView):
    model = Planet
    template_name = 'planet_list.html'

    def get_queryset(self):
        return Planet.objects.filter(user=self.request.user).order_by('-created_on')
