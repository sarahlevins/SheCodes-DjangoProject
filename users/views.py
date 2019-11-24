from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.base import TemplateView
from users.forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users:register_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {
        'form': form
    })


class RegisterSuccessView(TemplateView):
    template_name = "registration/register_success.html"


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                             'Your profile was successfully updated!')
            return redirect('eventfinder:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = CustomUserCreationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
