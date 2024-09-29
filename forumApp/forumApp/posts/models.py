from django.db import models

from forumApp.posts.choices import LanguageChoices


class Post(models.Model):

    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    author = models.CharField(
        max_length=30
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    language = models.CharField(
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER
    )