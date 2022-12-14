from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic import (TemplateView,
                                  ListView,
                                  View,
                                  DeleteView,
                                  UpdateView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from .models import Planet
from .forms import AddPlanetForm, EditPlanetForm, PlanetSearchForm


class IndexView(TemplateView):
    """
    View for the home / main landing page
    """
    template_name = 'index.html'


class PlanetFilter(BaseFilter):
    """
    Allows the user to search for planets by name from their dashboard
    """
    search_fields = {
        'search_text': ['name', ],
    }


class PlanetList(LoginRequiredMixin, SearchListView):
    """
    Planet list view, displays the user's planet dashboard
    with 8 planets per paged, ordered from the most recently updated
    """
    model = Planet
    template_name = 'planets/planet_list.html'
    paginate_by = 8

    form_class = PlanetSearchForm
    filter_class = PlanetFilter

    def get_queryset(self):
        return Planet.objects.filter(user=self.request.user). \
            order_by('-updated_on')


class AddPlanet(View):
    """
    Add planet view, displays & handles the form to add a planet
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'planets/add_planet.html',
            {
                "add_planet_form": AddPlanetForm(),
            }
        )

    def post(self, request, *args, **kwargs):

        add_planet_form = AddPlanetForm(data=request.POST)

        if add_planet_form.is_valid():
            add_planet_form.instance.user = self.request.user
            name = add_planet_form.cleaned_data.get('name')
            add_planet_form.save()
            messages.success(request,
                             'You have added %s to your planet list!' % name)
        else:
            add_planet_form = AddPlanetForm()

        return redirect('planet_list')


class EditPlanet(SuccessMessageMixin, UpdateView):
    """
    Displays and handles the form to edit a planet
    """
    model = Planet
    form_class = EditPlanetForm
    success_url = reverse_lazy('planet_list')
    success_message = 'Planet updated successfully!'


class DeletePlanet(DeleteView):
    """
    Displays and handles delete planet functionality
    """
    model = Planet
    success_url = reverse_lazy('planet_list')

    success_message = '%(name)s was removed from your planet list!'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data_to_return = super(DeletePlanet, self).delete(request,
                                                          *args,
                                                          **kwargs)
        messages.success(self.request, self.success_message % obj.__dict__)
        return data_to_return
