import re

from django.core.exceptions import ValidationError


def validate_name(value):

    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


def validate_passcode(value):

    if not re.findall(r"\d{6}", value):
        raise ValidationError("Your passcode must be exactly 6 digits!")