from django import template

register = template.Library()

@register.inclusion_tag("user_info.html")

def user_info(user):

    if user.is_authenticated:

        return {
            "username": user.username
        }



    return {
        "username": "Anonymous"
    }