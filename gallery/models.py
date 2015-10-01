from django.db import models
import datetime

class Gallery(models.Model):
    date_added  = models.DateTimeField(default=now)
    title       = models.CharField(max_length=64, unique=True)
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    is_public   = models.BooleanField(default=True)
