from datetime import datetime

from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return f"{self.user} {self.room}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
