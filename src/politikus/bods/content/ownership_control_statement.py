# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource



# from politikus.bods import _


class IOwnershipControlStatement(model.Schema):
    """ Marker interface and Dexterity Python Schema for OwnershipControlStatement
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('ownership_control_statement.xml')

    # Statement date
    # Implemented as Publication Date

    # componentStatements

    directives.widget('componentStatements',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    componentStatements = RelationList(
            title=_(u'Component Statements'),
            description=_(u'''
            Persons, Organizations, Relationships or Memberships
            implicated in circumstantial manner for
            this issue.'''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type=[
                    'Person',
                    'Organization',
                    'Relationship',
                    'Membership'])
                ),
            required=False,
            )



    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IOwnershipControlStatement)
class OwnershipControlStatement(Container):
    """
    """
