from django.urls import path, include

from exam_preparation_1.world_of_speed import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("car/", include([
        path("catalogue/", views.Catalogue.as_view(), name="catalogue"),
        path("create/", views.CreateCar.as_view(), name="create-car"),
        path("<int:pk>/details/", views.CarDetails.as_view(), name="car-details"),
        path("<int:pk>/edit/", views.edit_car, name="edit-car"),
        path("<int:pk>/delete/", views.delete_car, name="delete-car"),
    ])),

    path("profile/", include([
        path("create/", views.CreateProfile.as_view(), name="create-profile"),
        path("details/", views.profile_details, name="details-profile"),
        path("edit/", views.edit_profile, name="edit-profile"),
        path("delete/", views.delete_profile, name="delete-profile"),
    ]))
]