from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Planet
from .forms import EditPlanetForm, AddPlanetForm


class IndexView(TemplateView):
    template_name = 'index.html'


class PlanetList(LoginRequiredMixin, ListView):
    model = Planet
    template_name = 'planet_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Planet.objects.filter(user=self.request.user). \
            order_by('-created_on')


class AddPlanet(TemplateView):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_planet.html',
            {
                "add_planet_form": AddPlanetForm(),
            }
        )

    def post(self, request, *args, **kwargs):

        add_planet_form = AddPlanetForm(data=request.POST)

        if add_planet_form.is_valid():
            add_planet_form.instance.user = self.request.user
            add_planet_form.save()
        else:
            add_planet_form = AddPlanetForm()

        return redirect('planet_list')


class EditPlanet(View):

    def get(self, request, id, *args, **kwargs):
        queryset = Planet.objects.filter(user=self.request.user)
        planet = get_object_or_404(queryset, id=id)
        name = planet.name

        return render(
            request,
            'edit_planet.html',
            {
                "name": name,
                "edit_planet_form": EditPlanetForm(),
                "fully_explored": planet.fully_explored,
                "turian_insignia": planet.turian_insignia,
                "asari_writing": planet.asari_writing,
                "prothean_disc": planet.prothean_disc,
                "mineral": planet.mineral,
                "medallion": planet.medallion,
                "notes": planet.notes
            }
        )

    # model = Planet
    # template_name = 'edit_planet.html'
    # fields = ['name', 'fully_explored', 'turian_insignia',
    #           'asari_writing', 'prothean_disc', 'mineral', 'medallion',
    #           'notes']
