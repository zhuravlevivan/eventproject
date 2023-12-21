from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddEventForm
from .models import Event


def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'event/list.html', context)


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event': event
    }
    return render(request, 'event/detail.html', context)


def event_add(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'event/list.html', context=context)
    else:
        form = AddEventForm()
    context = {
        'title': 'Добавить событие',
        'form': form,
    }
    return render(request, 'event/add.html', context=context)
