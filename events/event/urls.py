from django.urls import path

from . import views


app_name = 'event'

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
    # path('events/<int:id>', views.event_detail, name='event_detail'),
    path('events/<int:pk>', views.ShowEvent.as_view(), name='event_detail'),
    path('events/add', views.AddEvent.as_view(), name='event_add'),
    path('edit/<int:pk>', views.UpdateEvent.as_view(), name='event_update'),
    path('delete/<int:pk>', views.DeleteEvent.as_view(), name='event_delete'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),


]
