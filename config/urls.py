# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from ils_loc_mapper import views


admin.autodiscover()


urlpatterns = [

    url( r'^admin/login/', RedirectView.as_view(pattern_name='login_url') ),

    url( r'^admin/', admin.site.urls ),

    url( r'^info/$', views.info, name='info_url' ),

    url( r'^v1/$', views.map_location_code, name='mapper_url' ),

    url( r'^login/$', views.login, name='login_url' ),

    url( r'^$', RedirectView.as_view(pattern_name='info_url') ),

    ]
