# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from politikus.bods.behaviors.incorporated_in_jurisdiction import IIncorporatedInJurisdictionMarker
from politikus.bods.testing import POLITIKUS_BODS_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class IncorporatedInJurisdictionIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_BODS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_incorporated_in_jurisdiction(self):
        behavior = getUtility(IBehavior, 'politikus.bods.incorporated_in_jurisdiction')
        self.assertEqual(
            behavior.marker,
            IIncorporatedInJurisdictionMarker,
        )
