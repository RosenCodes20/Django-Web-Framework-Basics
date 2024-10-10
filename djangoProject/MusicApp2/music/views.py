from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect

from MusicApp2.music.forms import BaseAlbumForm, BaseSongForm, EditAlbumBaseForm, DeleteAlbumBaseForm
from MusicApp2.music.models import Album, Song


def base(request):

    albums = Album.objects.all()

    context = {
        "albums": albums
    }

    return render(request, "common/index.html", context)


def album_details(request, id):

    album = Album.objects.get(id=id)

    context = {
        "album": album
    }

    return render(request, "albums/album-details.html", context)


def create_album(request):
    albums = Album.objects.all()

    if request.method == "GET":
        form = BaseAlbumForm()

    elif request.method == "POST":
        form = BaseAlbumForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "albums": albums,
        "form": form
    }

    return render(request, "albums/create-album.html", context)


def delete_album(request, id):

    album = Album.objects.get(id=id)

    if request.method == "GET":
        form = DeleteAlbumBaseForm(instance=album)

    else:
        form = DeleteAlbumBaseForm(request.POST, instance=album)
        album.delete()
        return redirect("index")

    context = {
        "album": album,
        "form": form
    }

    return render(request, "albums/delete-album.html", context)


def edit_album(request, id):

    album = Album.objects.get(id=id)

    if request.method == "GET":
        form = EditAlbumBaseForm(instance=album)

    else:
        form = EditAlbumBaseForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "album": album,
        "form": form
    }

    return render(request, "albums/edit-album.html", context)


def create_song(request):

    songs = Song.objects.all()

    if request.method == "GET":
        form = BaseSongForm()

    elif request.method == "POST":
        form = BaseSongForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "songs": songs,
        "form": form
    }

    return render(request, "songs/create-song.html", context)


def play_song(request, id):

    song = Song.objects.get(id=id)

    context = {
        "song": song
    }

    return render(request, "songs/music_player.html", context)


def serve_song(request, id):
    song = Song.objects.get(id=id)

    if song:
        response = HttpResponse(song.music_file_data, content_type="audio/mpeg")
        response["Content-Disposition"] = f'inline; filename="{song.song_name}"'
        return response
    else:
        return HttpResponse('Song not found', status=404)