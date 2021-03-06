from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event, Venue, Category
from .forms import EventCreateForm, EventUpdateForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from rest_framework import viewsets
from .serializers import EventSerializer
from .filters import EventFilter
from django_filters.views import FilterView


from django.http import HttpResponseRedirect, request


def index(request):
    upcoming_events_list = Event.objects.order_by('-start_time')[:5]
    latest_event = Event.objects.order_by('-created_date')[:1]
    context = {'upcoming_events_list': upcoming_events_list, 'latest_event':latest_event}
    return render(request, 'eventfinder/index.html', context)

class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

def attending(self, pk):
    event = Event.objects.get(pk=pk)
    user = User.objects.get(self.request.user)
    event.attendees.add(user)
    return HttpResponseRedirect('/freeeventfinder/')

class EventCreate(LoginRequiredMixin, CreateView):
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

    def get_object(self):
        event_id = self.kwargs.get('pk')
        return get_object_or_404(Event, pk=event_id, host=self.request.user)

class EventDelete(DeleteView):
    model = Event
    template_name = 'eventfinder/event_delete.html'
    success_url = reverse_lazy('eventfinder:index')

def event_filter(request):
    f = EventFilter(request.GET, queryset = Event.objects.all())
    return render(request, 'eventfinder/event_filter.html', {'filter': f})

# class EventFilter(ListView):
#     template_name = 'eventfinder/event_filter.html'
#     queryset = Event.objects.all()

class VenueDetail(DetailView):
    model = Venue
    context_object_name = 'venue'

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

