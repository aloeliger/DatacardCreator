import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInHighTauPtCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary["TauPt"] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary["TauPt"] >= 70.0
            and not (theEventDictionary.eventDictionary['Njets'] == 0 and theEventDictionary.eventDictionary['DeltaR'] < 2.0)
            and not (abs(theEventDictionary.eventDictionary['TauEta'])>0.2 and abs(theEventDictionary.eventDictionary['TauEta'])<0.3)
    ):
        return True
    else:
        return False
    return False

HighTauPtCategory = AnalysisCategoryDef.AnalysisCategory()
HighTauPtCategory.name = 'htt_PTH_mt_HighTauPt'
HighTauPtCategory.IsInCategory = IsInHighTauPtCategory
HighTauPtCategory.rollingVariable = 'HiggsPt'
HighTauPtCategory.rollingBins = [0,45,80,120,200,350,450,100000000]
HighTauPtCategory.reconstructionVariable = 'M_sv'
HighTauPtCategory.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]
