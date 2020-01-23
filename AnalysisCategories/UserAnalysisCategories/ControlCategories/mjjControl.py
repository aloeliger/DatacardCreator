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
MTInclusive.name = "mjj"
MTInclusive.IsInCategory = IsInInclusiveCategory
MTInclusive.rollingVariable = "TauPt"
MTInclusive.rollingBins = [0.0,9000.0]
MTInclusive.reconstructionVariable = "mjj"
MTInclusive.reconstructionBins = [0.0,25.0,50.0,75.0,100.0,125.0,150.0,175.0,200.0,225.0,250.0,
                                  275.0,300.0,325.0,350.0,375.0,400.0,425.0,450.0,475.0,500.0,]
