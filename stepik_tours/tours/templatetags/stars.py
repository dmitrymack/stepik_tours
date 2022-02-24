from django import template

register = template.Library()

@register.filter()
def stars(value):
    return int(value) * "★"