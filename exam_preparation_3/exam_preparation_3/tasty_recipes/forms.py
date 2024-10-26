from django import forms

from exam_preparation_3.tasty_recipes.models import Profile, Recipe


class BaseProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("nickname", "first_name", "last_name", "chef")


class BaseRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ("title", "cuisine_type", "ingredients", "instructions", "cooking_time", "image_url")

        error_messages = {
            "title": {
                "unique": "We already have a recipe with the same title!"
            }
        }


class EditRecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(BaseRecipeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class EditProfileBaseForm(BaseProfileForm):

    class Meta:
        model = Profile
        fields = "__all__"