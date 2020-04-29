import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInFourJetCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] >= 4
            ):
        return True
    else:
        return False
    return False

FourJet = AnalysisCategoryDef.AnalysisCategory()
FourJet.name = "mt_4jet"
FourJet.IsInCategory = IsInFourJetCategory
FourJet.rollingVariable = 'HiggsPt'
FourJet.rollingBins = [0,45,80,120,200,350,10000]
FourJet.reconstructionVariable= 'M_sv'
FourJet.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
