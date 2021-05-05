
from bika.lims import api
from bika.lims.browser import BrowserView
from bika.lims.browser.header_table import HeaderTableView



class HeaderTableView(HeaderView):
    def __call__(self):
        if "header_table_submitted" in self.request:
            schema = self.context.Schema()
            fields = schema.fields()
            form = self.request.form
            for field in fields:
                fieldname = field.getName()
                if fieldname in form:
                    # Handle (multiValued) reference fields
                    # https://github.com/bikalims/bika.lims/issues/2270
                    uid_fieldname = "{}_uid".format(fieldname)
                    if uid_fieldname in form:
                        value = form[uid_fieldname]
                        if field.multiValued:
                            value = value.split(",")
                        field.getMutator(self.context)(value)
                    else:
                        # other fields
                        field.getMutator(self.context)(form[fieldname])
            message = _("Maybe something changed.")
            # reindex the object after save to update all catalog metadata
            self.context.reindexObject()
            # notify object edited event
            event.notify(ObjectEditedEvent(self.context))
            self.context.plone_utils.addPortalMessage(message, "info")
        return self.template()
