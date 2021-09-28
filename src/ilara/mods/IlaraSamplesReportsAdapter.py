from bika.lims import api
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter
from zope.component import adapts
from zope.interface import implements

class IlaraSamplesReportsAdapter(object):
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
        self.listing.columns['sms_report'] = {
            'title': 'SMS Report',
            'sortable': False,
            'toggle': True,
        }

        # Make the new column visible for only published results
        for filter in self.listing.review_states:
            filter.update({"columns": self.listing.columns.keys()})
            # if filter.get("id") == "published":
                

    def folder_item(self, obj, item, index):
        # base_url = 'http://localhost:8081/'
        base_url = 'http://35.190.90.81/'

        sample = api.get_object(obj)
        ar = sample.getAnalysisRequest()
        doctor_url = sample.getContactURL()
        host = doctor_url.split('/')[1]
        # logger.info('Host: {0}'.format(host))

        if host == 'riverside':
            query_url = base_url+'smspublish?sampleid='+ar.Title()
            item['sms_report'] = "<a href='%s' target='_blank'>Send SMS</a>" % query_url
            
        return item