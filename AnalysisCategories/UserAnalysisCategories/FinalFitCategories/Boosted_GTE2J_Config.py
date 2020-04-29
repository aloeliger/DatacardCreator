import ROOT
import AnalysisCategories.AnalysisCategoryDef as AnalysisCategoryDef

def IsInBoostedGTETwoJetCategory(theAnalysisCategory,theEventDictionary):
    if(
            theEventDictionary.eventDictionary['TauPt'] >= 30.0
            and theEventDictionary.eventDictionary['MT'] < 50.0
            and (theEventDictionary.eventDictionary['Njets'] == 1.0 or (theEventDictionary.eventDictionary['Njets'] >= 2.0 and theEventDictionary.eventDictionary['mjj'] <= 350.0))
            and theEventDictionary.eventDictionary['Njets'] >= 2.0
    ):
        #theAnalysisCategory.dumpRLEFile.write(str(theEventDictionary.eventDictionary['run'])+' '
        #                                      +str(theEventDictionary.eventDictionary['lumi'])+' '
        #                                      +str(theEventDictionary.eventDictionary['evt'])+'\n')
        #if (theEventDictionary.eventDictionary['HiggsPt'] > 250
        #    and theEventDictionary.eventDictionary['M_sv'] > 90
        #    and theEventDictionary.eventDictionary['M_sv'] < 110):
        #    print theEventDictionary.Weight
        return True
    else:
        return False
    return False

BoostedGTE2J = AnalysisCategoryDef.AnalysisCategory()
BoostedGTE2J.name = 'mt_boosted_GE2J'
BoostedGTE2J.IsInCategory = IsInBoostedGTETwoJetCategory
BoostedGTE2J.rollingVariable = 'HiggsPt'
BoostedGTE2J.rollingBins=[0.0,60.0,120.0,200.0,250.0,10000.0]
#BoostedGTE2J.rollingBins=[0.0,60.0,120.0,200.0,300.0,10000.0]
BoostedGTE2J.reconstructionVariable = 'M_sv'
BoostedGTE2J.reconstructionBins = [50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0]
#BoostedGTE2J.dumpRLEFile = open ("BoostedGE2JDumpFile.txt","w")
