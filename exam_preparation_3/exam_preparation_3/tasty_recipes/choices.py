from django.db import models


class CuisineTypeChoices(models.TextChoices):

    FRENCH = "French", "French"
    CHINESE = "Chinese", "Chinese"
    ITALIAN = "Italian", "Italian"
    BALKAN = "Balkan", "Balkan"
    OTHER = "Other", "Other"