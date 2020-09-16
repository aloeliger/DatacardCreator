import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInLowTauPtCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary["TauPt"] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary["TauPt"] <= 50.0
    ):
        return True
    else:
        return False
    return False

LowTauPtCategory = AnalysisCategoryDef.AnalysisCategory()
LowTauPtCategory.name = 'mt_LowTauPt_HiggsPt'
LowTauPtCategory.IsInCategory = IsInLowTauPtCategory
LowTauPtCategory.rollingVariable = 'HiggsPt'
LowTauPtCategory.rollingBins = [0,45,80,120,200,350,450,100000000]
LowTauPtCategory.reconstructionVariable = 'M_sv'
LowTauPtCategory.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]