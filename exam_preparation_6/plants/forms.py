from django import forms

from plants.models import Plant


class PlantBaseForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = "__all__"
        labels = {
            "plant_type": "Type:"
        }

class PlantForm(PlantBaseForm):
    pass


class EditPlantForm(PlantBaseForm):
    pass


class DeletePlantForm(PlantBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True