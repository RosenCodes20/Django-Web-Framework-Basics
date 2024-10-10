import django.forms as forms

from MusicApp2.music.models import Album, Song


class BaseAlbumForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Album


class BaseSongForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Song

class EditAlbumBaseForm(BaseAlbumForm):
    pass


class DeleteAlbumBaseForm(BaseAlbumForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True