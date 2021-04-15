# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ilara.mods


class IlaraModsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ilara.mods)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ilara.mods:default')


ILARA_MODS_FIXTURE = IlaraModsLayer()


ILARA_MODS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ILARA_MODS_FIXTURE,),
    name='IlaraModsLayer:IntegrationTesting',
)


ILARA_MODS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ILARA_MODS_FIXTURE,),
    name='IlaraModsLayer:FunctionalTesting',
)


ILARA_MODS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ILARA_MODS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='IlaraModsLayer:AcceptanceTesting',
)
