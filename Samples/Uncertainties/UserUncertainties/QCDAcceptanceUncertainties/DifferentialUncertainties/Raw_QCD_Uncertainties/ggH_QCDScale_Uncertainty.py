from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggHUp',
            'QCDscale_ggHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggHUp':self.CreateQCDScaleggHDictionaryUp,
            'QCDscale_ggHDown':self.CreateQCDScaleggHDictionaryDown,
        }
    def CreateQCDScaleggHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_ggHUP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary


    def CreateQCDScaleggHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_ggHDOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

