from django.shortcuts import render, redirect

from django_web_framework_ex.django_ex.forms import BaseLeagueForm, BaseTeamForm, BasePlayerForm, PlayerEditForm, \
    PlayerDeleteForm
from django_web_framework_ex.django_ex.models import Player


def index(request):

    players = Player.objects.all()

    context = {
        "players": players
    }

    return render(request, "common/index.html", context)


def create_league(request):

    if request.method == "GET":
        form = BaseLeagueForm()

    else:
        form = BaseLeagueForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "leagues/create-league.html", context)


def login(request):

    return render(request, "logins/login.html")


def logout(request):

    return render(request, "logins/logout.html")


def register(request):

    return render(request, "logins/register.html")


def create_player(request):

    form = BasePlayerForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect("index")


    context = {
        "form": form
    }

    return render(request, "players/create-player.html", context)


def delete_player(request, pk):

    player = Player.objects.get(id=pk)

    if request.method == "GET":
        form = PlayerDeleteForm(instance=player)

    else:
        form = PlayerDeleteForm(request.POST, instance=player)

        player.delete()


    context = {
        "player": player,
        "form": form
    }

    return render(request, "players/delete-player.html", context)


def edit_player(request, pk):

    player = Player.objects.get(id=pk)

    if request.method == "GET":
        form = PlayerEditForm(instance=player)

    else:
        form = PlayerEditForm(request.POST, instance=player)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "player": player,
        "form": form
    }

    return render(request, "players/edit-player.html", context)


def player_details(request, pk):

    player = Player.objects.get(id=pk)

    context = {
        "player": player
    }

    return render(request, "players/player_details.html", context)


def edit_profile(request):

    return render(request, "profile/edit-profile.html")


def profile_details(request):

    return render(request, "profile/profile-details.html")

def create_team(request):

    if request.method == "GET":
        form = BaseTeamForm()

    else:
        form = BaseTeamForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")


    context = {
        "form": form
    }

    return render(request, "teams/create_team.html", context)