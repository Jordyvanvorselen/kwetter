from django.db import models
from django.utils import timezone


# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey('auth.User')
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
