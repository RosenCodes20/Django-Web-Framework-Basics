from django import forms
from django.forms import TextInput

from forumApp.posts.models import Post


class BasePostForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Post


class PostEditForm(BasePostForm):
    pass


class PostDeleteForm(BasePostForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchBarForm(forms.Form):

    post = forms.CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Search for a post....."
            }
        ),
        max_length=300,
        required=False,
        label=""
    )