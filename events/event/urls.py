from django.urls import path

from . import views

app_name = 'event'
urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>', views.event_detail, name='event_detail'),
    path('events/add', views.event_add, name='event_add'),

]
