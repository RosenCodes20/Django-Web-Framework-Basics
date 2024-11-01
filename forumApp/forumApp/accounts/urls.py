from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from forumApp.accounts.views import RegisterUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]