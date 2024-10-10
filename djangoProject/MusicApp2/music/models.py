from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
    )

    image_url = models.URLField()

    price = models.FloatField()

    def __str__(self):
        return self.album_name

    def song_names_only(self):
        return [song.song_name for song in self.song_set.all()]

class Song(models.Model):

    song_name = models.CharField(
        max_length=30
    )

    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
    )

    music_file_data = models.FileField(null=True, blank=True)