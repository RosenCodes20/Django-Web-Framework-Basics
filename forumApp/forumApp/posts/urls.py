from django.urls import path

from forumApp.posts import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("dash/", views.Dashboard.as_view(), name="dash"),
    path("post-details/<int:pk>/", views.details, name="details"),
    path("create-post/", views.CreatePost.as_view(), name="create-post"),
    path("edit-post/<int:pk>/", views.edit_post, name="edit-post"),
    path("delete-post/<int:pk>", views.delete_post, name="delete-post"),
    path("approve/<int:pk>/", views.approve_post, name="approve-post")
]