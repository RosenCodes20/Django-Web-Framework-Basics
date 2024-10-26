# Generated by Django 5.1.1 on 2024-10-06 13:52

import forumApp.posts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30, validators=[forumApp.posts.validators.check_author_name]),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[forumApp.posts.validators.content_length_validator]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[forumApp.posts.validators.check_if_bad_words_are_used_in_title]),
        ),
    ]