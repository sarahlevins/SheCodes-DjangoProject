from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Event, Venue, Category
from .forms import EventCreateForm

def index(request):
    upcoming_event_list = Event.objects.order_by('-start_time')[:5]
    context = {'upcoming_event_list': upcoming_event_list}
    return render(request, 'eventfinder/index.html', context)

class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

class EventCreate(CreateView):
    model = Event
    template_name = 'eventfinder/event_create.html'
    form_class = EventCreateForm

    def form_valid(self, form):
        form.instance.host = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)

class VenueDetail(DetailView):
    model = Venue
    context_object_name = 'venue'
