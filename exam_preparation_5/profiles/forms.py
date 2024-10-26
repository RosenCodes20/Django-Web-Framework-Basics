from django import forms
from django.forms import TextInput, PasswordInput

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "password")


class CreateProfileForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):
        widgets = {
            "first_name": TextInput(attrs={"placeholder": "First Name",}),
            "last_name": TextInput(attrs={"placeholder": "Last Name"}),
            "email": TextInput(attrs={"placeholder": "Email"}),
            "password": PasswordInput,
        }

        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": ""
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget.attrs["placeholder"] = "Password"


class EditProfileForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):

        fields = ("first_name", "last_name", "image_url", "age")