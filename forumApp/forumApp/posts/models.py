from django.db import models

from forumApp.posts.choices import LanguageChoices
from forumApp.posts.validators import content_length_validator, check_author_name, check_if_bad_words_are_used_in_title


class Post(models.Model):

    title = models.CharField(
        max_length=100,
        validators=[
            check_if_bad_words_are_used_in_title
        ],

        error_messages={
            "required": "The title should be entered or i'll ban you!!!"
        }

    )

    content = models.TextField(
        validators=[
            content_length_validator
        ]
    )

    author = models.CharField(
        max_length=30,
        validators=[
            check_author_name
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    language = models.CharField(
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER
    )


class Comment(models.Model):

    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.CharField(
        max_length=30,
        validators=[
            check_author_name
        ]
    )

    content = models.TextField(
        validators=[
            content_length_validator
        ]
    )

    created_at = models.DateTimeField(
        auto_now=True
    )