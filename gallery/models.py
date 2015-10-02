from django.db import models
from datetime import datetime

class Gallery(models.Model):
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
