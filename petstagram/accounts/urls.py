from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path("register/", views.register, name="accounts-register"),
    path("login/", views.login, name="accounts-login"),
    path("profile/<int:pk>/", include([
        path("", views.profile_details, name="profile-details"),
        path("edit/", views.edit_profile, name="edit-profile"),
        path("delete/", views.profile_delete, name="delete-profile"),
    ]))
]