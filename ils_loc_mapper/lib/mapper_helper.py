# -*- coding: utf-8 -*-

import datetime, json, logging
from django.http import HttpResponse, HttpResponseBadRequest


log = logging.getLogger(__name__)


class Mapper(object):

    def __init__(self):
        pass

    def validate_request( self, get_dct ):
        """ Validates params.
            Called by views.map_location_code() """
        return ( False, 'foo' )

    def prep_bad_response( self, err ):
        rsp = HttpResponseBadRequest( '400 / %s' % err )
        return rsp
