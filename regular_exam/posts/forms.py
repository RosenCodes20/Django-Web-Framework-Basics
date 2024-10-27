from django import forms

from posts.models import Post



class PostBaseForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"

        labels = {
            "image_url": "Post Image URL"
        }

        help_texts = {
            "image_url": ""
        }


class CreatePostForm(PostBaseForm):

    class Meta(PostBaseForm.Meta):
        help_texts = {
            "image_url": "Share your funniest furry photo URL!"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs["placeholder"] = "Put an attractive and unique title..."
        self.fields["content"].widget.attrs["placeholder"] = "Share some interesting facts about your adorable pets..."


class EditPostForm(PostBaseForm):
    pass

class DeletePostForm(PostBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = "readonly"