from django import forms

from .models import Event
from ckeditor.fields import RichTextField


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class AddEventForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    date_time = forms.DateTimeField(widget=forms.SelectDateWidget, label='Дата')
    location = forms.CharField(max_length=100, label='Место')

    class Meta:
        model = Event
        fields = '__all__'
