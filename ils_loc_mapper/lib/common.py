import logging


log = logging.getLogger(__name__)


def make_request_url( scheme, meta_dct ):
    """ Returns requesting url.
        Called by lib.view_info_helper.make_context() and lib.mapper_helper.prep_code_response() and prep_dump_response() """
    request_url = '%s://%s%s' % ( scheme,
        meta_dct.get( 'HTTP_HOST', '127.0.0.1' ),  # HTTP_HOST doesn't exist for client-tests
        meta_dct.get('REQUEST_URI', meta_dct['PATH_INFO'])
    )
    log.debug( 'request_url, ```%s```' % request_url )
    return request_url
