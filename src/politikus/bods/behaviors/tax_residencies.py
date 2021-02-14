# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from politikus.bods import _
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class ITaxResidenciesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ITaxResidencies(model.Schema):
    """
    """

    directives.widget(taxResidencies=SelectFieldWidget)
    taxResidencies = schema.List(
            title=u'Tax Residencies',
            description=u'''
            Countries representing the tax residencies
            held by this individual.
            ''',
            required=False,
            value_type=schema.Choice(
                vocabulary='collective.vocabularies.iso.countries',
                ),
            )

@implementer(ITaxResidencies)
@adapter(ITaxResidenciesMarker)
class TaxResidencies(object):
    def __init__(self, context):
        self.context = context

    @property
    def taxResidencies(self):
        if safe_hasattr(self.context, 'taxResidencies'):
            return self.context.taxResidencies
        return None

    @taxResidencies.setter
    def taxResidencies(self, value):
        self.context.taxResidencies = value
