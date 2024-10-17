from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_preparation_1.world_of_speed.choices import CarTypeChoices
from exam_preparation_1.world_of_speed.validators import check_right_username, validate_year


class Profile(models.Model):

    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(3, "Username must be at least 3 chars long!"),
            check_right_username
        ]
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(21)
        ],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=25
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=25
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=25
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class Car(models.Model):

    type = models.CharField(
        null=False,
        blank=False,
        choices=CarTypeChoices.choices,
        max_length=10
    )

    model = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            validate_year
        ]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        # TODO look again in the zadacha
        # TODO: DONE
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1)
        ]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="owners"
    )