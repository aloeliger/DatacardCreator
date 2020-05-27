from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_scale_Inclusive_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'vbf_scale'
        self.uncertaintyNames = [
            'vbf_scaleUp',
            'vbf_scaleDown',
        ]
        self.eventDictionaryModifications = {
            'vbf_scaleUp':self.CreateScaleDictionaryUp,
            'vbf_scaleDown':self.CreateScaleDictionaryDown,
        }
    def CreateScaleDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_Inclusive_UP
        return modifiedEventDictionary
    def CreateScaleDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_Inclusive_DOWN
        return modifiedEventDictionary
