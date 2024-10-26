from django import forms
from django.forms import TextInput

from fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):

    class Meta:
        model = Fruit
        fields = "__all__"


class CreateFruitForm(FruitBaseForm):

    class Meta(FruitBaseForm.Meta):
        widgets = {
            "name": TextInput(attrs={"placeholder": "Fruit Name"}),
            "image_url": TextInput(attrs={"placeholder": "Fruit Image URL"}),
            "description": TextInput(attrs={"placeholder": "Fruit Description"}),
            "nutrition": TextInput(attrs={"placeholder": "Nutrition Info"}),
        }

        labels = {
            "first_name": "",
            "image_url": "",
            "description": "",
            "nutrition": ""
        }


class EditFruitForm(FruitBaseForm):
    pass


class DeleteFruitForm(FruitBaseForm):

    class Meta(FruitBaseForm.Meta):
        fields = ("name", "image_url", "description")
    

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
            
        for field in self.fields:
            self.fields[field].disabled = True

