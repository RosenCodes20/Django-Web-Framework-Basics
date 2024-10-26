from django.shortcuts import render, redirect

from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile


def create_profile(request):

    form = CreateProfileForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "form": form
    }

    return render(request, "create-profile.html", context)


def profile_details(request):

    profile = Profile.objects.last()

    context = {
        "profile": profile
    }

    return render(request, "details-profile.html", context)


def edit_profile(request):
    profile = Profile.objects.last()

    form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile-details")

    context = {
        "form": form
    }

    return render(request, "edit-profile.html", context)


def delete_profile(request):

    profile = Profile.objects.last()

    if request.method == "POST":
        profile.delete()
        return redirect("index")

    return render(request, "delete-profile.html",)