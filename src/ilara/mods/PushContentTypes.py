from bika.lims import api
from bika.lims.api import mail as mailapi
from senaite.jsonapi.interfaces import IPushConsumer
from zope import interface
from plone.dexterity.utils import createContentInContainer
from bika.lims import logger


class IlaraContentTypes(object):
    """Custom adapter for sending sms pdf reports to contacts
    """
    interface.implements(IPushConsumer)

    def __init__(self, data):
        self.data = data

    def process(self):
        """Send notifications to contacts
        """

        response = {'status': 'received'}

        # self.data.get("sample_id")

        item = api.create(portal.payments, "payments", title="Test Payments")

        return response
    


    
