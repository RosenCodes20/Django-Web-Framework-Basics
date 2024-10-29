from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"



class ProfileForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):
        fields = ("username", "first_name", "last_name")


class EditProfileForm(ProfileBaseForm):
    pass