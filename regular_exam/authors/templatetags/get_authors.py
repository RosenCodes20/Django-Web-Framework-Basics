from django.template import Library

from authors.models import Author

register = Library()

@register.simple_tag
def get_authors():
    return Author.objects.all()