from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_VHUp',
            'QCDscale_VHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_VHUp':self.CreateQCDScaleVHDictionaryUp,
            'QCDscale_VHDown':self.CreateQCDScaleVHDictionaryDown,
        }
    def CreateQCDScaleVHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_VHUP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary


    def CreateQCDScaleVHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_VHDOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

