from django.shortcuts import render, redirect

from exam_past_prep.traveler.forms import CreateTravelerForm, EditTraveler
from exam_past_prep.traveler.models import Traveler


def create_traveler(request):
    form = CreateTravelerForm(request.POST or None)
    travelers = Traveler.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all-trips')

    context = {
        'form': form,
        'travelers': travelers
    }

    return render(request, 'create-traveler.html', context)

def traveler_details(request):
    traveler = Traveler.objects.first()
    travelers = Traveler.objects.all()

    context = {
        'traveler': traveler,
        'travelers': travelers
    }

    return render(request, 'details-traveler.html', context)

def traveler_edit(request):
    traveler = Traveler.objects.first()
    travelers = Traveler.objects.all()
    form = EditTraveler(request.POST or None, instance=traveler)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details-traveler')

    context = {
        'form': form,
        'travelers': travelers
    }

    return render(request, 'edit-traveler.html', context)

def traveler_delete(request):
    travelers = Traveler.objects.all()
    traveler = Traveler.objects.last()

    if request.method == "POST":
        traveler.delete()
        return redirect('index')

    context = {
        'traveler': traveler,
        'travelers': travelers
    }

    return render(request, 'delete-traveler.html', context)