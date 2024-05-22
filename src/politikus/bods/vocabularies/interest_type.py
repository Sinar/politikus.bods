""" Zope Vocabulary for BODS InterestType Codelist """

# from plone import api
from plone.dexterity.interfaces import IDexterityContent
from politikus.bods import _
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
    Beneficial Ownership Data Standard Interest Type 0.2
    https://standard.openownership.org/en/0.2.0/schema/reference.html#interesttype
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem('shareholding', _('Shareholding')),
            VocabItem('voting-rights', _('Voting Rights')),
            VocabItem('appointment-of-board', _('Appointment of board')),
            VocabItem('other-influence-or-control',
                      _('Other influence or control')),
            VocabItem('senior-managing-official',
                      _('Senior Managing Official')),
            VocabItem('settlor-of-trust', _('Settlor of trust')),
            VocabItem('trustee-of-trust', _('Trustee of a trust')),
            VocabItem('protector-of-trust', _('Protector of a trust')),
            VocabItem('beneficiary-of-trust',
                      _('Beneficiary of a trust')),
            VocabItem('other-influence-or-control-of-trust',
                      _('Other influence or control of a trust')),
            VocabItem('rights-to-surplus-assets-on-dissolution',
                      _('Rights to surplus assets on dissolution')),
            VocabItem('rights-to-profit-or-income',
                      _('Rights to receive profits or income')),
            VocabItem('rights-granted-by-contract',
                      _('Rights granted by contract')),
            VocabItem('conditional-rights-granted-by-contract',
                      _('Conditional rights granted by contract')),
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
