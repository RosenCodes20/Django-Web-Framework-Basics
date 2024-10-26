from django.urls import path

from petstagram.common import views

urlpatterns = [
    path("", views.index, name="home-page")
]