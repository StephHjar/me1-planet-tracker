from .models import Planet
from django import forms


class AddPlanetForm(forms.ModelForm):
    """
    Form that adds a planet to the database & planet dashboard
    """
    class Meta:
        model = Planet
        fields = ('name', 'fully_explored', 'turian_insignia',
                  'asari_writing', 'prothean_disc', 'mineral', 'medallion',
                  'notes',)


class EditPlanetForm(forms.ModelForm):
    """
    Form that allows the user to edit one of their own planets
    """
    class Meta:
        model = Planet
        fields = ('fully_explored', 'turian_insignia',
                  'asari_writing', 'prothean_disc', 'mineral', 'medallion',
                  'notes',)


class PlanetSearchForm(forms.Form):
    """
    Form that functions as a search bar on the user's planet dashboard
    """
    search_text = forms.CharField(
        required=True,
        label='Search by planet name ',
        widget=forms.TextInput(attrs={'placeholder': 'Search planets!'})
    )
