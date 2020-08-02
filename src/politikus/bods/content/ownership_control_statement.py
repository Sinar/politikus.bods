# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
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
from plone.app.z3cform.widget import SelectFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from politikus.bods import _

class IOwnershipControlStatement(model.Schema):
    """ Marker interface and Dexterity Python Schema for OwnershipControlStatement
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('ownership_control_statement.xml')

    # Statement date
    # Implemented as Publication Date

    # componentStatements

    directives.widget('subject',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    subject = RelationChoice(
            title=_(u'Subject'),
            description=_(u'''
            The subject of an ownership or control relationship.
            '''),
            source=CatalogSource(portal_type=[
                    'Organization',
                    ]),
            required=False,
            )

    directives.widget('interestedParty',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    interestedParty = RelationChoice(
            title=_(u'Interested Party'),
            description=_(u'''
            The interested party has some level of ownership or control
            over the entity referenced in this ownership or control
            statement. This should be described with reference to either
            an entity statement or person statement, or, where the
            interested party is unknown, details of why.
            '''),
            source=CatalogSource(portal_type=[
                    'Person',
                    'Organization',
                    ]),
            required=False,
            )

    # interests

    beneficialOwnershipOrControl = schema.Bool(
            title=_(u'Beneficial Ownership Control'),
            description=_(u'''
                Does this statement assert this as a beneficial
                ownership or control interest? A beneficial ownership or
                control interest is always between a natural person and
                some entity, and exists where the person ultimately
in               benefits from, or has a degree of control over, the
                entity. There may be cases where a person has an
                interest in an entity, but where there are arrangements
                or other conditions that mean this interest does not
                constitute beneficial ownership or control.
            '''),
            required=False,
            )

    directives.widget(interest_type=SelectFieldWidget)
    interest_type = schema.Choice(
        title=_(u'Interest Type'),
        description=_(u'''
        Nature of Interest
        '''),

        required=False,
        vocabulary='politikus.bods.InterestType',
        )

    directives.widget(interest_level=SelectFieldWidget)
    interest_level = schema.Choice(
        title=_(u'Interest Level'),
        description=_(u'''
        Is this interest held directly or indirectly?
        '''),

        required=False,
        vocabulary='politikus.bods.InterestLevel',
        )

    interest_details = RichText(
        title=_(u'Interest Details'),
        description=_(u'''
        This field may be used to provide the local name given to this
        kind of interest, or any further semi-structured or unstructured
        information to clarify the nature of the interest held.
        '''),
        required=False,
        )

    share_exact = schema.Float(
            title=_(u'Exact percentage share 0-100'),
            description=_(u'''
            The exact share of this interest held (where available).
            '''),
            required=False,
            )

    share_maximum = schema.Float(
            title=_(u'Maximum percentage share 0-100'),
            description=_(u'''
            The upper bound of the share of this interest known to be held.
            '''),
            required=False,
            )

    share_minimum = schema.Float(
            title=_(u'Minumum percentage share 0-100'),
            description=_(u'''
            The lower bound of the share of this interest known to be held.
            '''),
            required=False,
            )

    start_date = schema.Date(
        title=_(u'Start Date'),
        description=_(u'''
        When did this interest first occur. Please provide as precise a
        date as possible in ISO 8601 format.'''),
        required=False,)

    end_date = schema.Date(
        title=_('End Date'),
        description=_(u'''
        When did this interest cease. Please provide as precise a date as
        possible in ISO 8601 format.
        '''),
        required=False,)

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
