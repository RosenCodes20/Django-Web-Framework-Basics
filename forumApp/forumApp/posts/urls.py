from django.urls import path

from forumApp.posts import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dash/", views.dashboard, name="dash"),
    path("post-details/<int:pk>/", views.details, name="details"),
    path("create-post/", views.create_post, name="create-post"),
    path("edit-post/<int:pk>/", views.edit_post, name="edit-post"),
    path("delete-post/<int:pk>", views.delete_post, name="delete-post")
]