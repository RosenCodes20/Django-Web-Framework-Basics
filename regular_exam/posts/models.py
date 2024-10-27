from django.core.validators import MinLengthValidator
from django.db import models

from authors.models import Author


class Post(models.Model):

    title = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(5)
        ],
        error_messages={
            "unique": "Oops! That title is already taken. How about something fresh and fun?"
        }
    )

    image_url = models.URLField()

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name="posts",
        editable=False
    )