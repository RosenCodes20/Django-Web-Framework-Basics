from django.shortcuts import render, redirect

from albums.models import Album
from common.forms import CreateProfileForm
from profiles.models import Profile


def index(request):
    profiles = Profile.objects.all()

    form = CreateProfileForm(request.POST or None)

    albums = Album.objects.all()

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")


    if profiles:

        context = {
            "albums": albums
        }

        return render(request, "home-with-profile.html", context)

    else:

        context = {
            "form": form
        }

        return render(request, "home-no-profile.html", context)