from django.db import models


class PlantChoices(models.TextChoices):

    OUTDOOR_PLANTS = "Outdoor Plants", "Outdoor Plants"
    INDOOR_PLANTS = "Indoor Plants", "Indoor Plants"