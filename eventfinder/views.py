from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Event, Venue, Category
from .forms import EventCreateForm, EventUpdateForm

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

class EventUpdate(UpdateView):
    model = Event
    template_name = 'eventfinder/event_update.html'
    form_class = EventUpdateForm

class EventDelete(DeleteView):
    model = Event
    template_name = 'eventfinder/event_delete.html'
    success_url = reverse_lazy('eventfinder:index')

class VenueDetail(DetailView):
    model = Venue
    context_object_name = 'venue'
