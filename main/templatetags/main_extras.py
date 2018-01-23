from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag(takes_context=True)
def current(context, url_name, **kwargs):
    x = resolve(context.get('request').path)
    if (x.app_name + ':' + x.url_name) == url_name:
        return 'active'
    else:
        return ''
 
