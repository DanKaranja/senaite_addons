# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory
# import ilara.mods.config


_ = MessageFactory('ilara.mods')


# def initialize(context):

#     from ilara.mods.content.payments import payments

#     content_types, constructors, ftis = process_types(
#              listTypes(config.PROJECTNAME),
#              config.PROJECTNAME)


#     # We want to register each type with its own permission,
#     # this will afford us greater control during system
#     # configuration/deployment (credit : Ben Saller)

#     allTypes = zip(content_types, constructors)
#     for atype, constructor in allTypes:
#         kind = "%s: %s" % (config.PROJECTNAME, atype.portal_type)
#         utils.ContentInit(kind,
#                           content_types      = (atype,),
#                           extra_constructors = (constructor,),
#                           fti                = ftis,
#                           ).initialize(context)
