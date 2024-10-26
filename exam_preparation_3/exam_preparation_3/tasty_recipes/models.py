from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_preparation_3.tasty_recipes.choices import CuisineTypeChoices
from exam_preparation_3.tasty_recipes.validators import validate_name_starts_with_capital


class Profile(models.Model):

    nickname = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=20,
        validators=[
            MinLengthValidator(2, "Nickname must be at least 2 chars long!")
        ]
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            validate_name_starts_with_capital
        ]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            validate_name_starts_with_capital
        ]
    )

    chef = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    bio = models.TextField(
        blank=True,
        null=True
    )


class Recipe(models.Model):

    title = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(10)
        ]

        #TODO: ADD MESSAGE FOR UNIQUE IN FORMS
    )

    cuisine_type = models.CharField(
        blank=False,
        null=False,
        max_length=7,
        choices=CuisineTypeChoices.choices
    )

    ingredients = models.TextField(
        blank=False,
        null=False,
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField(
        blank=False,
        null=False
    )

    cooking_time = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1)
        ],
        help_text="Provide the cooking time in minutes."
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="recipe"
    )
