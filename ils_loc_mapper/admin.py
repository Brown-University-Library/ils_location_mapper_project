# -*- coding: utf-8 -*-

from .models import LocationCodeMapper
from django.contrib import admin


class LocationCodeMapperAdmin( admin.ModelAdmin ):
    list_display = [ 'code', 'building', 'display', 'format', 'note' ]
    ordering = [ 'code' ]
    save_on_top = True


admin.site.register( LocationCodeMapper, LocationCodeMapperAdmin )
