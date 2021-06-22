from bika.lims import api
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter
from zope.component import adapts
from zope.interface import implements
from bika.lims import logger

class IlaraSamplesAdapter(object):
    adapts(IListingView)
    implements(IListingViewAdapter)
    # Order of priority of this subscriber adapter over others
    priority_order = 1000

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
        # Add a new filter status
        # draft_status = {
        #     "id": "draft",
        #     "title": "Draft",
        #     "contentFilter": {
        #         "review_state": "sample_draft",
        #         "sort_on": "created",
        #         "sort_order": "descending",
        #     },
        #     "columns": self.listing.columns.keys(),
        # }
        # self.listing.review_states.append(draft_status)

        # Add the column
        self.listing.columns['request_payment'] = {
            'title': 'Request Payment',
            'sortable': False,
            'toggle': True,
        }

        # Make the new column visible for only published results
        for filter in self.listing.review_states:
            filter.update({"columns": self.listing.columns.keys()})
            # if filter.get("id") == "published":
                

    def folder_item(self, obj, item, index):
        base_url = 'http://localhost:8081/'
        # base_url = 'http://35.190.90.81/'

        sample = api.get_object(obj)
        sample_title = sample.Title()

        payment_app_url = base_url+'payments?sampleid='+sample_title
        item['request_payment'] = "<a href='%s' target='_blank'>Not paid</a>" % payment_app_url

        payment_requests = api.search({"portal_type": "payment", "title": sample_title,'sort_on': 'mpesa_checkoutrequestid','sort_order':'desc'})
        if len(payment_requests) > 0:
            payment_request = api.get_object(payment_requests[0])

            logger.info('A payment request was made for {0}'.format(payment_request.title))
            logger.info('ID: {0}'.format(payment_request.id))
            logger.info('Is consolidated: {0}'.format(payment_request.is_consolidated))
            logger.info('Result code: {0}'.format(payment_request.mpesa_resultcode))
            
            if payment_request.is_consolidated == "True":
                logger.info(sample_title+'is a consolidated payment')
                item['request_payment'] = "<a href='%s' target='_blank'>Consolidated Payment</a>" % payment_app_url
            
            if payment_request.is_consolidated == "False":
                logger.info(sample_title+'is not a consolidated payment, but: ')
                if payment_request.mpesa_resultcode == None:
                    item['request_payment'] = "<a href='%s' target='_blank'>Incomplete Payment</a>" % payment_app_url
            
        return item