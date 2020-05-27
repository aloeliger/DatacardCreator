from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_scale_ggH_2jet_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_scale_2jet_lowpt'
        self.uncertaintyNames = [
            'ggH_scale_2jet_lowptUp',
            'ggH_scale_2jet_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'ggH_scale_2jet_lowptUp':self.CreateScale2JetLowPtDictionaryUp,
            'ggH_scale_2jet_lowptDown':self.CreateScale2JetLowPtDictionaryDown,
        }
    def CreateScale2JetLowPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_2jet_lowpt_UP
        return modifiedEventDictionary
    def CreateScale2JetLowPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_ggH_scale_2jet_lowpt_DOWN
        return modifiedEventDictionary
    
