import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInTwoJetHighCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 2
            and theEventDictionary.eventDictionary['mjj'] > 450.0
            ):
        return True
    else:
        return False
    return False

TwoJetHigh = AnalysisCategoryDef.AnalysisCategory()
TwoJetHigh.name = "mt_2jet_high"
TwoJetHigh.IsInCategory = IsInTwoJetHighCategory
TwoJetHigh.rollingVariable = 'HiggsPt'
TwoJetHigh.rollingBins = [0,45,80,120,200,350,10000]
TwoJetHigh.reconstructionVariable= 'M_sv'
TwoJetHigh.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
