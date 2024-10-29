from django.template import Library

from profiles.models import Profile

register = Library()

@register.simple_tag
def get_profiles():
    return Profile.objects.all()