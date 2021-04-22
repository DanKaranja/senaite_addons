# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from bika.lims.interfaces import IBikaLIMS
from senaite.impress.interfaces import ILayer as ISenaiteIMPRESS
from senaite.lims.interfaces import ISenaiteLIMS


class IIlaraModsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
