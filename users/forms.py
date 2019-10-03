from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class RegisterUserForm(UserCreationForm):
  class Meta(UserCreationForm):
      model = User
      fields = (
        'username', 
        'email',
        'first_name',
        'last_name',
        )

class UpdateUserForm(UserChangeForm):
  class Meta:
      model = User
      fields = (
        'username', 
        'email',
        'first_name',
        'last_name',
        )