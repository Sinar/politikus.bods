# -*- coding: utf-8 -*-

# from plone import api
from politikus.bods import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class InterestType(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'shareholding', _(u'Shareholding')),
            VocabItem(u'voting-rights', _(u'Voting Rights')),
            VocabItem(u'appointment-of-board', _(u'Appointment of board')),
            VocabItem(u'other-influence-or-control',
                      _(u'Other influence or control')),
            VocabItem(u'senior-managing-official',
                      _(u'Senior Managing Official')),
            VocabItem(u'settlor-of-trust', _(u'Settlor of trust')),
            VocabItem(u'trustee-of-trust', _(u'Trustee of a trust')),
            VocabItem(u'protector-of-trust', _(u'Protector of a trust')),
            VocabItem(u'beneficiary-of-trust',
                      _(u'Beneficiary of a trust')),
            VocabItem(u'other-influence-or-control-of-trust',
                      _(u'Other influence or control of a trust')),
            VocabItem(u'rights-to-surplus-assets-on-dissolution',
                      _(u'Rights to surplus assets on dissolution')),
            VocabItem(u'rights-to-profit-or-income',
                      _(u'Rights to receive profits or income')),
            VocabItem(u'rights-granted-by-contract',
                      _(u'Rights granted by contract')),
            VocabItem(u'conditional-rights-granted-by-contract',
                      _(u'Conditional rights granted by contract')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


InterestTypeFactory = InterestType()
