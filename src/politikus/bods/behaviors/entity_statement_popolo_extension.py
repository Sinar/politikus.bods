# -*- coding: utf-8 -*-

from politikus.bods import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IEntityStatementPopoloExtensionMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IEntityStatementPopoloExtension(model.Schema):
    """
    """

    project = schema.TextLine(
        title=_(u'Project'),
        description=_(u'Give in a project name'),
        required=False,
    )


@implementer(IEntityStatementPopoloExtension)
@adapter(IEntityStatementPopoloExtensionMarker)
class EntityStatementPopoloExtension(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if safe_hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
