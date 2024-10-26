from django.core.exceptions import ValidationError


def validate_league_name(value):

    if value.split(" ")[0] == "Efbet":
        raise ValidationError("This is not a valid league!!")


def validate_team_name(value):

    if "Slavia" in value:
        raise ValidationError("This is not a good team!!!")


def validate_team_players(value):

    if value < 11:
        raise ValidationError("Team should be at least 11 players!!")


def validate_player_age(value):

    if value < 16 or value > 60:
        raise ValidationError("There isn't a player at this age!!")
