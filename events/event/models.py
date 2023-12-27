from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    # description = models.TextField(verbose_name='Описание')
    description = CKEditor5Field('Содержимое', config_name='extends')
    date_time = models.DateTimeField(verbose_name='Дата')
    location = models.CharField(max_length=100, verbose_name='Место')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-date_time']
        indexes = [
            models.Index(fields=['-date_time'])
        ]

    def get_absolute_url(self):
        return reverse('event:event_detail', kwargs={'event_detail_id': self.id})

