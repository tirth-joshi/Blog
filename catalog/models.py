from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User model
class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    birth_date = models.DateField(blank=True, null=True)


# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=180, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.CharField(max_length=180, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    is_private = models.BooleanField(default=False)


# Like model
class Like(models.Model):
    name = models.CharField(max_length=180, blank=True, null=True)
    type = models.CharField(max_length=180, blank=True, null=True)
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.DO_NOTHING)
