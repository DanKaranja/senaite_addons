from plone.app.textfield import RichText
from plone.autoform import directives
from plone.namedfile import field as namedfile
from plone.supermodel.directives import fieldset
from plone.supermodel import model
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from ploneconf.site import MessageFactory as _

class ISMSReport(model.Schema):
    """Dexterity-Schema for SMS reports
    """

    phone_number = TextLine(
        title=_(u"phone_number"),
        required=False
    )

    sms_message = TextLine(
        title=_(u"sms_message"),
        required=False
    )

    date_published = TextLine(
        title=_(u"date_published"),
        required=False
    )

    report_uid = TextLine(
        title=_(u"report_uid"),
        required=False
    )
