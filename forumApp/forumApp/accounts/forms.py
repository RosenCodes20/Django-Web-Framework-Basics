from django.contrib.auth.forms import UserCreationForm

from forumApp.accounts.models import CustomUserModel


class RegisterBaseForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ("username", "email")