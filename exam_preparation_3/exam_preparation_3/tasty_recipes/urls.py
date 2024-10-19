from django.urls import path

from exam_preparation_3.tasty_recipes import views

urlpatterns = [
    path("", views.index, name="index")
]