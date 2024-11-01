from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, Textarea, formset_factory

from forumApp.posts.models import Post, Comment


class BasePostForm(forms.ModelForm):

    class Meta:
        exclude = ("approved",)
        model = Post

        error_messages = {
            "title": {
                "max_length": "The title is too long it should be under 100 chars!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].required = True


    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data["title"]

        author = cleaned_data.get("author")

        if "Python" in title and "Ivelin" in author or "Aleksandar" in author:
            raise ValidationError(f"{author} has nothing common with python!!!")

        if len(author.split(" ")[0]) > 12:
            raise ValidationError("Author length should be not more than 12 symbols!!")

        return cleaned_data


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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("author", "content")

        labels = {
            "author": "",
            "content": ""
        }

        error_messages = {
            "author": {
                "max_length": "Please enter a valid author name with length of 30 chars!!",
                "required": "Please enter an author right now!!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["author"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter an author....."
        })

        self.fields["content"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter message.....",
            "rows": 1
        })


CommentFormSet = formset_factory(CommentForm, extra=1)