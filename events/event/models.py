from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    date_time = models.DateTimeField(verbose_name='Дата')
    # time = models.TimeField()
    location = models.CharField(max_length=100, verbose_name='Место')
