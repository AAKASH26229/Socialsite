import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    
    phone_number = models.CharField(max_length=10, unique=True, blank=False, null=False)
    email = models.EmailField("email address", blank=False, null=False)
    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['username', 'email', 'first_name', 'last_name']
    
        