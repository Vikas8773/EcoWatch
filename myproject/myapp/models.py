from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.username
