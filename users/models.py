from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_photo = models.ImageField(upload_to='user_photos', blank=True)

    def __str__(self):
        return self.username