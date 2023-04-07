from django.db import models

# Create your models here.
class Directions(models.Model):
    directions_name = models.CharField(max_length=200, verbose_name='Название направления')
    desc_lang_direct = models.CharField(max_length=200, verbose_name='Описание языков направления')
    city = models.CharField(max_length=200, verbose_name='Город')
    what_to_do = models.EmailField(max_length=200, verbose_name='Чем занимаются')
    desc_wtd = models.TextField(max_length=1000, verbose_name='Описание направления')

    def __str__(self):
        return self.directions_name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'