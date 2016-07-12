from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Album(models.Model):
    """
    model for user albums
    """
    user = models.ForeignKey(User)	
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    description = models.CharField(max_length=1024, verbose_name=_('Description'))

    # preview/thumbnail image for an album
    img = models.FileField(upload_to = 'photos/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __unicode__(self):
        """
        function returns unicode representation of album
        """
        return "%s" % self.title

class Photo(models.Model):
    """
    model for user photos
    """
    user = models.ForeignKey(User)	
    album = models.ForeignKey(Album)	
    img = models.FileField(upload_to = 'photos/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    
    def __unicode__(self):
        """
        function returns unicode representation of photo
        """
        return "%s" % self.img
