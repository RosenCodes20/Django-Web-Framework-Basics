from django import forms
from django.forms import DateInput

from exam_past_prep.trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        fields = ('destination', 'summary', 'start_date', 'duration', 'image_url')
        model = Trip
        widgets = {
            'destination': forms.TextInput(attrs={'placeholder': "Enter a short destination note..."}),
            'summary': forms.TextInput(attrs={'placeholder': "Share your exciting moments... "}),
            'image_url': forms.TextInput(attrs={'placeholder': "An optional image URL..."}),
            'start_date': DateInput(attrs={'type': 'date'})}

        labels = {
            'destination': 'Destination:',
            'summary': 'Summary:',
            'start_date': 'Started on:',
            'duration': 'Duration:',
            'image_url': 'Image URL:'
        }

class CreateTrip(TripBaseForm):
    pass

class EditTrip(TripBaseForm):
    pass

class DeleteTrip(TripBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = "readonly"