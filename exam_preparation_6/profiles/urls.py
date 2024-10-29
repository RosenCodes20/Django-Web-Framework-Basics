from django.urls import path, include

from profiles.views import CreateProfile, ProfileDetails, EditProfile, DeleteProfile

urlpatterns = [
    path("profile/", include([
        path("create/", CreateProfile.as_view(), name="create-profile"),
        path("details/", ProfileDetails.as_view(), name="profile-details"),
        path("edit/", EditProfile.as_view(), name="edit-profile"),
        path("delete/", DeleteProfile.as_view(), name="delete-profile")
    ]))
]