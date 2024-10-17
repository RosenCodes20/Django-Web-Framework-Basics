from django import forms

from exam_preparation_1.world_of_speed.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")

        widgets = {
            "password": forms.PasswordInput()
        }


class CreateCarBaseForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")

        widgets = {
            "image_url": forms.TextInput(attrs={
                "placeholder": "https://..."
            })
        }


class EditCarForm(CreateCarBaseForm):
    pass


class DeleteCarForm(CreateCarBaseForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class EditProfileForm(ProfileBaseForm):

    class Meta:
        fields = "__all__"
        model = Profile
