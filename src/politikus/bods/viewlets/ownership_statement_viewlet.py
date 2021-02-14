# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.interfaces import IVocabularyFactory


class OwnershipStatementViewlet(ViewletBase):

    def backrefs(self, attribute_name):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute=attribute_name)
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'Ownership Control Statement':

                    # Temporary workaround for broken objects
                    if obj.absolute_url():
                        # Only for Statements that are linked to an
                        # Issue
                        if obj.interestedParty:
                            result.append(obj)

        return result

    def render(self):
        return super(OwnershipStatementViewlet, self).render()
