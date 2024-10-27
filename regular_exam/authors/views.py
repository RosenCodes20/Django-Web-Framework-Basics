from cProfile import Profile

from django.shortcuts import render, redirect

from authors.forms import CreateAuthorForm, EditAuthorForm
from authors.models import Author


def create_author(request):
    form = CreateAuthorForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "form": form
    }

    return render(request, "authors/create-author.html", context)


def delete_author(request):

    author = Author.objects.last()

    if request.method == "POST":
        author.delete()
        return redirect("index")

    return render(request, "authors/delete-author.html")


def author_details(request):

    author = Author.objects.last()
    last_updated_post = author.posts.order_by("-updated_at").first()

    context = {
        "author": author,
        "last_updated_post": last_updated_post
    }

    return render(request, "authors/details-author.html", context)


def edit_author(request):

    author = Author.objects.last()

    form = EditAuthorForm(request.POST or None, instance=author)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("author-details")

    context = {
        "author": author,
        "form": form
    }

    return render(request, "authors/edit-author.html", context)