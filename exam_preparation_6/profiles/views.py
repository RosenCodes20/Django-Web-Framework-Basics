from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from plants.models import Plant
from profiles.forms import ProfileBaseForm, ProfileForm, EditProfileForm
from profiles.models import Profile


class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "create-profile.html"
    success_url = reverse_lazy("catalogue")

class DeleteProfile(DeleteView):
    model = Profile
    template_name = "delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return Profile.objects.last()


class EditProfile(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "edit-profile.html"
    success_url = reverse_lazy("profile-details")

    def get_object(self, queryset=None):
        return Profile.objects.last()

class ProfileDetails(DetailView):
    model = Profile
    template_name = "profile-details.html"

    def get_object(self, queryset=None):
        return Profile.objects.last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plants"] = Plant.objects.all()
        return context