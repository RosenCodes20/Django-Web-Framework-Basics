from django import template

from profiles.models import Profile

register = template.Library()

@register.simple_tag
def get_profiles():
    return Profile.objects.all()