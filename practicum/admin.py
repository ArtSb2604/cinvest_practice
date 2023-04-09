from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Answer, Question, Quiz, Result


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Article, ArticleAdmin)
class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Result)