import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInInclusiveCategory(theAnalysisCategory,theEventDictionary):
    isGoodEvent = False
    if(theEventDictionary.eventDictionary["TauPt"] > 30.0
       and theEventDictionary.eventDictionary["MT"] < 50.0
       and theEventDictionary.eventDictionary["Njets"] >= 1.0):
        isGoodEvent = True
    return isGoodEvent

MTInclusive = AnalysisCategoryDef.AnalysisCategory()
MTInclusive.name = "jeta_1"
MTInclusive.IsInCategory = IsInInclusiveCategory
MTInclusive.rollingVariable = "TauPt"
MTInclusive.rollingBins = [0.0,9000.0]
MTInclusive.reconstructionVariable = "LJetEta"
MTInclusive.reconstructionBins = [-5.0,-4.9,-4.8,-4.7,-4.6,-4.5,-4.4,-4.3,-4.2,-4.1,-4.0,
                                  -3.9,-3.8,-3.7,-3.6,-3.5,-3.4,-3.3,-3.2,-3.1,-3.0,
                                  -2.9,-2.8,-2.7,-2.6,-2.5,-2.4,-2.3,-2.2,-2.1,-2.0,
                                  -1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1,-1.0,
                                  -0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,
                                  0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,
                                  1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
                                  2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,
                                  3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0,
                                  4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5.0]
