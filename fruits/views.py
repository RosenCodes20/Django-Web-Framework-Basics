from django.shortcuts import render, redirect

from fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruits.models import Fruit
from profiles.models import Profile


def create_fruit(request):

    form = CreateFruitForm(request.POST or None)

    profile = Profile.objects.last()

    if request.method == "POST":
        if form.is_valid():
            fruit = form.save(commit=False)

            fruit.owner = profile

            fruit.save()

            return redirect("dashboard")

    context = {
        "form": form
    }

    return render(request, "create-fruit.html", context)


def fruit_details(request, pk):

    fruit = Fruit.objects.get(id=pk)

    context = {
        "fruit": fruit
    }

    return render(request, "details-fruit.html", context)


def edit_fruit(request, pk):

    fruit = Fruit.objects.get(id=pk)

    form = EditFruitForm(request.POST or None, instance=fruit)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "fruit": fruit,
        "form": form
    }

    return render(request, "edit-fruit.html", context)


def delete_fruit(request, pk):

    fruit = Fruit.objects.get(id=pk)

    form = DeleteFruitForm(request.POST or None, instance=fruit)

    if request.method == "POST":
        fruit.delete()
        return redirect("dashboard")

    context = {
        "fruit": fruit,
        "form": form
    }

    return render(request, "delete-fruit.html", context)

