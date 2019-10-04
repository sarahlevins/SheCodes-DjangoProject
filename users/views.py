from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    context_object_name = 'usersdetail'

class UserUpdate(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'user_update.html'

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('users:user-detail', kwargs={'pk': user_id})

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id, username=self.request.user)

class UserDelete(DeleteView):
    model = User
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('eventfinder:index')    

class Login(LoginView):
    pass

class Logout(LogoutView):
    pass
