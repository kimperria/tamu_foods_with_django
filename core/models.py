from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    '''
        Redefine user instances for the application
    '''
    email = models.EmailField(unique=True)
