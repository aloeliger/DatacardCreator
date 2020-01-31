import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInInclusiveCategory(theAnalysisCategory,theEventDictionary):
    isGoodEvent = False
    if(theEventDictionary.eventDictionary["TauPt"] > 30.0
       and theEventDictionary.eventDictionary["MT"] < 50.0
       and theEventDictionary.eventDictionary["Njets"] >= 2.0):
        isGoodEvent = True
    return isGoodEvent

MTInclusive = AnalysisCategoryDef.AnalysisCategory()
MTInclusive.name = "DEtaJJ"
MTInclusive.IsInCategory = IsInInclusiveCategory
MTInclusive.rollingVariable = "TauPt"
MTInclusive.rollingBins = [0.0,9000.0]
MTInclusive.reconstructionVariable = "DEtaJJ"
MTInclusive.reconstructionBins = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,
                                  1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
                                  2.1,2.2,2.3,2.4,2.5]
