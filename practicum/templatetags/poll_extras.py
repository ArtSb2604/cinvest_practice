import json
from django import template

from practicum.models import Article, Quiz

register = template.Library()

@register.filter
def back(value):
    if int(value)-1 != 0:
        return f'/practicum/article/{int(value)-1}/'
    else:
        return ''

@register.filter
def next(value):
    article = Article.objects.get(pk=int(value))
    article1 = Article.objects.get(pk=int(value)+1)
    quiz = Quiz.objects.get(article=article.cat)
    if article.cat == article1.cat:
        if int(value) + 1 > article1.pk:
            return quiz.pk
        else:
            return f'/practicum/article/{int(value) + 1}/'
    else:
        return ''
