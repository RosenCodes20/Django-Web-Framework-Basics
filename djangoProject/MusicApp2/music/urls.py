from django.contrib import admin
from django.urls import path, include

from MusicApp2.music import views

urlpatterns = [
    path("", views.base, name="index"),
    path("album/", include([
        path("create/", views.create_album, name="create album"),
        path("details/<int:id>", views.album_details, name="album details"),
        path("edit/<int:id>", views.edit_album, name="edit album"),
        path("delete/<int:id>", views.delete_album, name="delete album")
    ])),
    path("song/", include([
        path("create/", views.create_song, name="create song"),
        path("serve-song/<int:id>", views.serve_song, name="serve song"),
        path("play-song/<int:id>", views.play_song, name="play song")
    ]))
]