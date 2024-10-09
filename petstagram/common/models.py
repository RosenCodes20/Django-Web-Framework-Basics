from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):

    comment_text = models.TextField(
        max_length=300
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
        related_name="photos"
    )