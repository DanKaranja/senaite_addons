from bika.lims import api
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter

class IlaraCustomSamplesAdapter(object):
    adapts(IListingView)
    implements(IListingViewAdapter)

    # Order of priority of this subscriber adapter over others
    priority_order = 1000

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
        # Do your own stuff here. E.g., add search criteria in `contentFilter` variable
        return

    def folder_item(self, obj, item, index):
        # Do your own stuff here. E.g., set the value to display for a given column
        return item