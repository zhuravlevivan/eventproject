from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    # description = models.TextField(verbose_name='Описание')
    description = CKEditor5Field('Text', config_name='extends')
    date_time = models.DateTimeField(verbose_name='Дата')
    location = models.CharField(max_length=100, verbose_name='Место')
