import urllib.parse
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def query_param_add(context, key, value):
    """
    Extends the query string with a new key-value pair.
    """
    request = context['request']
    dict_ = request.GET.copy()
    dict_[key] = value
    return "?" + urllib.parse.urlencode(dict_)