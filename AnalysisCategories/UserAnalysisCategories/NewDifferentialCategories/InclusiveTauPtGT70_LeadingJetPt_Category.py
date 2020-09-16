import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInHighTauPtCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary["TauPt"] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary["TauPt"] >= 70.0
            #and theEventDictionary.eventDictionary['Njets'] >= 1
            and not (theEventDictionary.eventDictionary['Njets'] == 0 and theEventDictionary.eventDictionary['DeltaR'] < 2.0)
    ):
        return True
    else:
        return False
    return False

HighTauPtCategory = AnalysisCategoryDef.AnalysisCategory()
HighTauPtCategory.name = 'mt_HighTauPt_LeadingJetPt'
HighTauPtCategory.IsInCategory = IsInHighTauPtCategory
HighTauPtCategory.rollingVariable = 'LJetPt'
HighTauPtCategory.rollingBins = [0,30,60,120,200,350,100000000]
HighTauPtCategory.reconstructionVariable = 'M_sv'
HighTauPtCategory.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]
