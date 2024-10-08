# Generated by Django 5.1.1 on 2024-09-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('py', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('c++', 'C++'), ('c', 'C'), ('other', 'Other')], default='other')),
            ],
        ),
    ]
