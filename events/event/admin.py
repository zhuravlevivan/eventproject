from django.contrib import admin

from django import forms
from .models import Event


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_time', 'location')
    list_display_links = ('title',)
    form = EventAdminForm
