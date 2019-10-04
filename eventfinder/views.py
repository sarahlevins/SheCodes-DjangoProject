from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event, Venue, Category
from .forms import EventCreateForm, EventUpdateForm
from users.models import User
from django.forms import formset_factory


def index(request):
    upcoming_event_list = Event.objects.order_by('-start_time')[:5]
    context = {'upcoming_event_list': upcoming_event_list}
    return render(request, 'eventfinder/index.html', context)

class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

    def user_attending (request, user_id):
        attendee = User.objects.get(pk=user_id)
        EventInlineFormSete = inlineformset_factory(User, Event, fields=('attendees',))

        if request.method == "POST":
            formset = EventInlineFormSet(request.POST, request.FILES, instance=user)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(event.get_absolute_url())
        else:
            formset = EventInlineFormSet(instance=user)
            return render(request, 'attending.html', {'formset': formset})

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

class Attending(UpdateView):
    model = Event
    template_name = 'eventfinder/attending.html'
    fields = ['attendees']    

class VenueDetail(DetailView):
    model = Venue
    context_object_name = 'venue'
