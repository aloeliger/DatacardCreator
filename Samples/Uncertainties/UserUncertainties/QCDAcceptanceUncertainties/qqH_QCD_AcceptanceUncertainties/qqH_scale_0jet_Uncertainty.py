from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_scale_0jet_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'vbf_scale_0jet'
        self.uncertaintyNames = [
            'vbf_scale_0jetUp',
            'vbf_scale_0jetDown',
        ]
        self.eventDictionaryModifications = {
            'vbf_scale_0jetUp':self.CreateScale0JetDictionaryUp,
            'vbf_scale_0jetDown':self.CreateScale0JetDictionaryDown,
        }
    def CreateScale0JetDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_0jet_UP
        return modifiedEventDictionary
    def CreateScale0JetDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_0jet_DOWN
        return modifiedEventDictionary
