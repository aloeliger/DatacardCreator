from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggZH_scale_0jet_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_0jet'
        self.uncertaintyNames = [
            'ggH_scale_0jetUp',
            'ggH_scale_0jetDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_0jetUp':self.CreateScale0JetDictionaryUp,
            'ggH_scale_0jetDown':self.CreateScale0JetDictionaryDown,
        }
    def CreateScale0JetDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_0jet_UP
        return modifiedEventDictionary

    def CreateScale0JetDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_0jet_DOWN
        return modifiedEventDictionary
