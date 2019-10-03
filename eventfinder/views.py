from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Event


def index(request):
    upcoming_event_list = Event.objects.order_by('-start_time')[:5]
    context = {'upcoming_event_list': upcoming_event_list}
    return render(request, 'eventfinder/index.html', context)

class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'