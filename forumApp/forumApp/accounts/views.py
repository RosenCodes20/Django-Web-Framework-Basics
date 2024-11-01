from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forumApp.accounts.forms import RegisterBaseForm


class RegisterUserView(CreateView):
    form_class = RegisterBaseForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("index")
