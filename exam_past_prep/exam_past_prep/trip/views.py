from django.shortcuts import render, redirect

from exam_past_prep.traveler.models import Traveler
from exam_past_prep.trip.forms import CreateTrip, EditTrip, DeleteTrip
from exam_past_prep.trip.models import Trip


def create(request):
    form = CreateTrip(request.POST or None)
    traveleres = Traveler.objects.first()
    travelers = Traveler.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data:
                trip = form.save(commit=False)
                trip.traveler = traveleres
                trip.save()
                return redirect('all-trips')

    context = {
        'form': form,
        'traveleres': travelers,
        'travelers': travelers
    }

    return render(request, 'create-trip.html', context)

def trip_details(request, pk):
    trip = Trip.objects.get(id=pk)
    travelers = Traveler.objects.all()

    context = {
        'trip': trip,
        'travelers': travelers
    }

    return render(request, 'details-trip.html', context)

def trip_edit(request, pk):
    trip = Trip.objects.get(id=pk)
    travelers = Traveler.objects.all()
    form = EditTrip(request.POST or None, instance=trip)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all-trips')

    context = {
        'trip': trip,
        'form': form,
        'travelers': travelers
    }
    return render(request, 'edit-trip.html', context)

def trip_delete(request, pk):
    trip = Trip.objects.get(id=pk)
    travelers = Traveler.objects.all()
    form = DeleteTrip(request.POST or None, instance=trip)

    if request.method == 'POST':
        if form.is_valid():
            trip.delete()
            return redirect('all-trips')

    context = {
        'trip': trip,
        'form': form,
        'travelers': travelers
    }
    return render(request, 'delete-trip.html', context)