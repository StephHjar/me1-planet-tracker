from .models import Planet
from django import forms


class AddPlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = ('name', 'fully_explored', 'turian_insignia',
                  'asari_writing', 'prothean_disc', 'mineral', 'medallion',
                  'notes',)


class EditPlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = ('fully_explored', 'turian_insignia',
                  'asari_writing', 'prothean_disc', 'mineral', 'medallion',
                  'notes',)
