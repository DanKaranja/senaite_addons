from bika.lims import api
from bika.lims.api import mail as mailapi
from senaite.jsonapi.interfaces import IPushConsumer
from zope import interface
from bika.lims import logger


class SMSReport(object):
    """Custom adapter for sending sms pdf reports to contacts
    """
    interface.implements(IPushConsumer)

    def __init__(self, data):
        self.data = data

    def process(self):
        """Send notifications to contacts
        """
        # Get query parameters
        sample = self.data.get("sample")
        phone_number = self.data.get("phone_number")

        log_info_sample = "Received Sample ID + Phone: {0},{1} ".format(sample, phone_number)
        logger.info(log_info_sample)

        # Get pdf link
        # emails = self.phone_number()

        # Send the emails
        # success = map(lambda e: self.send(e, subject, message), emails)
        return self.get_Pdf(sample)
        # return True

    def get_Pdf(self,sample):
        """Returns the pdf file of the sample report
        """
        # query = {"portal_type": "AnalysisRequest","title":sample}
        # AnalysisRequests = map(api.get_object, api.search(query, "portal_catalog"))

        query_results = api.search({"portal_type": "AnalysisRequest","id": "%s" % sample,"Complete":True})
        # ARReports  = map(api.get_object, query_results)

        log_info_query_sample = "Pdf sample query for '{0}' has returned {1} result(s)".format(sample,len(query_results))
        logger.info(log_info_query_sample)

        message = log_info_query_sample
        value = False

        if len(query_results) > 0:
            value = query_results[0].Patient.uid
        
        response =  {"message":message,"value":value}


        # query = {"portal_type": ["Contact", "LabContact"]}
        # contacts = map(api.get_object, api.search(query, "portal_catalog"))
        # emails = map(lambda c: c.getEmailAddress(), contacts)
        # emails = filter(None, emails)
        return response

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