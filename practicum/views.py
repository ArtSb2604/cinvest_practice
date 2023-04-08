from django.shortcuts import render
from django.views.generic import ListView, DetailView

from practicum.models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article/articles.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = "article/detail.html"
    context_object_name = 'article'

