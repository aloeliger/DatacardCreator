from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggZH_scale_1jet_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_1jet_lowpt'
        self.uncertaintyNames = [
            'ggH_scale_1jet_lowptUp',
            'ggH_scale_1jet_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_1jet_lowptUp':self.CreateScale1JetLowPtDictionaryUp,
            'ggH_scale_1jet_lowptDown':self.CreateScale1JetLowPtDictionaryDown
        }
    def CreateScale1JetLowPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_1jet_lowpt_UP
        return modifiedEventDictionary
    def CreateScale1JetLowPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggVH_scale_1jet_lowpt_DOWN
        return modifiedEventDictionary
