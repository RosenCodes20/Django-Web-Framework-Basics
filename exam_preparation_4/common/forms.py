from django import forms
from django.forms import TextInput

from profiles.models import Profile


class BaseProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"

        # widgets = {
        #     "username": TextInput(attrs={"placeholder": "Username"}),
        #     "email": TextInput(attrs={"placeholder": "Email"}),
        #     "age": TextInput(attrs={"placeholder": "Age"})
        # }


class CreateProfileForm(BaseProfileForm):
    pass