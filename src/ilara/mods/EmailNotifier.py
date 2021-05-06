from bika.lims import api
from bika.lims.api import mail as mailapi
from senaite.jsonapi.interfaces import IPushConsumer
from zope import interface


class EmailNotifier(object):
    """Custom adapter for sending e-mail notifications to contacts
    """
    interface.implements(IPushConsumer)

    def __init__(self, data):
        self.data = data

    def process(self):
        """Send notifications to contacts
        """
        # Get the subject and body to be sent
        subject = data.get("subject")
        message = data.get("message")

        # Get e-mail addresses from all contacts
        emails = self.get_emails()

        # Send the emails
        success = map(lambda e: self.send(e, subject, message), emails)
        return any(success)

    def get_emails(self):
        """Returns the emails from all registered contacts
        """
        query = {"portal_type": ["Contact", "LabContact"]}
        contacts = map(api.get_object, api.search(query, "portal_catalog"))
        emails = map(lambda c: c.getEmailAddress(), contacts)
        emails = filter(None, emails)
        return list(OrderedDict.fromkeys(uids))

    def send(self, email, subject, body):
        """Creates and sends an email message
        """
        lab = api.get_setup().laboratory
        from_addr = lab.getEmailAddress()
        msg = mailapi.compose(from_addr, email, subject, body)
        return mailapi.send_email(mime_msg)