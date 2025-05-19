from django.core.validators import MinLengthValidator
from django.db import models

from exam_past_prep.traveler.validators import validate_nickname


class Traveler(models.Model):

    nickname = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(3, 'Please enter a valid nickname!'),
            validate_nickname
        ],
        unique=True,
        null=False,
        blank=False,
        help_text="*Nicknames can contain only letters and digits."
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=30,
        unique=True
    )

    country = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(2)
        ]
    )

    about_me = models.TextField(
        null=True,
        blank=True
    )

