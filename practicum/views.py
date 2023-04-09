from random import randrange

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from internship.models import DirectionsDesc
from practicum.models import Article, Quiz, Result


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article/articles.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['cat'] = DirectionsDesc.objects.all()
        return context

class ArticleDetail(DetailView):
    model = Article
    template_name = "article/detail.html"
    context_object_name = 'article'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['quiz'] = Quiz.objects.get(article=article.cat)
        return context


class QuizDetail(DetailView):
    model = Quiz
    template_name = "article/quiz-detail.html"
    context_object_name = 'quiz'

    def post(self, request, *args, **kwargs):
        Result(user=request.user.pk, result_ball=randrange(6), max_ball=5).save()
        return render(request, "article/result.html")

