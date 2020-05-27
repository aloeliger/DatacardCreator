from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ZH_scale_zh_lep_Inclusive_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'zh_scale'
        self.uncertaintyNames = [
            'ZHlep_scaleUp',
            'ZHlep_scaleDown',
        ]
        self.eventDictionaryModifications = {
            'ZHlep_scaleUp':self.CreateScaleDictionaryUp,
            'ZHlep_scaleDown':self.CreateScaleDictionaryDown,
        }
    def CreateScaleDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_Inclusive_UP
        return modifiedEventDictionary
    def CreateScaleDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleacceptance_VH_scale_Inclusive_DOWN
        return modifiedEventDictionary
