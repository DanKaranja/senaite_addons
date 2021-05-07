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

        aRequest_query_results = api.search({"portal_type": "AnalysisRequest","id": "%s" % sample,"Complete":True})
        aReport_query_results = api.search({"portal_type": "ARReport","parent_id": "%s" % sample,"Complete":True})

        # AnalysisRequests  = map(api.get_object, query_results)

        log_info_query_aRequest = "aRequest query for '{0}' has returned {1} result(s)".format(sample,len(aRequest_query_results))
        log_info_query_aReport = "aReport query for '{0}' has returned {1} result(s)".format(sample,len(aReport_query_results))

        logger.info(log_info_query_aRequest)
        logger.info(log_info_query_aReport)

        filtered_aReports =  filter(lambda n : n.parent_id == sample,aReport_query_results)
        log_info_query_aReport = "aReport filter for '{0}' has returned {1} result(s)".format(sample,len(filtered_aReports))

        if len(filtered_aReports) > 0:
            try:
                logger.info("Attempt 1: {0}".format(filtered_aReports[0].url))
            except Exception as e:
                logger.info("Attempt 1 failed: {0}".format(e))

            # try:
            #     logger.info("Attempt 2: {0}".format(aRequest_query_results[0].MemberDiscount))
            # except Exception as e:
            #     logger.info("Attempt 2: failed: {0}".format(e))
            
            # try:
            #     logger.info("Attempt 3: {0}".format(query_results[0]['Patient']))
            # except Exception as e:
            #     logger.info("Attempt 3: failed: {0}".format(e))

        # Patient = fields.get("Patient")
        # value = {"Sample Type": SampleTypeTitle.value}
        # response =  {"message":message,"value":value}


        # query = {"portal_type": ["Contact", "LabContact"]}
        # contacts = map(api.get_object, api.search(query, "portal_catalog"))
        # emails = map(lambda c: c.getEmailAddress(), contacts)
        # emails = filter(None, emails)
        return True

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