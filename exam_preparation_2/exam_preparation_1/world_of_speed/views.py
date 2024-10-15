from django.shortcuts import render


def index(request):

    return render(request, "index.html")


def catalogue(request):

    return render(request, "catalogue.html")


def create_car(request):

    return render(request, "car-create.html")


def delete_car(request, pk):

    return render(request, "car-delete.html")


def car_details(request, pk):

    return render(request, "car-details.html")


def edit_car(request, pk):

    return render(request, "car-edit.html")


def create_profile(request):

    return render(request, "profile-create.html")


def delete_profile(request):

    return render(request, "profile-delete.html")


def profile_details(request):

    return render(request, "profile-details.html")


def edit_profile(request):

    return render(request, "profile-edit.html")