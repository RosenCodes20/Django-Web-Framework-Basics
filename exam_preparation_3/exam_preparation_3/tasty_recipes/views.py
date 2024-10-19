from django.shortcuts import render


def index(request):

    return render(request, "home-page.html")


def catalogue(request):

    return render(request, "catalogue.html")


def create_profile(request):

    return render(request, "create-profile.html")


def create_recipe(request):

    return render(request, "create-recipe.html")


def delete_profile(request):

    return render(request, "delete-profile.html")


def delete_recipe(request, pk):

    return render(request, "delete-recipe.html")


def profile_details(request):

    return render(request, "delete-profile.html")


def recipe_details(request, pk):

    return render(request, "details-recipe.html")


def edit_profile(request):

    return render(request, "edit-profile.html")


def edit_recipe(request, pk):

    return render(request, "edit-recipe.html")