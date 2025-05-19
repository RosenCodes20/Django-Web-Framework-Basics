from django.template import Library

from exam_past_prep.traveler.models import Traveler

register = Library()

@register.simple_tag
def get_travelers():
    return Traveler.objects.all()