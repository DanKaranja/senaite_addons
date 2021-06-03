from plone.supermodel import model
from zope import schema
from bika.lims import _
from bika.lims.catalog import SETUP_CATALOG
from plone.dexterity.content import Item


class SMSReport(Item):
    """Dynamic Analysis Specification
    """
    _catalogs = [SETUP_CATALOG]

class ISMSReport(model.Schema):
    """Dexterity-Schema for SMS reports
    """

    phone_number = schema.TextLine(
        title=_(u"phone_number"),
        required=False
    )

    sms_message = schema.TextLine(
        title=_(u"sms_message"),
        required=False
    )

    date_published = schema.TextLine(
        title=_(u"date_published"),
        required=False
    )

    report_uid = schema.TextLine(
        title=_(u"report_uid"),
        required=False
    )

    tiny_url = schema.TextLine(
        title=_(u"report_uid"),
        required=False
    )
