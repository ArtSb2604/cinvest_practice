import random

from django.db import models

# Create your models here.
from internship.models import DirectionsDesc, Directions


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    cat = models.CharField(max_length=200, verbose_name='Категория')
    text = models.TextField(max_length=200000, verbose_name='Текст статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class Quiz(models.Model):
    name = models.CharField(max_length=120)
    article = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Result(models.Model):
    user = models.CharField(max_length=200)
    result_ball = models.CharField(max_length=200)
    max_ball = models.CharField(max_length=200)