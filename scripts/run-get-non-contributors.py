# -*- coding: utf-8 -*-
# from imio.helpers.content import object_values
from plone import api

import logging
import sys
import transaction


portal = obj  # noqa
logger = logging.getLogger('get non contributors')

# get admin user
acl_users = app.acl_users  # noqa
user = acl_users.getUser('admin')
if user:
    user = user.__of__(acl_users)
    newSecurityManager(None, user)

view = portal.unrestrictedTraverse('@@send_mail')
view.get_non_contributor_organizations_members(2023)
