from django import forms
from .models import Event, Category, Venue
import django_filters

class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    venue = django_filters.CharFilter(field_name='venue__name', lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget = forms.CheckboxSelectMultiple)
    start_time= django_filters.DateFilter()
    class Meta:
        model = Event
        fields = ['name', 'venue', 'category', 'start_time']
        