from django.shortcuts import render

from exam_past_prep.traveler.models import Traveler
from exam_past_prep.trip.models import Trip


def index(request):
    travelers = Traveler.objects.all()

    context = {
        'travelers': travelers
    }

    return render(request, 'index.html', context)


def all_trips(request):
    travelers = Traveler.objects.all()
    trips = Trip.objects.all()
    context = {
        'travelers': travelers,
        'trips': trips
    }

    return render(request, 'all-trips.html', context)