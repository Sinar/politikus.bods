# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from politikus.bods.behaviors.tax_residencies import ITaxResidenciesMarker
from politikus.bods.testing import POLITIKUS_BODS_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class TaxResidenciesIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_BODS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_tax_residencies(self):
        behavior = getUtility(IBehavior, 'politikus.bods.tax_residencies')
        self.assertEqual(
            behavior.marker,
            ITaxResidenciesMarker,
        )
