from django import template
register=template.Library()

@register.simple_tag(name='multy')
def multy(a,b):
    return a*b