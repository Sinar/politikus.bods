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


class INationalitiesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class INationalities(model.Schema):
    """
    """

    directives.widget(nationalities=SelectFieldWidget)
    nationalities = schema.List(
            title=u'Nationalities',
            description=u'Nationalities held by this individual',
            required=False,
            value_type=schema.Choice(
                vocabulary='collective.vocabularies.iso.countries',
                ),
            )


@implementer(INationalities)
@adapter(INationalitiesMarker)
class Nationalities(object):
    def __init__(self, context):
        self.context = context

    @property
    def nationalities(self):
        if safe_hasattr(self.context, 'nationalities'):
            return self.context.nationalities
        return None

    @nationalities.setter
    def nationalities(self, value):
        self.context.nationalities = value
