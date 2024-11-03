from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, ListView, DetailView

from forumApp.posts.forms import BasePostForm, PostEditForm, PostDeleteForm, SearchBarForm, CommentFormSet
from forumApp.posts.models import Post


# def index(request):
#     context = {
#         "today_date": datetime.today
#     }
#
#     return render(request, "base.html", context)

class Index(TemplateView):
    template_name = "base.html"


class Dashboard(ListView, FormView):
    model = Post
    form_class = SearchBarForm
    success_url = reverse_lazy("dash")
    context_object_name = "posts"
    template_name = "posts/dashboards.html"
    paginate_by = 2

    def get_queryset(self):

        queryset = self.model.objects.all()

        if not self.request.user.has_perm("posts.can_approve_posts"):
            queryset =queryset.filter(approved=True)

        if "post" in self.request.GET:
            post = self.request.GET.get("post")
            queryset = queryset.filter(title__icontains=post)

        return queryset


# TODO: SHOULD FINISH WITH APPROVED BY GIVING THE APPROVED SIGN SO REDACTOR CAN APPROVE IT!!!!!!!!!!!!!!

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


# def create_post(request):
#
#     form = BasePostForm(request.POST or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("dash")
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "posts/create-post.html", context)


class CreatePost(CreateView):
    model = Post
    template_name = "posts/create-post.html"
    form_class = BasePostForm
    success_url = reverse_lazy("dash")


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

            return redirect("details", pk=post.id)

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
