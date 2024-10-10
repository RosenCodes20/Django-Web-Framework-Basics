from django.urls import path, include

from django_web_framework_ex.django_ex import views

urlpatterns = [
    path("", views.index, name="index"),
    path("league/", include([
        path("create-league/", views.create_league, name="create-league")
    ])),
    path("logins/", include([
        path("login/", views.login, name="login"),
        path("logout/", views.logout, name="logout"),
        path("register/", views.register, name="register"),
    ])),

    path("players/", include([
        path("create-player/", views.create_player, name="create-player"),
        path("delete-player/<int:pk>/", views.delete_player, name="delete-player"),
        path("edit-player/<int:pk>/", views.edit_player, name="edit-player"),
        path("player-details/<int:pk>/", views.player_details, name="player-details"),
    ])),

    path("profile/", include([
        path("edit-profile", views.edit_profile, name="edit-profile"),
        path("profile-details", views.profile_details, name="profile-details")
    ])),

    path("teams/", include([
        path("create-team/", views.create_team, name="create-team")
    ]))
]