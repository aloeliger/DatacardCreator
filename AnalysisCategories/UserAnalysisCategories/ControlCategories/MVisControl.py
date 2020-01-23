import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInInclusiveCategory(theAnalysisCategory,theEventDictionary):
    isGoodEvent = False
    if(theEventDictionary.eventDictionary["TauPt"] > 30.0
       and theEventDictionary.eventDictionary["MT"] < 50.0):
        isGoodEvent = True
    return isGoodEvent

MTInclusive = AnalysisCategoryDef.AnalysisCategory()
MTInclusive.name = "mvis"
MTInclusive.IsInCategory = IsInInclusiveCategory
MTInclusive.rollingVariable = "TauPt"
MTInclusive.rollingBins = [0.0,9000.0]
MTInclusive.reconstructionVariable = "MVis"
MTInclusive.reconstructionBins = [50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0,
                                  105.0,110.0,115.0,120.0,125.0,130.0,135.0,140.0,145.0,150.0,
                                  155.0,160.0,165.0,170.0,175.0,180.0,185.0,190.0,195.0,200.0]
