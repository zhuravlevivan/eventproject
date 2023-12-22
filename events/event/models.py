from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
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
