import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInInclusiveCategory(theAnalysisCategory,theEventDictionary):
    isGoodEvent = False
    if(theEventDictionary.eventDictionary["TauPt"] > 30.0
       and theEventDictionary.eventDictionary["MT"] < 50.0):
        isGoodEvent = True
    return isGoodEvent

MTInclusive = AnalysisCategoryDef.AnalysisCategory()
MTInclusive.name = "mupt"
MTInclusive.IsInCategory = IsInInclusiveCategory
MTInclusive.rollingVariable = "TauPt"
MTInclusive.rollingBins = [0.0,9000.0]
MTInclusive.reconstructionVariable = "MuPt"
MTInclusive.reconstructionBins = [20.0,22.0,24.0,26.0,28.0,30.0,32.0,34.0,36.0,38.0,40.0,
                                  42.0,44.0,46.0,48.0,50.0,52.0,54.0,56.0,58.0,60.0,
                                  62.0,64.0,66.0,68.0,70.0,72.0,74.0,76.0,78.0,80.0]
