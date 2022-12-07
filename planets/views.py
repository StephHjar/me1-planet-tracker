from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Planet
from .forms import AddPlanetForm


class IndexView(TemplateView):
    template_name = 'index.html'


class PlanetList(LoginRequiredMixin, ListView):
    model = Planet
    template_name = 'planet_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Planet.objects.filter(user=self.request.user). \
            order_by('-created_on')


class AddPlanet(View):

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


class EditPlanet(UpdateView):

    model = Planet

    fields = ['fully_explored', 'turian_insignia', 'asari_writing',
              'prothean_disc', 'mineral', 'medallion', 'notes']

    success_url = "/planet_list"

    # def get(self, request, id, *args, **kwargs):
    #     queryset = Planet.objects.filter(user=self.request.user)
    #     planet = get_object_or_404(queryset, id=id)
    #     name = planet.name

    #     return render(
    #         request,
    #         'edit_planet.html',
    #         {
    #             "name": name,
    #             "edit_planet_form": EditPlanetForm(instance=planet),
    #         }
    #     )

    # def post(self, request, id, *args, **kwargs):
    #     queryset = Planet.objects.filter(user=self.request.user)
    #     planet = get_object_or_404(queryset, id=id)
    #     name = planet.name

    #     edit_planet_form = EditPlanetForm(data=request.POST)

    #     if edit_planet_form.is_valid():
    #         edit_planet_form.instance.user = self.request.user
    #         edit_planet_form.instance.name = name
    #         edit_planet_form.instance.id = id
    #         edit_planet_form.instance.created_on = self.request.created_on
    #         edit_planet_form.save()
    #     else:
    #         edit_planet_form = EditPlanetForm(instance=planet)

        # return redirect('planet_list')


class DeletePlanet(DeleteView):
    model = Planet
    success_url = reverse_lazy('planet_list')
