from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='users_profile', null=True, blank=True)
