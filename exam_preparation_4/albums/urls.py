from django.urls import path, include

from albums import views

urlpatterns = [
    path("album/", include([
        path("add/", views.add_album, name="add-album"),
        path("<int:pk>/details/", views.album_details, name="album-details"),
        path("<int:pk>/edit/", views.album_edit, name="edit-album"),
        path("<int:pk>/delete/", views.delete_album, name="delete-album")
    ]))
]