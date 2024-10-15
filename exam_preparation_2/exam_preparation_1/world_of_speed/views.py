from django.shortcuts import render, redirect

from exam_preparation_1.world_of_speed.forms import ProfileBaseForm, CreateCarBaseForm
from exam_preparation_1.world_of_speed.models import Profile


def index(request):

    profiles = Profile.objects.all()

    context = {
        "profiles": profiles
    }

    return render(request, "index.html", context)


def catalogue(request):

    return render(request, "catalogue.html")


def create_car(request):

    form = CreateCarBaseForm(request.POST or None)
    car_owner = Profile.objects.all().first()
    if request.method == "POST":
        if form.is_valid():
            if form.cleaned_data:
                car = form.save(commit=False)
                car.owner = car_owner
                car.save()
                return redirect("catalogue")


    context = {
        "form": form
    }

    return render(request, "car-create.html", context)


def delete_car(request, pk):

    return render(request, "car-delete.html")


def car_details(request, pk):

    return render(request, "car-details.html")


def edit_car(request, pk):

    return render(request, "car-edit.html")


def create_profile(request):

    form = ProfileBaseForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect("catalogue")


    context = {
        "form": form
    }

    return render(request, "profile-create.html", context)


def delete_profile(request):

    return render(request, "profile-delete.html")


def profile_details(request):

    return render(request, "profile-details.html")


def edit_profile(request):

    return render(request, "profile-edit.html")