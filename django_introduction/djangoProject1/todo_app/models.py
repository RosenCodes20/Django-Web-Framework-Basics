

from django.db import models
# Create your models here.


class TodoApp(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )