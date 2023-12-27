# from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .forms import AddEventForm
from .models import Event

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from events.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


class EventList(ListView):
    model = Event
    template_name = 'event/list.html'
    context_object_name = 'events'
    paginate_by = 2


class ShowEvent(DetailView):
    model = Event
    template_name = 'event/detail.html'


class AddEvent(CreateView):
    model = Event
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


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "event/email.html", {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
