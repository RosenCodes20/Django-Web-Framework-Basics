from django.core.exceptions import ValidationError


def validate_nickname(nickname):
    if not nickname.isalpha():
        raise ValidationError("Your nickname is invalid!")