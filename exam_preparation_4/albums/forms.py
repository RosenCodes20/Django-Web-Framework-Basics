from django import forms
from django.forms import TextInput

from albums.models import Album


class AlbumBaseForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ("album_name", "artist", "genre", "description", "image_url", "price")

        widgets = {
            "album_name": TextInput(attrs={"placeholder": "Album Name"}),
            "artist": TextInput(attrs={"placeholder": "Artist"}),
            "description": TextInput(attrs={"placeholder": "Description"}),
            "image_url": TextInput(attrs={"placeholder": "Image URL"}),
            "price": TextInput(attrs={"placeholder": "Price"})
        }


class AlbumAddForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True