from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path("add/", views.add_page, name="ph-add-page"),
    path("<int:pk>/", include([
        path("", views.details_page, name="ph-details-page"),
        path("edit/", views.edit_page, name="ph-edit-page")
    ]))
]