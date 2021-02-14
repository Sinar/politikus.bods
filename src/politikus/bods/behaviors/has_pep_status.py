# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from politikus.bods import _
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IHasPepStatusMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IHasPepStatus(model.Schema):
    """
    """

    hasPepStatus = schema.Bool(
        title=_(u'Has PEP Status'),
        description=_(u'''
            Is the person described in this statement a politically
            exposed person?  This field should not be used if PEP
            declarations are not expected as part of this disclosure. If
            a PEP declaration is expected but missing this field should
            not be used but the reason for the missing data declared in
            the pepStatusDetails field.
            '''
                      ),
        required=False,
    )


@implementer(IHasPepStatus)
@adapter(IHasPepStatusMarker)
class HasPepStatus(object):
    def __init__(self, context):
        self.context = context

    @property
    def hasPepStatus(self):
        if safe_hasattr(self.context, 'hasPepStatus'):
            return self.context.hasPepStatus
        return None

    @hasPepStatus.setter
    def hasPepStatus(self, value):
        self.context.hasPepStatus = value
