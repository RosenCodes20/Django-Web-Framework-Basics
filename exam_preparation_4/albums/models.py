from django.core.validators import MinValueValidator
from django.db import models

from albums.choices import GenreChoices
from profiles.models import Profile


class Album(models.Model):

    album_name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=30
    )

    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30
    )

    genre = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        choices=GenreChoices.choices
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0)
        ]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="albums"
    )