# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from politikus.bods.content.ownership_control_statement import IOwnershipControlStatement  # NOQA E501
from politikus.bods.testing import POLITIKUS_BODS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class OwnershipControlStatementIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_BODS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_ownership_control_statement_schema(self):
        fti = queryUtility(IDexterityFTI, name='Ownership Control Statement')
        schema = fti.lookupSchema()
        self.assertEqual(IOwnershipControlStatement, schema)

    def test_ct_ownership_control_statement_fti(self):
        fti = queryUtility(IDexterityFTI, name='Ownership Control Statement')
        self.assertTrue(fti)

    def test_ct_ownership_control_statement_factory(self):
        fti = queryUtility(IDexterityFTI, name='Ownership Control Statement')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOwnershipControlStatement.providedBy(obj),
            u'IOwnershipControlStatement not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_ownership_control_statement_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Ownership Control Statement',
            id='ownership_control_statement',
        )

        self.assertTrue(
            IOwnershipControlStatement.providedBy(obj),
            u'IOwnershipControlStatement not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('ownership_control_statement', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('ownership_control_statement', parent.objectIds())

    def test_ct_ownership_control_statement_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Ownership Control Statement')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_ownership_control_statement_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Ownership Control Statement')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'ownership_control_statement_id',
            title='Ownership Control Statement container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
