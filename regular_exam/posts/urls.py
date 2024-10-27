from django.urls import path, include

from posts import views

urlpatterns = [
    path("posts/", include([
        path("create/", views.create_post, name="create-post"),
        path("<int:pk>/details/", views.post_details, name="post-details"),
        path("<int:pk>/edit/", views.edit_post, name="edit-post"),
        path("<int:pk>/delete/", views.delete_post, name="delete-post")
    ]))
]