from django.core.exceptions import ValidationError


def validate_profile_username(value):

    if not value.isalnum():
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")