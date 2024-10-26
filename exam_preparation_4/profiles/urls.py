from django.urls import path, include

from profiles import views

urlpatterns = [
    path("profile/", include([
        path("details/", views.profile_details, name="profile-details"),
        path("delete/", views.delete_profile, name="profile-delete")
    ]))
]