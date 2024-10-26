# Generated by Django 5.1.2 on 2024-10-26 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='profiles.profile'),
        ),
    ]
