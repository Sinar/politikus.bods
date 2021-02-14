# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from politikus.bods.behaviors.has_pep_status import IHasPepStatusMarker
from politikus.bods.testing import POLITIKUS_BODS_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class HasPepStatusIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_BODS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_has_pep_status(self):
        behavior = getUtility(IBehavior, 'politikus.bods.has_pep_status')
        self.assertEqual(
            behavior.marker,
            IHasPepStatusMarker,
        )
