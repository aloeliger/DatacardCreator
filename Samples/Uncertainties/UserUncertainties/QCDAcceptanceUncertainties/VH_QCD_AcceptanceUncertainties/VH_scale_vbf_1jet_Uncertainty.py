from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_scale_vbf_1jet_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_scale_1jet'
        self.uncertaintyNames = [
            'VH_scale_1jetUp',
            'VH_scale_1jetDown',
        ]
        self.eventDictionaryModifications = {
            'VH_scale_1jetUp':self.CreateScale1JetDictionaryUp,
            'VH_scale_1jetDown':self.CreateScale1JetDictionaryDown,
            }
    def CreateScale1JetDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_1jet_UP
        return modifiedEventDictionary
    def CreateScale1JetDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_1jet_DOWN
        return modifiedEventDictionary
