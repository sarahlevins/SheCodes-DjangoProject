from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'eventfinder'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('event_create/', views.EventCreate.as_view(), name='event-create'),
    path('<int:pk>/event_update/', views.EventUpdate.as_view(), name='event-update'),
    path('<int:pk>/event_delete/', views.EventDelete.as_view(), name='event-delete'),
    path('venue_detail/<int:pk>', views.VenueDetail.as_view(), name='venue-detail'),
    path('attending/', views.Attending.as_view(), name='attending')
    ]