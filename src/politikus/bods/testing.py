# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import politikus.bods


class PolitikusBodsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=politikus.bods)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'politikus.bods:default')


POLITIKUS_BODS_FIXTURE = PolitikusBodsLayer()


POLITIKUS_BODS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLITIKUS_BODS_FIXTURE,),
    name='PolitikusBodsLayer:IntegrationTesting',
)


POLITIKUS_BODS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLITIKUS_BODS_FIXTURE,),
    name='PolitikusBodsLayer:FunctionalTesting',
)


POLITIKUS_BODS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLITIKUS_BODS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolitikusBodsLayer:AcceptanceTesting',
)
