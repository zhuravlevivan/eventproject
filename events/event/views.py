from django.shortcuts import render, get_object_or_404

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
