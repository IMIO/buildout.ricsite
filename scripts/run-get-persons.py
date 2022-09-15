# -*- coding: utf-8 -*-
# from imio.helpers.content import object_values
from plone import api


import logging
import sys
import transaction


portal = obj  # noqa
logger = logging.getLogger('get persons')

pc = portal.portal_catalog
brains = pc.unrestrictedSearchResults(portal_type='person')
print(u'Type org;Organisation;Nom;Prénom;Email;Fonctions;Tél;Mobile')
for brain in brains:
    person = brain.getObject()
    org = person.getParentNode()
    print(u"{};{};{};{};{};{};{};{}".format(
        org.organization_type, org.title, person.lastname, person.firstname, person.email,
        u', '.join(person.functions or []), person.phone or u'', person.cell_phone or u''))
