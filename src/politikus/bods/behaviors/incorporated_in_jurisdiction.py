# -*- coding: utf-8 -*-

from politikus.bods import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.autoform import directives
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from zope import schema
from plone.app.z3cform.widget import SelectFieldWidget

class IIncorporatedInJurisdictionMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IIncorporatedInJurisdiction(model.Schema):
    """
    """
    directives.widget(incorporatedInJurisdiction=SelectFieldWidget)
    incorporatedInJurisdiction = schema.Choice(
            title=u'Incorporated in Jurisdiction',
            description=u'Where this legal entity is incorporated',
            required=False,
            vocabulary='collective.vocabularies.iso.countries',
            )


@implementer(IIncorporatedInJurisdiction)
@adapter(IIncorporatedInJurisdictionMarker)
class IncorporatedInJurisdiction(object):
    def __init__(self, context):
        self.context = context

    @property
    def incorporatedInJurisdiction(self):
        if safe_hasattr(self.context, 'incorporatedInJurisdiction'):
            return self.context.incorporatedInJurisdiction
        return None

    @incorporatedInJurisdiction.setter
    def incorporatedInJurisdiction(self, value):
        self.context.incorporatedInJurisdiction = value
