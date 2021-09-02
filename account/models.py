from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    card = models.CharField(max_length=255, null=True, blank=True)
    is_director = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
