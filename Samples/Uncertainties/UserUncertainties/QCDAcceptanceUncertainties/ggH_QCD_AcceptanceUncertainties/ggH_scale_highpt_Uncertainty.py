from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_scale_ggH_highpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_highpt'
        self.uncertaintyNames = [
            'ggH_scale_highptUp',
            'ggH_scale_highptDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_highptUp':self.CreateScaleHighPtDictionaryUp,
            'ggH_scale_highptDown':self.CreateScaleHighPtDictionaryDown,
        }
    def CreateScaleHighPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_highpt_UP
        return modifiedEventDictionary

    def CreateScaleHighPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_highpt_DOWN
        return modifiedEventDictionary
