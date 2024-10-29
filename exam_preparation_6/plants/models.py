from django.core.validators import MinLengthValidator
from django.db import models

from plants.choices import PlantChoices
from plants.validators import validate_name_only_letters


class Plant(models.Model):

    plant_type = models.CharField(
        max_length=14,
        choices=PlantChoices.choices
    )

    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            validate_name_only_letters
        ],
    )

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()