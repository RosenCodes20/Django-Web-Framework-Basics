from datetime import datetime

from django.shortcuts import render, redirect

from forumApp.posts.forms import BasePostForm, PostEditForm, PostDeleteForm, SearchBarForm, CommentFormSet
from forumApp.posts.models import Post


def index(request):
    context = {
        "today_date": datetime.today
    }

    return render(request, "base.html", context)


def dashboard(request):
    form = SearchBarForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            cleaned_post = form.cleaned_data["post"]
            posts = Post.objects.filter(title__icontains=cleaned_post)


    context = {
        "posts": posts,
        "form": form
    }

    return render(request, "posts/dashboards.html", context)


def create_post(request):

    form = BasePostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dash")

    context = {
        "form": form
    }

    return render(request, "posts/create-post.html", context)


def details(request, pk):

    post = Post.objects.get(id=pk)

    if request.method == "GET":
        comment_formset = CommentFormSet()

    else:
        comment_formset = CommentFormSet(request.POST)

        if comment_formset.is_valid():
            for form in comment_formset:
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect("dash")

    context = {
        "post": post,
        "form": comment_formset
    }

    return render(request, "posts/post-details.html", context)


def edit_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "GET":
        form = PostEditForm(instance=post)

    else:
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("dash")

    context = {
        "form": form,
        "post": post
    }

    return render(request, "posts/edit-post.html", context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "GET":
        form = PostDeleteForm(instance=post)

    else:
        form = PostDeleteForm(request.POST, instance=post)

        post.delete()

        return redirect("dash")

    context = {
        "post": post,
        "form": form
    }

    return render(request, "posts/delete-post.html", context)