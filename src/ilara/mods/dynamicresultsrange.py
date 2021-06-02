from bika.lims.interfaces import IDynamicResultsRange
from bika.lims.interfaces.analysis import IRequestAnalysis
from zope.interface import implementer
from bika.lims import logger


@implementer(IDynamicResultsRange)
class DynamicResultsRange(object):

    def __init__(self, analysis):
        self.analysis = analysis
        self.analysisrequest = analysis.getRequest()
        self.specification = self.analysisrequest.getSpecification()
        self.dynamicspec = None
        if self.specification:
            self.dynamicspec = self.specification.getDynamicAnalysisSpec()

    def __call__(self):
        if not IRequestAnalysis.providedBy(self.analysis):
            # Cannot grab the patient from analyses not assigned to a Sample
            return {}

        # Get the sample's specificaion
        if not self.specification:
            # No specification, nothing to do
            return {}

        # Get the patient from the sample
        patient = sample.getField("Patlient").get(self.analysisrequest)
        if not patient:
            # No patient assigned for this sample, do nothing
            return {}

        # Patient's age (in years)
        age = patient.getAge()
        # Patient's gender (male/female/dk)
        sex = patient.getGender()

        # Get the dynamic specification for this analysis by keyword
        # We expect the xls to have the columns "keyword", "age" and "sex"
        keyword = self.analysis.getKeyword()
        ranges = self.dynamicspec.get_by_keyword().get(keyword)

        if not ranges:
            # No ranges defined for this analysis
            return {}

        # Find a match by age and sex
        for range in ranges:
            if range.get("sex") == sex:
                return range

        # No dynamic specification found for this analysis and patient
        return {}