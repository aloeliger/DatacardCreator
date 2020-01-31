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
MTInclusive.name = "jpt_1"
MTInclusive.IsInCategory = IsInInclusiveCategory
MTInclusive.rollingVariable = "TauPt"
MTInclusive.rollingBins = [0.0,9000.0]
MTInclusive.reconstructionVariable = "LJetPt"
MTInclusive.reconstructionBins = [0.0,4.0,8.0,12.0,16.0,20.0,24.0,28.0,32.0,36.0,40.0,
                                  44.0,48.0,52.0,56.0,60.0,64.0,68.0,72.0,76.0,80.0,
                                  84.0, 88.0, 92.0, 96.0, 100.0, 104.0, 108.0, 112.0, 116.0, 120.0,
                                  124.0, 128.0, 132.0, 136.0, 140.0, 144.0, 148.0, 152.0, 156.0, 160.0,
                                  164.0, 168.0, 172.0, 176.0, 180.0, 184.0, 188.0, 192.0, 196.0, 200.0]
