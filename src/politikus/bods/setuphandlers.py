# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'politikus.bods:uninstall',
        ]


# The politikus.popolo person and organization views display the
# BODS fields from these behaviors, so they must be enabled on the
# content types for the data to be available on the views.
TYPE_BEHAVIORS = (
    ('Person', (
        'politikus.bods.nationalities',
        'politikus.bods.tax_residencies',
        'politikus.bods.has_pep_status',
        'politikus.bods.pep_status_details',
        )),
    ('Organization', (
        'politikus.bods.incorporated_in_jurisdiction',
        )),
    )


def _register_type_behaviors(portal):
    for type_name, behaviors in TYPE_BEHAVIORS:
        fti = portal.portal_types.getTypeInfo(type_name)
        if fti is None:
            continue
        enabled = list(fti.behaviors)
        for behavior in behaviors:
            if behavior not in enabled:
                enabled.append(behavior)
        fti._updateProperty('behaviors', tuple(enabled))


def post_install(context):
    """Post install script"""
    _register_type_behaviors(aq_inner(context))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
