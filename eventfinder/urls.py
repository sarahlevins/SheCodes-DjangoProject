from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'eventfinder'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event-detail')
    ]