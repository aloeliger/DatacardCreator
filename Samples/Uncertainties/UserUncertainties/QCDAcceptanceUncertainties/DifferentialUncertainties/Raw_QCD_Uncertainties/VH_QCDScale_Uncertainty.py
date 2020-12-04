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
        try:            
            modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_VHUP
        except:
            pass
        return modifiedEventDictionary

    def CreateQCDScaleVHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:            
            modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_VHDOWN
        except:
            pass
        return modifiedEventDictionary
