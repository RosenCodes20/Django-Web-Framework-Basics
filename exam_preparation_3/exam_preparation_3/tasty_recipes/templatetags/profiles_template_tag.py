from django import template

from exam_preparation_3.tasty_recipes.models import Profile

register = template.Library()

@register.simple_tag
def profiles_template_tag():
    return Profile.objects.all()