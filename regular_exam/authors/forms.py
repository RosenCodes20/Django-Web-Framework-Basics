from django import forms
from django.forms import PasswordInput

from authors.models import Author


class AuthorBaseForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = "__all__"



class CreateAuthorForm(AuthorBaseForm):

    class Meta(AuthorBaseForm.Meta):
        fields = ("first_name", "last_name", "passcode", "pets_number")
        widgets = {
            "passcode": PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = "Enter your first name..."
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter your last name..."
        self.fields["passcode"].widget.attrs["placeholder"] = "Enter 6 digits..."
        self.fields["pets_number"].widget.attrs["placeholder"] = "Enter the number of your pets..."


class EditAuthorForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        labels = {
            "image_url": "Post Image URL"
        }
        fields = ("first_name", "last_name", "pets_number", "info", "image_url")