from django import template

register = template.Library()


@register.filter(name="urls")
def urls(value):
    return str("/news/detail/" + str(value) + "/")


@register.filter(name="limit5")
def limit5(value):
    return value[:5]


@register.filter(name="categaryURL")
def categoryURL(value):
    return value.categary.url

@register.filter(name="categaryCate")
def categoryURL(value):
    return value.categary.categary

