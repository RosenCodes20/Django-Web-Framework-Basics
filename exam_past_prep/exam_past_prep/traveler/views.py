from django.shortcuts import render, redirect

from exam_past_prep.traveler.forms import CreateTravelerForm
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

    return render(request, 'details-traveler.html')

def traveler_edit(request):
    return render(request, 'edit-traveler.html')

def traveler_delete(request):
    return render(request, 'delete-traveler.html')