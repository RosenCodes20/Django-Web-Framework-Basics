from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from plants.models import Plant


class Index(TemplateView):

    template_name = "home-page.html"


class Catalogue(ListView):
    model = Plant
    template_name = "catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plants"] = Plant.objects.all()
        return context