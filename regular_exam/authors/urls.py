from django.urls import path, include

from authors import views

urlpatterns = [
    path("author/", include([
        path("create/", views.create_author, name="create-author"),
        path("details/", views.author_details, name="author-details"),
        path("edit/", views.edit_author, name="edit-author"),
        path("delete/", views.delete_author, name="delete-author")
    ]))
]