# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from django.conf import settings as project_settings
from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponseRedirect

log = logging.getLogger(__name__)


class LocationCodeMapper(models.Model):
    code = models.CharField( max_length=10 )
    building = models.CharField( max_length=100 )
    display = models.CharField( max_length=100 )
    format = models.CharField( max_length=100 )
    note = models.TextField( blank=True )
    create_date = models.DateTimeField( auto_now_add=True, help_text='Set automatically on save.' )
    modify_date = models.DateTimeField( auto_now=True, help_text='Set automatically on save.' )

    def __str__(self):
        return '%s - %s' % ( self.building, self.format )
