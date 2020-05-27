from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_scale_lowmjj_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'vbf_scale_lowmjj'
        self.uncertaintyNames = [
            'vbf_scale_lowmjjUp',
            'vbf_scale_lowmjjDown',
        ]
        self.eventDictionaryModifications = {
            'vbf_scale_lowmjjUp':self.CreateScaleLowmjjDictionaryUp,
            'vbf_scale_lowmjjDown':self.CreateScaleLowmjjDictionaryDown,
        }
    def CreateScaleLowmjjDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_lowmjj_UP
        return modifiedEventDictionary
    def CreateScaleLowmjjDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_lowmjj_DOWN
        return modifiedEventDictionary
