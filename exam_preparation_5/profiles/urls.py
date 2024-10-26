from django.urls import path, include

from profiles import views

urlpatterns = [
    path("profile/", include([
        path("details/", views.profile_details, name="profile-details"),
        path("create/", views.create_profile, name="create-profile"),
        path("edit/", views.edit_profile, name="edit-profile"),
        path("delete/", views.delete_profile, name="delete-profile")
    ]))
]