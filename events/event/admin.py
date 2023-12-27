from django.contrib import admin

from django import forms
from .models import Event

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_time', 'location')
    list_display_links = ('title',)
    form = EventAdminForm
