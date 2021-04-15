# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ilara.mods.testing import ILARA_MODS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ilara.mods is properly installed."""

    layer = ILARA_MODS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ilara.mods is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ilara.mods'))

    def test_browserlayer(self):
        """Test that IIlaraModsLayer is registered."""
        from ilara.mods.interfaces import (
            IIlaraModsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IIlaraModsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ILARA_MODS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ilara.mods'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ilara.mods is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ilara.mods'))

    def test_browserlayer_removed(self):
        """Test that IIlaraModsLayer is removed."""
        from ilara.mods.interfaces import \
            IIlaraModsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IIlaraModsLayer,
            utils.registered_layers())
