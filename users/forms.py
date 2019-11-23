from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from users.models import Profile


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Enter username', min_length=4, max_length=150)
    first_name = forms.CharField(
        label='Enter first name', min_length=4, max_length=50)
    last_name = forms.CharField(
        label='Enter last name', min_length=4, max_length=50)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(
        label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'profile_photo')
