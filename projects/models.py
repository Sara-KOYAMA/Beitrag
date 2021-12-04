from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    """ユーザのモデル"""
    name=models.CharField(max_length=256)

class Blog(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    #text=models.TextFiled(default='')
    day = models.DateField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    comment = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)