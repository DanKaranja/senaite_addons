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
        item['request_payment'] = "<a href='%s' target='_blank'>Request Payment</a>" % payment_app_url

        payment_requests = api.search({"portal_type": "mpesarequest", "title": sample_title})
        if len(payment_requests) > 0:
            payment_request = api.get_object(payment_requests[0])
            logger.info('A payment request was made for '+sample_title)
            item['request_payment'] = "<a href='%s' target='_blank'>Incomplete Payment</a>" % payment_app_url
        
        payment_responses = api.search({"portal_type": "mpesaresponse", "title": sample_title,"sort_on": "created"})
        logger.info('Responses for '+sample_title+' : '+str(len(payment_responses)))
        if len(payment_responses) > 0:
            payment_response = api.get_object(payment_responses[0])
            payment_result_code = payment_response.resultcode
            logger.info('Created: '+payment_response.created)

            if payment_result_code and payment_result_code == '0': 
                logger.info('Result code: '+payment_result_code)
                item['request_payment'] = "<a href='%s' target='_blank'>Paid</a>" % payment_app_url
                    
        
        
        return item