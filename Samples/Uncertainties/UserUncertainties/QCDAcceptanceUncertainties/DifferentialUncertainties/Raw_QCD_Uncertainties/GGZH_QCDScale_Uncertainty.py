from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggZH_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggZH_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggZHUp',
            'QCDscale_ggZHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggZHUp':self.CreateQCDScaleggZHDictionaryUp,
            'QCDscale_ggZHDown':self.CreateQCDScaleggZHDictionaryDown,
        }
    def CreateQCDScaleggZHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_ggZHUP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary


    def CreateQCDScaleggZHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_ggZHDOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

