from django.template.defaulttags import register

@register.filter
def lookup(d, key):
    return d[key]