from django.shortcuts import render, redirect

from exam_past_prep.traveler.models import Traveler
from exam_past_prep.trip.forms import CreateTrip


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
    return render(request, 'details-trip.html')

def trip_edit(request, pk):
    return render(request, 'edit-trip.html')

def trip_delete(request, pk):
    return render(request, 'delete-trip.html')