from django.urls import path

from djangoProject1.todo_app import views

urlpatterns = [
    path("", views.search_bar)
]