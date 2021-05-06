from bika.lims import api
from bika.lims.api import mail as mailapi
from senaite.jsonapi.interfaces import IPushConsumer
from zope import interface


class IlaraPushTasks(object):
    """Custom adapter for performing Ilara's bidding
    """
    interface.implements(IPushConsumer)

    def __init__(self, data):
        self.data = data

    def process(self):
        """Send notifications to contacts
        """
        # Get the subject and body to be sent
        task_type = data.get("task_type")

        if task_type  == 'send_sms':
            sample_id = data.get("sample_uid")
            phone_numner = data.get("phone_number")

        # Get e-mail addresses from all contacts
        # emails = self.get_emails()

        # Send the emails
        # success = map(lambda e: self.send(e, subject, message), emails)
        return  'got it!'
        #return any(success)

    def get_pdfLink(self):
        """Returns the sample report pdf link
        """
        query = {"portal_type": ["Contact", "LabContact"]}
        contacts = map(api.get_object, api.search(query, "portal_catalog"))
        emails = map(lambda c: c.getEmailAddress(), contacts)
        emails = filter(None, emails)
        return list(OrderedDict.fromkeys(uids))

    # def get_emails(self):
    #     """Returns the emails from all registered contacts
    #     """
    #     query = {"portal_type": ["Contact", "LabContact"]}
    #     contacts = map(api.get_object, api.search(query, "portal_catalog"))
    #     emails = map(lambda c: c.getEmailAddress(), contacts)
    #     emails = filter(None, emails)
    #     return list(OrderedDict.fromkeys(uids))

    # def send(self, email, subject, body):
    #     """Creates and sends an email message
    #     """
    #     lab = api.get_setup().laboratory
    #     from_addr = lab.getEmailAddress()
    #     msg = mailapi.compose(from_addr, email, subject, body)
    #     return mailapi.send_email(mime_msg)