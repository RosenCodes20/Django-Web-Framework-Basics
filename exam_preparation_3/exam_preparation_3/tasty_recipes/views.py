from django.shortcuts import render, redirect

from exam_preparation_3.tasty_recipes.forms import BaseProfileForm, BaseRecipeForm, EditRecipeForm, DeleteRecipeForm, \
    EditProfileBaseForm
from exam_preparation_3.tasty_recipes.models import Profile, Recipe


def index(request):
    profiles = Profile.objects.all()

    context = {
        "profiles": profiles
    }

    return render(request, "home-page.html", context)


def catalogue(request):
    profiles = Profile.objects.all()

    recipes = Recipe.objects.all()

    context = {
        "profiles": profiles,
        "recipes": recipes
    }

    return render(request, "catalogue.html", context)


def create_profile(request):
    profiles = Profile.objects.all()

    form = BaseProfileForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form,
        "profiles": profiles
    }

    return render(request, "create-profile.html", context)


def create_recipe(request):
    profiles = Profile.objects.all()
    recipe_author = profiles.last()
    form = BaseRecipeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            recipe = form.save(commit=False)

            recipe.author = recipe_author

            recipe.save()
            return redirect("catalogue")

    context = {
        "profiles": profiles,
        "form": form
    }

    return render(request, "create-recipe.html", context)


def delete_profile(request):
    profiles = Profile.objects.all()

    profile = Profile.objects.last()

    if request.method == "POST":
        profile.delete()
        return redirect("index")


    context = {
        "profiles": profiles,
        "profile": profile
    }

    return render(request, "delete-profile.html", context)


def delete_recipe(request, pk):
    profiles = Profile.objects.all()

    recipe = Recipe.objects.get(id=pk)

    form = DeleteRecipeForm(request.POST or None, instance=recipe)

    if request.method == "POST":
        recipe.delete()
        return redirect("catalogue")

    context = {
        "profiles": profiles,
        "form": form,
        "recipe": recipe
    }

    return render(request, "delete-recipe.html", context)


def profile_details(request):
    profiles = Profile.objects.all()

    profile = Profile.objects.last()

    context = {
        "profiles": profiles,
        "profile": profile
    }

    return render(request, "details-profile.html", context)


def recipe_details(request, pk):
    profiles = Profile.objects.all()

    recipe = Recipe.objects.get(id=pk)

    ingredients = recipe.ingredients.split(", ")

    context = {
        "profiles": profiles,
        "recipe": recipe,
        "ingredients": ingredients
    }

    return render(request, "details-recipe.html", context)


def edit_profile(request):
    profiles = Profile.objects.all()

    profile = Profile.objects.last()

    form = EditProfileBaseForm(request.POST or None, instance=profile)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile-details")

    context = {
        "profiles": profiles,
        "profile": profile,
        "form": form
    }

    return render(request, "edit-profile.html", context)


def edit_recipe(request, pk):
    profiles = Profile.objects.all()

    recipe = Recipe.objects.get(id=pk)

    form = EditRecipeForm(request.POST or None, instance=recipe)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "profiles": profiles,
        "recipe": recipe,
        "form": form
    }

    return render(request, "edit-recipe.html", context)