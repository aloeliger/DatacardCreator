from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggZH_scale_Inclusive_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale'
        self.uncertaintyNames = [
            'ggH_scaleUp',
            'ggH_scaleDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scaleUp':self.CreateScaleDictionaryUp,
            'ggH_scaleDown':self.CreateScaleDictionaryDown,
        }
    def CreateScaleDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_Inclusive_UP
        return modifiedEventDictionary

    def CreateScaleDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_Inclusive_DOWN
        return modifiedEventDictionary
