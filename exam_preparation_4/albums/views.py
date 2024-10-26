from django.shortcuts import render, redirect

from albums.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album
from profiles.models import Profile


def add_album(request):

    form = AlbumAddForm(request.POST or None)

    profile = Profile.objects.last()

    if request.method == "POST":
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = profile
            album.save()
            return redirect("index")

    context = {
        "form": form
    }

    return render(request, "album-add.html", context)


def delete_album(request, pk):

    album = Album.objects.get(id=pk)

    form = AlbumDeleteForm(request.POST or None, instance=album)

    if request.method == "POST":
        album.delete()
        return redirect("index")

    context = {
        "album": album,
        "form": form
    }

    return render(request, "album-delete.html", context)


def album_details(request, pk):

    album = Album.objects.get(id=pk)

    context = {
        "album": album
    }

    return render(request, "album-details.html", context)


def album_edit(request, pk):
    album = Album.objects.get(id=pk)

    form = AlbumEditForm(request.POST or None, instance=album)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "album": album,
        "form": form
    }

    return render(request, "album-edit.html", context)