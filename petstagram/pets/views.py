from django.shortcuts import render

def add_page(request):

    return render(request, "pets/pet-add-page.html")


def delete_page(request, username, pets_slug):

    return render(request, "pets/pet-delete-page.html")


def details_page(request, username, pets_slug):

    return render(request, "pets/pet-details-page.html")


def edit_page(request, username, pets_slug):

    return render(request, "pets/pet-edit-page.html")
