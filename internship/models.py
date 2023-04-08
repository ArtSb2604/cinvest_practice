from django.db import models


class DirectionsDesc(models.Model):
    title = models.CharField(max_length=200, verbose_name='Описание')
    data_menu = models.CharField(max_length=200, verbose_name='data_menu')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направление'


class Directions(models.Model):
    directions_name = models.CharField(max_length=200, verbose_name='Название направления')
    data_menu = models.CharField(max_length=200, verbose_name='data_menu')

    def __str__(self):
        return self.directions_name

    class Meta:
        verbose_name = 'Описание направление'
        verbose_name_plural = 'Описание направление'


class TitleMain(models.Model):
    header = models.CharField(max_length=200, verbose_name='h1')
    main_title = models.TextField(verbose_name='div')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Информация на сайте'
        verbose_name_plural = 'Информация на сайте'
