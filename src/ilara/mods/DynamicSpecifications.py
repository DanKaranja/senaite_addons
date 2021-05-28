from bika.lims.interfaces import IDynamicResultsRange
from bika.lims.interfaces.analysis import IRequestAnalysis
from zope.interface import implementer
from bika.lims import logger


@implementer(IDynamicResultsRange)
class DynamicResultsRange(object):

    def __init__(self, analysis):
        self.analysis = analysis

    def __call__(self):
        if not IRequestAnalysis.providedBy(self.analysis):
            # Cannot grab the patient from analyses not assigned to a Sample
            return {}

        # Get the sample's specificaion
        sample = self.analysis.getRequest()
        specification = sample.getSpecification()
        if not specification:
            # No specification, nothing to do
            return {}

        # Dynamic specification
        dyn_spec = specification.getDynamicAnalysisSpec()

        # Get the patient from the sample
        sample = self.analysis.getRequest()
        patient = sample.getField("Patient").get(sample)
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
        ranges = dyn_spec.get_by_keyword().get(keyword)

        # og_range = specification.get_by_keyword().get(keyword)
        # fs = 'Original ranges: %s - %s' % (og_range['min'], og_range['max'])
        # dfs = 'Dynamic ranges: %s - %s' % (ranges['min'], ranges['max'])
        # logger.info('fs')

        if not ranges:
            # No ranges defined for this analysis
            return {}

        # Find a match by age and sex
        for range in ranges:
            return range
                

        # No dynamic specification found for this analysis and patient
        return {}