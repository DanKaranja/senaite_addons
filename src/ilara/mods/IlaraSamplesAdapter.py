from bika.lims import api
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter
from zope.component import adapts
from zope.interface import implements

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
        sample = api.get_object(obj)
        # sms_api_url = obj.getContactURL
        # subtotal = obj.getDateReceived
        # ar = sample.getAnalysisRequest()
        
        # query_url = 'http://35.190.90.81/payments?sampleid='+sample.Title()
        query_url = 'http://localhost:8081/payments?sampleid='+sample.Title()
        item['request_payment'] = "<a href='%s' target='_blank'>Request Payment</a>" % query_url
        return item