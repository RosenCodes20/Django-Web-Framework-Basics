from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import validate_profile_username


class Profile(models.Model):

    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=[
            MinLengthValidator(2),
            validate_profile_username
        ],
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

