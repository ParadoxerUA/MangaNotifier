from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class User(AbstractBaseUser):

    username = models.TextField(max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta(AbstractBaseUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class MangaList(models.Model):

    name = models.TextField(max_length=100)
    url = models.URLField(max_length=300)
    updated = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
