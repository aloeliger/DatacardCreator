from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_scale_vbf_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_vbf'
        self.uncertaintyNames = [
            'ggH_scale_vbfUp',
            'ggH_scale_vbfDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_vbfUp':self.CreateScaleVbfDictionaryUp,
            'ggH_scale_vbfDown':self.CreateScaleVbfDictionaryDown,
        }
    def CreateScaleVbfDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_vbf_UP
        return modifiedEventDictionary
    def CreateScaleVbfDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_vbf_DOWN
        return modifiedEventDictionary
