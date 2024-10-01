from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path("add/", views.add_page, name="add-page"),
    path("<str:username>/pet/<slug:pets_slug>/", include([
        path("", views.details_page, name="details-page"),
        path("edit/", views.edit_page, name="edit-page"),
        path("delete/", views.delete_page, name="delete-page")
    ])),

]