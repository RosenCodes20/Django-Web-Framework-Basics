from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from exam_preparation_1.world_of_speed.forms import ProfileBaseForm, CreateCarBaseForm, EditCarForm, DeleteCarForm, \
    EditProfileForm
from exam_preparation_1.world_of_speed.models import Profile, Car


class Index(ListView):
    model = Profile
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["profiles"] = Profile.objects.all()

        return context

# def index(request):
#
#     profiles = Profile.objects.all()
#
#     context = {
#         "profiles": profiles
#     }
#
#     return render(request, "index.html", context)


class Catalogue(ListView):
    template_name = "catalogue.html"
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cars"] = Car.objects.all()
        context["profiles"] = Profile.objects.all()

        return context

# def catalogue(request):
#
#     cars = Car.objects.all()
#     profiles = Profile.objects.all()
#
#
#     context = {
#         "cars": cars,
#         "profiles": profiles
#     }
#
#     return render(request, "catalogue.html", context)


class CreateCar(CreateView):
    model = Car
    template_name = "car-create.html"
    form_class = CreateCarBaseForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        car_owner = Profile.objects.last()

        car = form.save(commit=False)
        car.owner = car_owner
        car.save()

        return super().form_valid(form)


# def create_car(request):
#     profiles = Profile.objects.all()
#
#     form = CreateCarBaseForm(request.POST or None)
#     car_owner = Profile.objects.all().last()
#     if request.method == "POST":
#         if form.is_valid():
#             if form.cleaned_data:
#                 car = form.save(commit=False)
#                 car.owner = car_owner
#                 car.save()
#                 return redirect("catalogue")
#
#
#     context = {
#         "form": form,
#         "profiles": profiles
#     }
#
#     return render(request, "car-create.html", context)


def delete_car(request, pk):

    car = Car.objects.get(id=pk)
    profiles = Profile.objects.all()

    form = DeleteCarForm(request.POST or None, instance=car)

    if request.method == "POST":

        car.delete()
        return redirect("catalogue")

    context = {
        "form": form,
        "car": car,
        "profiles": profiles

    }

    return render(request, "car-delete.html", context)


class CarDetails(DetailView):
    model = Car
    template_name = "car-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["car"] = Car.objects.get(id=context["car"].pk)
        context["profiles"] = Profile.objects.all()

        return context

# def car_details(request, pk):
#
#     car = Car.objects.get(id=pk)
#     profiles = Profile.objects.all()
#
#     context = {
#         "car": car,
#         "profiles": profiles
#     }
#
#     return render(request, "car-details.html", context)


def edit_car(request, pk):

    car = Car.objects.get(id=pk)
    profiles = Profile.objects.all()

    form = EditCarForm(request.POST or None, instance=car)

    if request.method == "POST":

        if form.is_valid():

            form.save()
            return redirect("catalogue")


    context = {
        "car": car,
        "form": form,
        "profiles": profiles

    }


    return render(request, "car-edit.html", context)


class CreateProfile(CreateView):

    model = Profile
    form_class = ProfileBaseForm
    template_name = "profile-create.html"

    def get_success_url(self):
        return reverse_lazy("catalogue")


# def create_profile(request):
#     profiles = Profile.objects.all()
#
#     form = ProfileBaseForm(request.POST or None)
#
#     if request.method == "POST":
#
#         if form.is_valid():
#             form.save()
#             return redirect("catalogue")
#
#
#     context = {
#         "form": form,
#         "profiles": profiles
#     }
#
#     return render(request, "profile-create.html", context)


def delete_profile(request):
    profile = Profile.objects.all().last()
    profiles = Profile.objects.all()

    if request.method == "POST":

        profile.delete()
        return redirect("index")

    context = {
        "profile": profile,
        "profiles": profiles

    }

    return render(request, "profile-delete.html", context)


def profile_details(request):

    profile = Profile.objects.all().last()
    profiles = Profile.objects.all()

    profiles_price = []

    for prof in profile.owners.all():
        profiles_price.append(prof.price)

    profiles_sum = sum(profiles_price)

    context = {
        "profile": profile,
        "profiles": profiles,
        "profiles_sum": profiles_sum
    }

    return render(request, "profile-details.html", context)


def edit_profile(request):

    profile = Profile.objects.all().last()
    profiles = Profile.objects.all()

    form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == "POST":

        if form.is_valid():

            form.save()
            return redirect("details-profile")


    context = {
        "profile": profile,
        "form": form,
        "profiles": profiles

    }

    return render(request, "profile-edit.html", context)