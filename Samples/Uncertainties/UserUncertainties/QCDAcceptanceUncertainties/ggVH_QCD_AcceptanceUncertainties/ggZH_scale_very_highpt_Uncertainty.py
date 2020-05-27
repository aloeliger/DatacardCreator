from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggZH_scale_very_highpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_very_highpt'
        self.uncertaintyNames = [
            'ggH_scale_very_highptUp',
            'ggH_scale_very_highptDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_very_highptUp':self.CreateScaleVeryHighPtDictionaryUp,
            'ggH_scale_very_highptDown':self.CreateScaleVeryHighPtDictionaryDown,
        }
    def CreateScaleVeryHighPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_very_highpt_UP
        return modifiedEventDictionary
    def CreateScaleVeryHighPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_very_highpt_DOWN
        return modifiedEventDictionary
