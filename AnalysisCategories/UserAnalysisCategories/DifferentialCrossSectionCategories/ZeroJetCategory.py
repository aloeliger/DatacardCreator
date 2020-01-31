import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInZeroJetCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 0
            ):
        return True
    else:
        return False
    return False

ZeroJet = AnalysisCategoryDef.AnalysisCategory()
ZeroJet.name = "mt_0jet"
ZeroJet.IsInCategory = IsInZeroJetCategory
ZeroJet.rollingVariable = 'HiggsPt'
ZeroJet.rollingBins = [0,20,45,80,120,200,350,10000]
ZeroJet.reconstructionVariable= 'M_sv'
ZeroJet.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
