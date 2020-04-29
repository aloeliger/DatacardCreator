import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInOneJetCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 1
            ):
        return True
    else:
        return False
    return False

OneJet = AnalysisCategoryDef.AnalysisCategory()
OneJet.name = "mt_1jet"
OneJet.IsInCategory = IsInOneJetCategory
OneJet.rollingVariable = 'HiggsPt'
OneJet.rollingBins = [0,45,80,120,200,350,10000]
OneJet.reconstructionVariable= 'M_sv'
OneJet.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,9000.0]
