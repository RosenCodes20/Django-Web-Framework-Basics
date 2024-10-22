from django.shortcuts import render, redirect

from profiles.models import Profile


def delete_profile(request):

    profile = Profile.objects.last()

    if request.method == "POST":
        profile.delete()
        return redirect("index")

    return render(request, "profile-delete.html")


def profile_details(request):

    profile = Profile.objects.last()

    context = {
        "profile": profile
    }

    return render(request, "profile-details.html", context)