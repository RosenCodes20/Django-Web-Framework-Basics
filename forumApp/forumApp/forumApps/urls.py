from django.urls import path

from forumApp.forumApps import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dash/", views.dashboard, name="dash"),
    path("post-details/<int:pk>/", views.details, name="details")
]