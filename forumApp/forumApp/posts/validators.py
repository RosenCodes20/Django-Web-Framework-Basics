from django.core.exceptions import ValidationError


def content_length_validator(value):

    if len(value) > 300:
        raise ValidationError("The value length should not be higher than 300 symbols!")


def check_author_name(value):

    if "Ioan" in value:
        raise ValidationError(f"{value} is banned from posting!!")


def check_if_bad_words_are_used_in_title(value):

    bad_words = ["word1", "word2", "word3"]

    for word in bad_words:
        if word in value:
            raise ValidationError("Bad word is used here!!")