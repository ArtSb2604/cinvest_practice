import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    Activity = models.BooleanField(verbose_name='Активировать/Деактивировать пользователя', default=False)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100)
    birthdate = models.DateField(verbose_name='Дата рождения', max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name='Город', max_length=100)
    number_phone = models.CharField(verbose_name='Телефон', max_length=100)
    social_contact = models.CharField(verbose_name='Контакт для оперативной связи (Телеграм, VK или что-то ещё)',
                                      max_length=100)
    course = models.CharField(verbose_name='Укажите вашу ступень обучения', max_length=100)
    university = models.CharField(verbose_name='Расскажите, какого университета', max_length=100)
    department = models.CharField(verbose_name='Кафедра', max_length=100)
    specialization = models.CharField(verbose_name='Специальность', max_length=100)
    year_graduation = models.CharField(verbose_name='Укажите год окончания', max_length=100)
    average_score = models.CharField(verbose_name='Укажите ваш средний балл в вузе', max_length=100)
    educational_interests = models.CharField(verbose_name='Расскажите о своих учебных интересах:', max_length=100)
    what_tasks = models.CharField(
        verbose_name='Опишите, какими задачами вам было бы интересно заниматься во время стажировки', max_length=100)
    achievements = models.CharField(verbose_name='Расскажите о своих достижениях', max_length=100)
    work_experience = models.CharField(
        verbose_name='Если у вас есть опыт работы/стажировки, расскажите об этом подробнее', max_length=100)
    find_out = models.CharField(verbose_name='Откуда вы узнали о стажировках в Банке Центр-Инвест', max_length=100)
    interested_internship = models.CharField(
        verbose_name='Почему вас заинтересовала стажировка в Банке Центр-Инвест, и чего вы от неё ждёте?',
        max_length=100)
    resume = models.FileField(verbose_name='Добавьте резюме', blank=True, null=True)
    categories = models.CharField(verbose_name='Направление', max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
