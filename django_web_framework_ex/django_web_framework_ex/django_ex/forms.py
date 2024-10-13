from django import forms

from django_web_framework_ex.django_ex.models import League, Team, Player


class BaseLeagueForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = League

        labels = {
            "league_name": "League Name:",
            "country": "Country:"
        }


class BaseTeamForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Team


class BasePlayerForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Player