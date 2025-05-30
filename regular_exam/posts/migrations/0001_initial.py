# Generated by Django 5.1.2 on 2024-10-27 07:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': 'Oops! That title is already taken. How about something fresh and fun?'}, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('image_url', models.URLField(help_text='Share your funniest furry photo URL!')),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='authors.author')),
            ],
        ),
    ]
