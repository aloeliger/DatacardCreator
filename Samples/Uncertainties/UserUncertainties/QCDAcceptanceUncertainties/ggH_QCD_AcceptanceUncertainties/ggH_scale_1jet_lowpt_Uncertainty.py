from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_scale_ggH_1jet_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_1jet'
        self.uncertaintyNames = [
            'ggH_scale_1jet_lowptUp',
            'ggH_scale_1jet_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_1jet_lowptUp':self.CreateScale1JetDictionaryUp,
            'ggH_scale_1jet_lowptDown':self.CreateScale1JetDictionaryDown,
        }
    def CreateScale1JetDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_1jet_lowpt_UP
        return modifiedEventDictionary
    def CreateScale1JetDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_1jet_lowpt_DOWN
        return modifiedEventDictionary
