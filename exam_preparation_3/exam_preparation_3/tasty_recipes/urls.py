from django.urls import path, include

from exam_preparation_3.tasty_recipes import views

urlpatterns = [
    path("", views.index, name="index"),

    path("recipe/", include([
        path("catalogue/", views.catalogue, name="catalogue"),
        path("create/", views.create_recipe, name="create-recipe"),
        path("<int:pk>/details/", views.recipe_details, name="recipe-details"),
        path("<int:pk>/edit/", views.edit_recipe, name="edit-recipe"),
        path("<int:pk>/delete/", views.delete_recipe, name="delete-recipe"),
    ])),

    path("profile/", include([
        path("create/", views.create_profile, name="create-profile"),
        path("details/", views.profile_details, name="profile-details"),
        path("edit/", views.edit_profile, name="edit-profile"),
        path("delete/", views.delete_profile, name="delete-profile"),
    ]))
]