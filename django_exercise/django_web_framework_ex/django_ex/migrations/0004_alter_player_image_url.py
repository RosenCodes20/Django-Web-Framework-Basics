# Generated by Django 5.1.2 on 2024-10-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ex', '0003_player_image_url_alter_team_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_url',
            field=models.URLField(),
        ),
    ]