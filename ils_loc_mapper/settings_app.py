# -*- coding: utf-8 -*-

import json, os


README_URL = os.environ['ILS_LOC_MPR__README_URL']

## auth
SUPER_USERS = json.loads( os.environ['ILS_LOC_MPR__SUPER_USERS_JSON'] )
STAFF_USERS = json.loads( os.environ['ILS_LOC_MPR__STAFF_USERS_JSON'] )  # users permitted access to admin
STAFF_GROUP = os.environ['ILS_LOC_MPR__STAFF_GROUP']  # not grouper-group; rather, name of django-admin group for permissions
TEST_META_DCT = json.loads( os.environ['ILS_LOC_MPR__TEST_META_DCT_JSON'] )
