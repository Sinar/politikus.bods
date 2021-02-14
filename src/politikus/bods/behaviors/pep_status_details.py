# -*- coding: utf-8 -*-

from plone import schema
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from politikus.bods import _
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IPepStatusDetailsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IPepStatusDetails(model.Schema):
    """
    """

    pepStatusDetails = schema.Text(
        title=_(u'PEP Status Details'),
        description=_(u'''
        One or more descriptions of this person's Politically-Exposed
        Person (PEP) status. (One per line) '''),
        required=False,
    )


@implementer(IPepStatusDetails)
@adapter(IPepStatusDetailsMarker)
class PepStatusDetails(object):
    def __init__(self, context):
        self.context = context

    @property
    def pepStatusDetails(self):
        if safe_hasattr(self.context, 'pepStatusDetails'):
            return self.context.pepStatusDetails
        return None

    @pepStatusDetails.setter
    def pepStatusDetails(self, value):
        self.context.pepStatusDetails = value
