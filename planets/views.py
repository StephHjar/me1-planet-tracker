from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from planets.models import Planet


class IndexView(TemplateView):
    template_name = 'index.html'


class PlanetList(LoginRequiredMixin, ListView):
    model = Planet
    template_name = 'planet_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Planet.objects.filter(user=self.request.user). \
            order_by('-created_on')


class AddPlanet(CreateView):
    model = Planet
    template_name = 'add_planet.html'
    fields = ['name', 'fully_explored', 'turian_insignia',
              'asari_writing', 'prothean_disc', 'mineral', 'medallion',
              'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPlanet, self).form_valid(form)

    def get_success_url(self):
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
