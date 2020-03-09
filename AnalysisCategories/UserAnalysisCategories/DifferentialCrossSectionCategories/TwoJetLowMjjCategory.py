import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInTwoJetLowCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 2
            and theEventDictionary.eventDictionary['mjj'] < 450.0
            ):
        return True
    else:
        return False
    return False

TwoJetLow = AnalysisCategoryDef.AnalysisCategory()
TwoJetLow.name = "mt_2jetlow"
TwoJetLow.IsInCategory = IsInTwoJetLowCategory
TwoJetLow.rollingVariable = 'HiggsPt'
TwoJetLow.rollingBins = [0,20,45,80,120,200,350,10000]
TwoJetLow.reconstructionVariable= 'M_sv'
TwoJetLow.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
