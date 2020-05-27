from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_scale_vbf_lowmjj_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_scale)_lowmjj'
        self.uncertaintyNames = [
            'VH_scale_lowmjjUp',
            'VH_scale_lowmjjDown',
        ]
        self.eventDictionaryModifications = {
            'VH_scale_lowmjjUp':self.CreateScaleLowmjjDictionaryUp,
            'VH_scale_lowmjjDown':self.CreateScaleLowmjjDictionaryDown,
            }
    def CreateScaleLowmjjDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_lowmjj_UP
        return modifiedEventDictionary
    def CreateScaleLowmjjDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_lowmjj_DOWN
        return modifiedEventDictionary
