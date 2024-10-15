from django.urls import path, include

from exam_preparation_1.world_of_speed import views

urlpatterns = [
    path("", views.index, name="index"),
    path("car/", include([
        path("catalogue/", views.catalogue, name="catalogue"),
        path("<int:pk>/details/", views.car_details, name="car-details"),
        path("<int:pk>/edit/", views.edit_car, name="edit-car"),
        path("<int:pk>/delete/", views.delete_car, name="delete-car"),
    ])),

    path("profile/", include([
        path("create/", views.create_profile, name="create-profile"),
        path("details/", views.profile_details, name="details-profile"),
        path("edit/", views.edit_profile, name="edit-profile"),
        path("delete/", views.delete_profile, name="delete-profile"),
    ]))
]