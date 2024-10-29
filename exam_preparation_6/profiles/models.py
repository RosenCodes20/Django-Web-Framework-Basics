from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import validate_name


class Profile(models.Model):

    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2)
        ]
    )

    first_name = models.CharField(
        max_length=20,
        validators=[
            validate_name
        ]
    )

    last_name = models.CharField(
        max_length=20,
        validators=[
            validate_name
        ]
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )