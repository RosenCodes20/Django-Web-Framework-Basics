from django.db import models


class GenreChoices(models.TextChoices):
    POP_MUSIC = 'Pop Music', 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music', 'Jazz Music'
    RANDB = 'R&B Music', 'R&B Music'
    ROCK_MUSIC = 'Rock Music', 'Rock Music'
    COUNTRY_MUSIC = 'Country Music', 'Country Music'
    DANCE_MUSIC = 'Dance Music', 'Dance Music'
    HIP_HOP = 'Hip Hop Music', 'Hip Hop Music'
    OTHER = 'Other', 'Other'