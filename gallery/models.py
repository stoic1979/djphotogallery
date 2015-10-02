from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Gallery(models.Model):
    owner       = models.ForeignKey(User)
    date_added  = models.DateTimeField(default=datetime.now)
    title       = models.CharField(max_length=64, unique=True)
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    is_public   = models.BooleanField(default=True)

    def __unicode__(self):
        """
        function returns unicode representation of a gallery
        """
        return self.title

class Photo(models.Model):
    gallery     = models.ForeignKey(Gallery)
    date_added  = models.DateTimeField(default=datetime.now)
    title       = models.CharField(max_length=64)
    slug        = models.SlugField(unique=True)
    caption     = models.TextField(blank=True)
    is_public   = models.BooleanField(default=True)

    def __unicode__(self):
        """
        function returns unicode representation of a photo
        """
        return self.title
