# -*- coding: utf-8 -*-

import datetime, json, logging, pprint
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from ils_loc_mapper.models import LocationCodeMapper


log = logging.getLogger(__name__)


class Mapper(object):

    def __init__(self):
        pass

    def validate_request( self, get_dct ):
        """ Validates params.
            Called by views.map_location_code() """
        out = {'rslt': False, 'err': 'Bad Request'}
        ( code_val, data_val ) = ( get_dct.get('code', None), get_dct.get('data', None) )
        if code_val:
            if len(code_val) > 0:
                out = {'rslt': True, 'err': None}
        elif data_val:
                if len(data_val) > 0:
                    out = {'rslt': True, 'err': None}
        log.debug( 'validity-out, ```%s```' % out )
        return out

    def get_request_type( self, get_dct ):
        """ Returns `code` or `dump`.
            Called by views.map_location_code() """
        try:
            get_dct['code']
            code_type = 'code'
        except Exception as e:
            code_type = 'data'
        log.debug( 'code_type, `%s`' % code_type )
        return code_type

    def prep_code_data( self, code ):
        """ Performs lookup & returns data.
            Called by views.map_location_code() """
        out = { 'rslt': None, 'err': None }
        try:
            match = LocationCodeMapper.objects.get( code=code )
            out['rslt'] = {
                'building': match.building,
                'code': match.code,
                'display': match.display,
                'format': match.format
            }
        except Exception as e:
            log.error( 'exception getting data, ```%s```' % e )
            out['err'] = 'not found'
        log.debug( 'data-out, ```%s```' % out )
        return out

    def prep_dump_data( self ):
        """ Returns all data.
            Called by views.map_location_code() """
        items_dct = {}
        data_objs = LocationCodeMapper.objects.all().order_by( 'code' )
        for obj in data_objs:
            obj_dct = obj.dictify()
            del( obj_dct['code'] )
            items_dct[obj.code] = obj_dct
        log.debug( 'items_dct, ```%s...```' % pprint.pformat(items_dct)[0:100] )
        return items_dct

    def prep_code_response( self, data_dct ):
        """ Returns appropriate response based on data.
            Called by views.map_location_code() """
        if data_dct['err']:
            rsp = HttpResponseNotFound( '404 / no match for code')
        else:
            out_dct = {
                'request': 'request-url-coming',
                'result': {
                    'items': [ data_dct['rslt'] ],
                    'docs': 'url-coming'
                }
            }
            j_out = json.dumps( out_dct, sort_keys=True, indent=2 )
            rsp = HttpResponse( j_out, content_type='application/json; charset=utf-8' )
        return rsp

    def prep_dump_response( self, data_lst ):
        """ Returns json response.
            Called by views.map_location_code() """
        out_dct = {
            'request': 'request-url-coming',
            'result': {
                'items': data_lst,
                'docs': 'url-coming'
            }
        }
        j_out = json.dumps( out_dct, sort_keys=True, indent=2 )
        rsp = HttpResponse( j_out, content_type='application/json; charset=utf-8' )
        return rsp

    def prep_bad_request_response( self, err ):
        rsp = HttpResponseBadRequest( '400 / %s' % err )
        return rsp

    def prep_server_error_response( self, message ):
        """ Triggered by prep_data() problem:
            Called by views.map_location_code() """
        rsp =HttpResponseServerError( '500 / %s' % message )
        return rsp
