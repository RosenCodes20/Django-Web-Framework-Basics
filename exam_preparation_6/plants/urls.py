from django.urls import path

from plants.views import CreatePlant, PlantDetails, EditPlant, DeletePlant

urlpatterns = [
    path("create/", CreatePlant.as_view(), name="create-plant"),
    path("details/<int:pk>/",  PlantDetails.as_view(), name="plant-details"),
    path("edit/<int:pk>/", EditPlant.as_view(), name="edit-plant"),
    path("delete/<int:pk>/", DeletePlant.as_view(), name="delete-plant")
]