from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_scale_vbf_0jet_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_scale_0jet'
        self.uncertaintyNames = [
            'VH_scale_0jetUp',
            'VH_scale_0jetDown',
        ]
        self.eventDictionaryModifications = {
            'VH_scale_0jetUp':self.CreateScale0JetDictionaryUp,
            'VH_scale_0jetDown':self.CreateScale0JetDictionaryDown,
            }
    def CreateScale0JetDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_0jet_UP
        return modifiedEventDictionary

    def CreateScale0JetDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_0jet_DOWN
        return modifiedEventDictionary
