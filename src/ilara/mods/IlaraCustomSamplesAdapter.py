from bika.lims import api
from senaite.core.listing.interfaces import IListingView
from senaite.core.listing.interfaces import IListingViewAdapter

class IlaraCustomSamplesAdapter(object):

    # Order of priority of this subscriber adapter over others
    priority_order = 1000

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
        # Do your own stuff here. E.g., add search criteria in `contentFilter` variable
                # Add a new filter status
        draft_status = {
            "id": "draft",
            "title": "Draft",
            "contentFilter": {
                "review_state": "sample_draft",
                "sort_on": "created",
                "sort_order": "descending",
            },
            "columns": self.listing.columns.keys(),
        }
        self.listing.review_states.append(draft_status)

        # Add the column
        self.listing.columns["MyColumn"] = {
            "title": "My column",
            "sortable": False,
            "toggle": True,
        }

        # Make the new column visible for all filter statuses
        for filter in self.listing.review_states:
            filter.update({"columns": self.listing.columns.keys()})
        return

    def folder_item(self, obj, item, index):
        # Do your own stuff here. E.g., set the value to display for a given column

        sample = api.get_object(obj)
        item["Trigger SMS"] =  "Empty value"
        
        return item