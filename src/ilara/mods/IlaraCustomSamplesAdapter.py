from bika.lims import api
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter
from zope.component import adapts
from zope.interface import implements

class IlaraCustomSamplesAdapter(object):
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
        # self.listing.columns["sms_report"] = {
        #     "title": "Dispatch SMS Report",
        #     "sortable": False,
        #     "toggle": True,
        # }

        # # Make the new column visible for only published results
        # for filter in self.listing.review_states:
        #     if filter.get("id") == "published":
        #         filter.update({"columns": self.listing.columns.keys()})

    def folder_item(self, obj, item, index):
        # sample = api.get_object(obj)
        # sms_api_url = obj.getContactURL
        # subtotal = obj.getDateReceived
        # item["sms_report"] = subtotal #"<a href='%s'>Send SMS: - %s</a>" % (sms_api_url,subtotal)
        return item