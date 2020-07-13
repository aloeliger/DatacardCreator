import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInIntermediateTauPtCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary["TauPt"] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary["TauPt"] >= 50.0
            and theEventDictionary.eventDictionary["TauPt"] <= 70.0
    ):
        return True
    else:
        return False
    return False

IntermediateTauPtCategory = AnalysisCategoryDef.AnalysisCategory()
IntermediateTauPtCategory.name = 'mt_IntermediateTauPt_HiggsPt'
IntermediateTauPtCategory.IsInCategory = IsInIntermediateTauPtCategory
IntermediateTauPtCategory.rollingVariable = 'HiggsPt'
IntermediateTauPtCategory.rollingBins = [0,45,80,120,200,350,450,100000000]
IntermediateTauPtCategory.reconstructionVariable = 'M_sv'
IntermediateTauPtCategory.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]
