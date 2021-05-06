
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from bika.health import utils
from bika.lims.browser.analysisrequest import AnalysisRequestViewView as BaseAnalysisRequestViewView
from .header_table import HeaderTableView


class AnalysisRequestViewView(BaseAnalysisRequestViewView):
    """Main AR View
    """

    def __call__(self):
        # If the analysis request has been received and hasn't been yet
        # verified yet, redirect the user to manage_results view, but only if
        # the user has privileges to Edit(Field)Results, cause otherwise she/he
        # will receive an InsufficientPrivileges error!
        if (self.request.PATH_TRANSLATED.endswith(self.context.id) and
            self.can_edit_results() and self.can_edit_field_results() and
           self.is_received() and not self.is_verified()):

            # Redirect to manage results view if not cancelled
            if not self.is_cancelled():
                manage_results_url = "{}/{}".format(
                    self.context.absolute_url(), "manage_results")
                return self.request.response.redirect(manage_results_url)

        # render header table
        self.header_table = HeaderTableView(self.context, self.request)()

        # Create the ResultsInterpretation by department view
        self.riview = ARResultsInterpretationView(self.context, self.request)

        return self.template()