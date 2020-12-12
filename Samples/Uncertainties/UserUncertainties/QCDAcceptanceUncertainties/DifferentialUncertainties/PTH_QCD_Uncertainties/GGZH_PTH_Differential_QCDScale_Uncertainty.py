from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

def getGGZHLLTT_PTH_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_gt450UP
    except:
        return theWeight
    return theWeight

def getGGZHLLTT_PTH_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_gt450DOWN
    except:
        return theWeight
    return theWeight

def getGGZHNNTT_PTH_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_gt450UP
    except:
        return theWeight
    return theWeight

def getGGZHNNTT_PTH_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_gt450DOWN
    except:
        return theWeight
    return theWeight

def getGGZHQQTT_PTH_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_gt450UP
    except:
        return theWeight
    return theWeight

def getGGZHQQTT_PTH_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_gt450DOWN
    except:
        return theWeight
    return theWeight

class GGZH_PTH_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'GGZH_PTH_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggZHUp',
            'QCDscale_ggZHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggZHUp':self.CreateQCDScaleGGZHDictionaryUp,
            'QCDscale_ggZHDown':self.CreateQCDScaleGGZHDictionaryDown,
        }
    def CreateQCDScaleGGZHDictionaryUp(self,theTree,nominalEventDictionary):
        GGZHLLTTWeight = getGGZHLLTT_PTH_UpWeight(theTree)
        GGZHNNTTWeight = getGGZHNNTT_PTH_UpWeight(theTree)
        GGZHQQTTWeight = getGGZHQQTT_PTH_UpWeight(theTree)

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
        GGZHLLTTWeight = getGGZHLLTT_PTH_DownWeight(theTree)
        GGZHNNTTWeight = getGGZHNNTT_PTH_DownWeight(theTree)
        GGZHQQTTWeight = getGGZHQQTT_PTH_DownWeight(theTree)

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

