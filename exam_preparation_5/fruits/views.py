from django.shortcuts import render


def create_fruit(request):

    return render(request, "create-fruit.html")


def fruit_details(request, pk):

    return render(request, "details-fruit.html")


def edit_fruit(request, pk):

    return render(request, "edit-fruit.html")


def delete_fruit(request, pk):

    return render(request, "delete-fruit.html")

