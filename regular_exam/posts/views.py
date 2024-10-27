from django.shortcuts import render, redirect

from authors.models import Author
from posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from posts.models import Post


def create_post(request):

    form = CreatePostForm(request.POST or None)

    author = Author.objects.last()

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)

            post.author = author

            post.save()

            return redirect("dashboard")

    context = {
        "form": form
    }

    return render(request, "posts/create-post.html", context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    form = DeletePostForm(request.POST or None, instance=post)

    if request.method == "POST":
        post.delete()
        return redirect("dashboard")

    context = {
        "post": post,
        "form": form
    }

    return render(request, "posts/delete-post.html", context)


def post_details(request, pk):

    post = Post.objects.get(id=pk)

    context = {
        "post": post
    }

    return render(request, "posts/details-post.html", context)

def edit_post(request, pk):
    post = Post.objects.get(id=pk)

    form = EditPostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "post": post,
        "form": form
    }

    return render(request, "posts/edit-post.html", context)