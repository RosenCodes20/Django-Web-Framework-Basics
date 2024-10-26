from django.shortcuts import render

from fruits.models import Fruit


def index(request):

    return render(request, "index.html")


def dashboard(request):

    fruits = Fruit.objects.all()

    context = {
        "fruits": fruits
    }

    return render(request, "dashboard.html", context)