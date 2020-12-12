from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

def getGGZHLLTT_NJETS_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets4UP
    except:
        return theWeight
    return theWeight

def getGGZHNNTT_NJETS_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets4UP
    except:
        return theWeight
    return theWeight

def getGGZHQQTT_NJETS_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets4UP
    except:
        return theWeight
    return theWeight

def getGGZHLLTT_NJETS_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets4DOWN
    except:
        return theWeight
    return theWeight

def getGGZHNNTT_NJETS_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets4DOWN
    except:
        return theWeight
    return theWeight

def getGGZHQQTT_NJETS_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets4DOWN
    except:
        return theWeight
    return theWeight

class GGZH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'GGZH_NJets_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggZHUp',
            'QCDscale_ggZHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggZHUp':self.CreateQCDScaleGGZHDictionaryUp,
            'QCDscale_ggZHDown':self.CreateQCDScaleGGZHDictionaryDown,
        }
    def CreateQCDScaleGGZHDictionaryUp(self,theTree,nominalEventDictionary):
        GGZHLLTTWeight = getGGZHLLTT_NJETS_UpWeight(theTree)
        GGZHNNTTWeight = getGGZHNNTT_NJETS_UpWeight(theTree)
        GGZHQQTTWeight = getGGZHQQTT_NJETS_UpWeight(theTree)

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
        GGZHLLTTWeight = getGGZHLLTT_NJETS_DownWeight(theTree)
        GGZHNNTTWeight = getGGZHNNTT_NJETS_DownWeight(theTree)
        GGZHQQTTWeight = getGGZHQQTT_NJETS_DownWeight(theTree)

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
