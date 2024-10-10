from django.shortcuts import render

from djangoProject1.todo_app.models import TodoApp


def search_bar(request):

    get_todo_filter = request.GET.get("todo_filter", "")

    all_todos = TodoApp.objects.filter(name__icontains=get_todo_filter)

    context = {
        "todos": all_todos,
        "get_todo_filter": get_todo_filter
    }

    return render(request, "search.html", context)