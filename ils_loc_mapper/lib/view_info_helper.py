# -*- coding: utf-8 -*-

import datetime, json, logging, os, subprocess
from . import common
from django.conf import settings
from ils_loc_mapper import settings_app


log = logging.getLogger(__name__)


def get_commit():
    """ Returns commit-string.
        Called by views.info() """
    original_directory = os.getcwd()
    log.debug( 'BASE_DIR, ```%s```' % settings.BASE_DIR )
    git_dir = settings.BASE_DIR
    log.debug( 'git_dir, ```%s```' % git_dir )
    os.chdir( git_dir )
    output_utf8 = subprocess.check_output( ['git', 'log'], stderr=subprocess.STDOUT )
    output = output_utf8.decode( 'utf-8' )
    os.chdir( original_directory )
    lines = output.split( '\n' )
    commit = lines[0]
    return commit


def get_branch():
    """ Returns branch.
        Called by views.info() """
    original_directory = os.getcwd()
    git_dir = settings.BASE_DIR
    os.chdir( git_dir )
    output_utf8 = subprocess.check_output( ['git', 'branch'], stderr=subprocess.STDOUT )
    output = output_utf8.decode( 'utf-8' )
    os.chdir( original_directory )
    lines = output.split( '\n' )
    branch = 'init'
    for line in lines:
        if line[0:1] == '*':
            branch = line[2:]
            break
    return branch


def make_context( request, rq_now, info_txt, taken ):
    """ Builds and returns context.
        Called by views.info() """
    cntxt = {
        'request': {
            # 'url': common.make_request_url( request.scheme, request.META ),
            'url': common.make_request_url( request ),
            'timestamp': str( rq_now ) },
        'response': {
            'documentation': settings_app.README_URL,
            'version': info_txt,
            'elapsed_time': str( taken ) }
    }
    return cntxt
