# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from . import settings_app
from ils_loc_mapper.lib import view_info_helper
from ils_loc_mapper.lib.mapper_helper import Mapper
from django.conf import settings as project_settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


log = logging.getLogger(__name__)
mapper = Mapper()


def info( request ):
    """ Returns basic data including branch & commit. """
    # log.debug( 'request.__dict__, ```%s```' % pprint.pformat(request.__dict__) )
    rq_now = datetime.datetime.now()
    commit = view_info_helper.get_commit()
    branch = view_info_helper.get_branch()
    info_txt = commit.replace( 'commit', branch )
    resp_now = datetime.datetime.now()
    taken = resp_now - rq_now
    context_dct = view_info_helper.make_context( request, rq_now, info_txt, taken )
    output = json.dumps( context_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def map_location_code( request ):
    """ Returns format for specific code or all data. """
    ( rq_now, vldty_dct ) = ( datetime.datetime.now(), mapper.validate_request(request.GET) )
    if vldty_dct['rslt'] == False:
        return mapper.prep_bad_request_response( vldty_dct['err'] )
    request_type = mapper.get_request_type( request.GET )
    if request_type == 'code':
        data_dct = mapper.prep_code_data( request.GET['code'] )
        rsp = mapper.prep_code_response( data_dct, request, rq_now )
    else:
        data_dct = mapper.prep_dump_data()
        rsp = mapper.prep_dump_response( data_dct, request, rq_now )
    return rsp


def login( request ):
    """ Brings up shib and redirects to admin. """
    return HttpResponse( 'foo' )
