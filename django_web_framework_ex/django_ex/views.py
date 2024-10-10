from django.shortcuts import render


def index(request):

    return render(request, "common/index.html")


def create_league(request):

    return render(request, "leagues/create-league.html")


def login(request):

    return render(request, "logins/login.html")


def logout(request):

    return render(request, "logins/logout.html")


def register(request):

    return render(request, "logins/register.html")


def create_player(request):

    return render(request, "players/create-player.html")


def delete_player(request, pk):

    return render(request, "players/delete-player.html")


def edit_player(request, pk):

    return render(request, "players/edit-player.html")


def player_details(request, pk):

    return render(request, "players/player_details.html")


def edit_profile(request):

    return render(request, "profile/edit-profile.html")


def profile_details(request):

    return render(request, "profile/profile-details.html")

def create_team(request):

    return render(request, "teams/create_team.html")