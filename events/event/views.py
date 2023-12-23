from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .forms import AddEventForm
from .models import Event


# def event_list(request):
#     events = Event.objects.all()
#     context = {
#         'events': events
#     }
#     return render(request, 'event/list.html', context)


# def event_detail(request, id):
#     event = get_object_or_404(Event, id=id)
#     context = {
#         'event': event
#     }
#     return render(request, 'event/detail.html', context)
class EventList(ListView):
    model = Event
    template_name = 'event/list.html'
    context_object_name = 'events'
    paginate_by = 2


class ShowEvent(DetailView):
    model = Event
    template_name = 'event/detail.html'

# def event_add(request):
#     events = Event.objects.all()
#     context = {
#         'events': events
#     }
#     if request.method == 'POST':
#         form = AddEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'event/list.html', context=context)
#     else:
#         form = AddEventForm()
#     context = {
#         'title': 'Добавить событие',
#         'form': form,
#     }
#     return render(request, 'event/add.html', context=context)


class AddEvent(CreateView):
    form_class = AddEventForm
    template_name = 'event/add.html'
    success_url = reverse_lazy('event:event_list')


class UpdateEvent(UpdateView):
    model = Event
    fields = '__all__'
    template_name = 'event/edit.html'
    success_url = reverse_lazy('event:event_list')


class DeleteEvent(DeleteView):
    model = Event
    template_name = 'event/delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('event:event_list')


