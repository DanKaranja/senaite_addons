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

        response = {'status': 'received'}

        # Get query parameters
        sample_id = None

        try:
            sample_id = self.data.get("sample_id")
        except Exception as e:
            logger.info('No sample_id provided'.format(e))

        if sample_id != None:
            response.update(self.returnInvoiceAmount(sample_id))
        else:
            response.update(self.returnBills())

        # Get pdf link
        # emails = self.phone_number()
        # Send the emails
        # success = map(lambda e: self.send(e, subject, message), emails)

        # return self.returnBills()
        return response

    def returnBills(self):
        """Create's user for patient to login
        """

        aRequest_query_results = api.search({"portal_type": "AnalysisRequest","Complete":True})
        logger.info("Results: {0}".format(len(aRequest_query_results)))

        response = {'status': 'processed'}
        results = []

        if len(aRequest_query_results) > 0:

            for sample_r in aRequest_query_results:
                sample = api.get_object(sample_r)
                sample_object  = {}

                try:
                    sample_object['title'] = sample.Title()
                    sample_object['subtotal'] = sample.getSubtotal()
                    # logger.info('{0}: {1}'.format(sample.Title(),sample.getSubtotal()))
                except Exception as e:
                    logger.info("Failed to get sample object properties {0}".format(e))

                results.append(sample_object)
        
        if len(results) > 0:
            response.update({'status': 'success'})
        
        response.update({'results':results})

        return response

    def returnInvoiceAmount(self,sample_id):
        """Returns the emails from all registered contacts
        """

        aRequest_query_results = api.search({"portal_type": "AnalysisRequest","id": "%s" % sample_id,"Complete":True})
        

        response = {'status': 'processed'}
        results = []

        if len(aRequest_query_results) > 0:
            invoice_object  = {}

            #Fetching sample object

            logger.info("Analysis Request Results: {0}".format(len(aRequest_query_results)))

            sample = api.get_object(aRequest_query_results[0])

            try:
                invoice_object['title'] = sample.Title()
                invoice_object['subtotal'] = sample.getSubtotal()
                logger.info('{0}: {1}'.format(sample.Title(),sample.getSubtotal()))
            except Exception as e:
                logger.info("Failed to get sample object properties {0}".format(e))

            results.append(invoice_object)

            #Fetching patient details

            aRequest_cat_query_results = api.search({"id": "%s" % sample_id}, catalog="bika_catalog_analysisrequest_listing")
            logger.info("Analysis Request Catalog Results: {0}".format(len(aRequest_cat_query_results)))
            
            patient_id = aRequest_cat_query_results[0].getPatientID
            patient_query_results = api.search({"portal_type": "Patient","id": "%s" % patient_id,"Complete":True})

            logger.info("Patient Results: {0}".format(len(patient_query_results)))
            
            patient = api.get_object(patient_query_results[0])

            try:
                invoice_object['MobilePhone'] = patient.getMobilePhone()
                invoice_object['FullName'] = patient.getFullname()

                logger.info('{0} - {1}'.format(patient.getFullname(),patient.getMobilePhone()))
            except Exception as e:
                logger.info("Failed to get patient object properties {0}".format(e))

            results.append(invoice_object)
                    
                    
        
        if len(results) > 0:
            response.update({'status': 'success'})
        
        response.update({'results':results})

        return response
