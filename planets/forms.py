# from .models import Planet
# from django import forms


# class PlanetForm(forms.ModelForm):
#     class Meta:
#         model = Planet
#         fields = ('name', 'fully_explored', 'turian_insignia',
#                   'asari_writing', 'prothean_disc', 'mineral', 'medallion',
#                   'notes',)
                
#         def form_valid(self, form):
#             form.instance.user = self.request.user
#             return super().form_valid(form)