from django.shortcuts import render

from posts.models import Post


def index(request):

    return render(request, "common/index.html")


def dashboard(request):

    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "common/dashboard.html", context)