from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class WH_scale_wh_lep_Inclusive_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'wh_scale'
        self.uncertaintyNames = [
            'WHlep_scaleUp',
            'WHlep_scaleDown'
        ]
        self.eventDictionaryModifications = {
            'WHlep_scaleUp':self.CreateScaleDictionaryUp,
            'WHlep_scaleDown':self.CreateScaleDictionaryDown,
            }
    def CreateScaleDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_Inclusive_UP
        return modifiedEventDictionary
    def CreateScaleDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleacceptance_VH_scale_Inclusive_DOWN
        return modifiedEventDictionary
