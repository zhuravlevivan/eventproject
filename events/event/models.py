from django.db import models
from tinymce import models as tinymce_models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    # description = models.TextField(verbose_name='Описание')
    description = tinymce_models.HTMLField()

    date_time = models.DateTimeField(verbose_name='Дата')
    location = models.CharField(max_length=100, verbose_name='Место')
