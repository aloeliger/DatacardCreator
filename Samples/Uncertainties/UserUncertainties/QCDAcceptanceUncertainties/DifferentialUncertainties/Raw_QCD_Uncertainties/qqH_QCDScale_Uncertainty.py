from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'qqH_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_qqHUp',
            'QCDscale_qqHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_qqHUp':self.CreateQCDScaleqqHDictionaryUp,
            'QCDscale_qqHDown':self.CreateQCDScaleqqHDictionaryDown,
        }
    def CreateQCDScaleqqHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_qqHUP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

            
    def CreateQCDScaleqqHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_qqHDOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

