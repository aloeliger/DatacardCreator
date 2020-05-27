from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_scale_Inclusive_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_scale'
        self.uncertaintyNames = [
            'VH_scaleUp',
            'VH_scaleDown',
        ]
        self.eventDictionaryModifications = {
            'VH_scaleUp':self.CreateScaleDictionaryUp,
            'VH_scaleDown':self.CreateScaleDictionaryDown,
        }
    def CreateScaleDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_Inclusive_UP
        return modifiedEventDictionary
    def CreateScaleDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleacceptance_VH_scale_Inclusive_DOWN
        return modifiedEventDictionary
