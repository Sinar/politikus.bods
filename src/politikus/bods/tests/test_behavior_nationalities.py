# -*- coding: utf-8 -*-
from politikus.bods.behaviors.nationalities import INationalitiesMarker
from politikus.bods.testing import POLITIKUS_BODS_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class NationalitiesIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_BODS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_nationalities(self):
        behavior = getUtility(IBehavior, 'politikus.bods.nationalities')
        self.assertEqual(
            behavior.marker,
            INationalitiesMarker,
        )
