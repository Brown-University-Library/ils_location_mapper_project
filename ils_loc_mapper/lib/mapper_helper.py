# -*- coding: utf-8 -*-

import datetime, json, logging
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound


log = logging.getLogger(__name__)


class Mapper(object):

    def __init__(self):
        pass

    def validate_request( self, get_dct ):
        """ Validates params.
            Called by views.map_location_code() """
        return ( True, None )

    def prep_bad_response( self, err ):
        rsp = HttpResponseBadRequest( '400 / %s' % err )
        return rsp

    def prep_data( self, get_dct ):
        """ Performs lookup & preps json.
            Called by views.map_location_code() """
        data = []
        return data

    def prep_response( self, data ):
        """ Returns appropriate response based on data.
            Called by views.map_location_code() """
        if data == []:
            rsp = HttpResponseNotFound()
        return rsp



