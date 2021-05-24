# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.CORE.
#
# SENAITE.CORE is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2020 by it's authors.
# Some rights reserved, see README and LICENSE.

from AccessControl import ClassSecurityInfo
from Products.Archetypes.public import ManagedSchema
from Products.Archetypes.public import StringField
from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import TextAreaWidget
from Products.Archetypes.public import TextField
from Products.Archetypes.public import registerType
from zope.interface import implements

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from bika.lims import bikaMessageFactory as _
from ilara.mods.config import PROJECTNAME
from bika.lims.interfaces import IDeactivable
from ilara.mods.interfaces import IPayments

schema = ManagedSchema((

    TextField(
        "uid",
        allowable_content_types=("text/plain",),
        widget=TextAreaWidget(
            label=_("Remarks"),
        )
    ),

    StringField(
        "amount",
        searchable=1,
        required=0,
        widget=StringWidget(
            label=_("amount."),
        ),
    ),
))


class Payments(base.ATCTContent):
    """An Archetype for an Payments application"""

    implements(IPayments)

    schema = schema


registerType(Payments, PROJECTNAME)