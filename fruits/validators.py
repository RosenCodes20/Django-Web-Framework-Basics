from django.core.exceptions import ValidationError


def validate_fruit_name(value):

    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")
