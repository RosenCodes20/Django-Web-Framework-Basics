from django import forms
from django.core.exceptions import ValidationError

from django_web_framework_ex.django_ex.models import League, Team, Player


class BaseLeagueForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = League

        labels = {
            "league_name": "League Name:",
            "country": "Country:"
        }

        error_messages = {
            "league_name": {
                "required": "This field is required",
                "invalid": "Enter a valid league name"
            },

            "country": {
                "required": "This field is required",
                "invalid": "Please enter a valid country!!"
            }
        }


    def clean_country(self):
        country = self.cleaned_data["country"]

        if not country[0].isupper():

            raise ValidationError("Please enter a country that starts with capital letter")


class BaseTeamForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Team


class BasePlayerForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Player

        error_messages = {
            "club": {
                "required": "Please select a club that this player plays in!",
            },

            "name": {
                "unique": "Name should be unique!!!",
                "required": "This field is required!"
            },

            "age": {
                "required": "This field is required",
                "invalid": "Enter a valid age!!"
            }
        }


class PlayerEditForm(BasePlayerForm):
    pass


class PlayerDeleteForm(BasePlayerForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True