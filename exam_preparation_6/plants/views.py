from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from plants.forms import PlantForm, EditPlantForm, DeletePlantForm
from plants.models import Plant


class CreatePlant(CreateView):
    model = Plant
    form_class = PlantForm
    template_name = "create-plant.html"
    success_url = reverse_lazy("catalogue")

class DeletePlant(DeleteView, UpdateView):
    model = Plant
    form_class = DeletePlantForm
    template_name = "delete-plant.html"
    success_url = reverse_lazy("catalogue")

class EditPlant(UpdateView):
    model = Plant
    form_class = EditPlantForm
    template_name = "edit-plant.html"
    success_url = reverse_lazy("catalogue")


class PlantDetails(DetailView):
    model = Plant
    template_name = "plant-details.html"