import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInZeroJetHighCategory(theAnalysisCategory,theEventDictionary):
    if (
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and theEventDictionary.eventDictionary['Njets'] == 0
            and theEventDictionary.eventDictionary['DeltaR'] < 3.0
            and theEventDictionary.eventDictionary['DeltaR'] > 2.0
    ):
        #theAnalysisCategory.dumpRLEFile.write(str(theEventDictionary.eventDictionary['run'])+' '
        #                                      +str(theEventDictionary.eventDictionary['lumi'])+' '
        #                                      +str(theEventDictionary.eventDictionary['evt'])+'\n')
        return True
    else:
        return False
    return False

ZeroJetHigh = AnalysisCategoryDef.AnalysisCategory()
ZeroJetHigh.name = 'mt_0jet_PTH_GE10'
ZeroJetHigh.IsInCategory = IsInZeroJetHighCategory
ZeroJetHigh.rollingVariable = 'TauPt'
ZeroJetHigh.rollingBins = [30.0,40.0,50.0,10000.0]
ZeroJetHigh.reconstructionVariable = 'M_sv'
ZeroJetHigh.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]
#ZeroJetHigh.dumpRLEFile = open ("ZeroJetLowDRDumpFile.txt","w")
