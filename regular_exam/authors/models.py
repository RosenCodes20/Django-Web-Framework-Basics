from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from authors.validators import validate_name, validate_passcode


class Author(models.Model):

    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            validate_name
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            validate_name
        ]
    )

    passcode = models.CharField(
        validators=[
            validate_passcode
        ],
        help_text="Your passcode must be a combination of 6 digits"
    )

    pets_number = models.PositiveSmallIntegerField()


    info = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )
