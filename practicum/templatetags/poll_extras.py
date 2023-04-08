import json
from django import template

from practicum.models import Article

register = template.Library()

@register.filter
def back(value):
    if int(value)-1 != 0:
        return f'/practicum/article/{int(value)-1}/'
    else:
        return ''

@register.filter
def next(value):
    article = Article.objects.last()
    if int(value)+1 > article.pk:
        return ''
    else:
        return f'/practicum/article/{int(value)+1}/'
