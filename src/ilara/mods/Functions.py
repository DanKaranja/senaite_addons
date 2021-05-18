from bika.lims import api
from bika.lims.api import mail as mailapi
from senaite.jsonapi.interfaces import IPushConsumer
from zope import interface
from bika.lims import logger


class IlaraFunctions(object):
    """Custom adapter for sending sms pdf reports to contacts
    """
    interface.implements(IPushConsumer)

    def __init__(self, data):
        self.data = data

    def process(self):
        """Send notifications to contacts
        """
        # Get query parameters

        # sample_id = self.data.get("sample_id")

        # Get pdf link
        # emails = self.phone_number()

        # Send the emails
        # success = map(lambda e: self.send(e, subject, message), emails)
        return self.returnBills()
        # return True

    def returnBills(self):
        """Create's user for patient to login
        """

        aRequest_query_results = api.search({"portal_type": "AnalysisRequest","Complete":True})
        logger.info("Results: {0}".format(len(aRequest_query_results)))

        results = []

        if len(aRequest_query_results) > 0:

            for sample_r in aRequest_query_results:
                sample = api.get_object(sample_r)
                sample_object  = {}

                try:
                    sample_object['title'] = sample.Title()
                    sample_object['subtotal'] = sample.getSubtotal()
                    logger.info('{0}: {1}'.format(sample.Title(),sample.getSubtotal()))
                except Exception as e:
                    logger.info("Failed to get sample object properties {0}".format(e))

                results.append(sample_object)
            
            # try:
            #     logger.info("Attempt 3: {0}".format(aRequest_query_results[0].getSubtotal))
            # except Exception as e:
            #     logger.info("Attempt 3: failed: {0}".format(e))

        # portal_groups = api.get_tool("portal_groups")
        # portal_registration = api.get_tool("portal_registration")

        # bsc = api.get_tool('bika_setup_catalog')
        # exists = [o.getObject() for o in bsc(portal_type="LabContact") if o.getObject().getUsername()==username]
        # if exists:
        #     error = "Lab Contact: username '{0}' already exists.".format(username)
        #     logger.error(error)




        # query = {"portal_type": "AnalysisRequest","title":sample}
        # AnalysisRequests = map(api.get_object, api.search(query, "portal_catalog"))

        # aRequest_query_results = api.search({"portal_type": "AnalysisRequest","id": "%s" % sample,"Complete":True})
        # aReport_query_results = api.search({"portal_type": "ARReport"})

        # AnalysisRequests  = map(api.get_object, query_results)

        # log_info_query_aRequest = "aRequest query for '{0}' has returned {1} result(s)".format(sample,len(aRequest_query_results))
        # log_info_query_aReport = "aReport query for '{0}' has returned {1} result(s)".format(sample,len(aReport_query_results))

        # logger.info(log_info_query_aRequest)
        # logger.info(log_info_query_aReport)

        # filtered_aReports =  filter(lambda n : n.parent_id == sample,aReport_query_results)
        # log_info_query_aReport = "aReport filter for '{0}' has returned {1} result(s)".format(sample,len(filtered_aReports))

        # if len(filtered_aReports) > 0:
        #     try:
        #         logger.info("Attempt 1: {0}".format(filtered_aReports[0].url))
        #     except Exception as e:
        #         logger.info("Attempt 1 failed: {0}".format(e))

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
        return results

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