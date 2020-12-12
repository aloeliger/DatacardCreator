from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

def getGGZHLLTT_J1PT_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60UP
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120UP
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200UP
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350UP
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350UP
    except:
        return theWeight
    return theWeight

def getGGZHNNTT_J1PT_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60UP
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120UP
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200UP
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350UP
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350UP
    except:
        return theWeight
    return theWeight

def getGGZHQQTT_J1PT_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60UP
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120UP
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200UP
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350UP
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350UP
    except:
        return theWeight
    return theWeight

def getGGZHLLTT_J1PT_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60DOWN
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120DOWN
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200DOWN
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350DOWN
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350DOWN
    except:
        return theWeight
    return theWeight

def getGGZHNNTT_J1PT_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60DOWN
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120DOWN
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200DOWN
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350DOWN
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350DOWN
    except:
        return theWeight
    return theWeight

def getGGZHQQTT_J1PT_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60DOWN
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120DOWN
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200DOWN
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350DOWN
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350DOWN
    except:
        return theWeight
    return theWeight

class GGZH_J1PT_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'GGZH_J1PT_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggZHUp',
            'QCDscale_ggZHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggZHUp':self.CreateQCDScaleGGZHDictionaryUp,
            'QCDscale_ggZHDown':self.CreateQCDScaleGGZHDictionaryDown,
        }
    def CreateQCDScaleGGZHDictionaryUp(self,theTree,nominalEventDictionary):        
        GGZHLLTTWeight = getGGZHLLTT_J1PT_UpWeight(theTree)
        GGZHNNTTWeight = getGGZHNNTT_J1PT_UpWeight(theTree)
        GGZHQQTTWeight = getGGZHQQTT_J1PT_UpWeight(theTree)

        if GGZHLLTTWeight == 0 and GGZHNNTTWeight == 0 and GGZHQQTTWeight == 0:
            return nominalEventDictionary
        else:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            if GGZHLLTTWeight != 0:
                modifiedEventDictionary.Weight = GGZHLLTTWeight
            elif GGZHNNTTWeight != 0:
                modifiedEventDictionary.Weight = GGZHNNTTWeight
            elif GGZHQQTTWeight != 0:
                modifiedEventDictionary.Weight = GGZHQQTTWeight
            return modifiedEventDictionary

    def CreateQCDScaleGGZHDictionaryDown(self,theTree,nominalEventDictionary):
        GGZHLLTTWeight = getGGZHLLTT_J1PT_DownWeight(theTree)
        GGZHNNTTWeight = getGGZHNNTT_J1PT_DownWeight(theTree)
        GGZHQQTTWeight = getGGZHQQTT_J1PT_DownWeight(theTree)

        if GGZHLLTTWeight == 0 and GGZHNNTTWeight == 0 and GGZHQQTTWeight == 0:
            return nominalEventDictionary
        else:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            if GGZHLLTTWeight != 0:
                modifiedEventDictionary.Weight = GGZHLLTTWeight
            elif GGZHNNTTWeight != 0:
                modifiedEventDictionary.Weight = GGZHNNTTWeight
            elif GGZHQQTTWeight != 0:
                modifiedEventDictionary.Weight = GGZHQQTTWeight
            return modifiedEventDictionary
