from django import forms

from exam_past_prep.traveler.models import Traveler


class CreateTravelerBaseForm(forms.ModelForm):

    class Meta:
        fields = ('nickname', 'email', 'country')
        model = Traveler
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': "Enter a unique nickname..."}),
            'email': forms.TextInput(attrs={'placeholder': "Enter a valid email address..."}),
            'country': forms.TextInput(attrs={'placeholder': "Enter a country code like <BGR>..."})
        }

        labels = {
            'nickname': 'Nickname:',
            'email': 'Email:',
            'country': 'Country:'
        }

class CreateTravelerForm(CreateTravelerBaseForm):
    pass