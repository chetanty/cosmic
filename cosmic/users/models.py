from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    is_developer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username