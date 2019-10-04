from django import forms
from django.forms import ModelForm, DateTimeInput
from django.contrib.admin import widgets

from .models import Event

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
        'name', 
        'description', 
        'start_time',
        'end_time',
        'venue', 
        'category',
        'photo',
        )

class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
        'name', 
        'description', 
        'start_time',
        'end_time',
        'venue', 
        'category',
        'photo',
        )