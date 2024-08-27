from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # counter for the amount of logins
    login_count = models.PositiveIntegerField(default=0)
    name_agreement = models.CharField(max_length=5, default="No")


# whenever the user logs in, the counter will be increased
def login_user(user, **kwargs):
    user.login_count += 1
    user.save()


