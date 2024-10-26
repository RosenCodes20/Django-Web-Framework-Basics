from django.db import models

from django_web_framework_ex.django_ex.validators import validate_league_name, validate_team_name, \
    validate_team_players, validate_player_age


class League(models.Model):

    league_name = models.CharField(
        max_length=200,
        validators=[
            validate_league_name
        ]
    )

    country = models.CharField(
        max_length=200,
    )

    def __str__(self):

        return self.league_name


class Team(models.Model):

    team_name = models.CharField(
        max_length=100,
        validators=[
            validate_team_name
        ],
        unique=True
    )

    team_league = models.ForeignKey(
        to=League,
        on_delete=models.CASCADE,
        related_name="league",
        default=League.objects.all()[0] if League.objects.all() else None,
        blank=True,
        null=True
    )

    players = models.IntegerField(
        validators=[
            validate_team_players
        ]
    )

    def __str__(self):
        return self.team_name


class Player(models.Model):

    name = models.CharField(
        max_length=100
    )

    age = models.IntegerField(
        validators=[
            validate_player_age
        ]
    )

    price = models.BigIntegerField()

    club = models.ForeignKey(
        to=Team,
        on_delete=models.CASCADE,
        related_name="team"
    )

    image_url = models.URLField()