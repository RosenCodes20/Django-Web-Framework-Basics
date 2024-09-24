from datetime import datetime
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.context_processors import request


def index(request):
    context = {
        "users": [
            "ivan",
            "pesho",
            "gosho",
            "rosen"
        ],
        "admin": {
            "name": "Rosen",
            "age": 16,
            "color": "brown"
        }
    }

    return render(request, "base.html", context)


def dashboard(request):

    context = {
        "posts": [
                {
                "title": "What is the new capital of Bulgaria",
                "author": "Rosen Ivanov",
                "content": "The new capital of Bulgaria is Mezdra",
                "post_date": datetime.today(),
                "index": 1
            },
            {
                "title": "What is the new capital of Germany",
                "author": "Ivan Genchev",
                "content": "The new capital of Germany is Munich",
                "post_date": datetime.today(),
                "index": 2
            },
        ]
    }

    return render(request, "posts/dashboards.html", context)


def details(request, pk):

    curr_post = None

    posts = {"posts": [
            {
            "title": "What is the new capital of Bulgaria",
            "author": "Rosen Ivanov",
            "content": "The new capital of Bulgaria is Mezdra",
            "post_date": datetime.today(),
            "index": 1
        },
            {
                "title": "What is the new capital of Germany",
                "author": "Ivan Genchev",
                "content": "The new capital of Germany is Munich",
                "post_date": datetime.today(),
                "index": 2
            },
        ]
    }

    for posts in posts.values():
        for post in posts:
            if post["index"] == pk:
                curr_post = post

    context = {
        "post": curr_post
    }

    return render(request, "posts/post-details.html", context)
