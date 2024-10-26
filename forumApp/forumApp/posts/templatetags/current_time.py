from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag(name="current_time")
def curr_time(strf="%Y-%m-%d %H:%M:%S"):
    return datetime.today().strftime(strf)