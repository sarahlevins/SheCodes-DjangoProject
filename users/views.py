from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegisterUserForm, UpdateUserForm
from .models import User

class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('eventfinder:index')

class UserDetail(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

class UserUpdate(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'user_update.html'

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('users:user-detail', kwargs={'pk': user_id})

class Login(LoginView):
    pass

class Logout(LogoutView):
    pass
