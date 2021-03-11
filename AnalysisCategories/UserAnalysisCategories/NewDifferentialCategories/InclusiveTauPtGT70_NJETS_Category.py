import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInHighTauPtCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary["TauPt"] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary["TauPt"] >= 70.0
            and not (theEventDictionary.eventDictionary['Njets'] == 0 and theEventDictionary.eventDictionary['DeltaR'] < 2.0)
    ):
        return True
    else:
        return False
    return False

HighTauPtCategory = AnalysisCategoryDef.AnalysisCategory()
HighTauPtCategory.name = 'htt_NJ_mt_HighTauPt'
HighTauPtCategory.IsInCategory = IsInHighTauPtCategory
HighTauPtCategory.rollingVariable = 'Njets'
HighTauPtCategory.rollingBins = [0,1,2,3,4,20]
HighTauPtCategory.reconstructionVariable = 'M_sv'
HighTauPtCategory.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]
#HighTauPtCategory.reconstructionBins = [75.0,90.0,105.0,120.0,135.0,150.0,170.0,190.0,210,250.0]
