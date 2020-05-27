from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_scale_highmjj_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'vbf_scale_highmjj_lowpt'
        self.uncertaintyNames = [
            'vbf_scale_highmjj_lowptUp',
            'vbf_scale_highmjj_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'vbf_scale_highmjj_lowptUp':self.CreateScaleHighMjjLowPtDictionaryUp,
            'vbf_scale_highmjj_lowptDown':self.CreateScaleHighMjjLowPtDictionaryDown,
        }
    def CreateScaleHighMjjLowPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_highmjj_lowpt_UP
        return modifiedEventDictionary

    def CreateScaleHighMjjLowPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_highmjj_lowpt_DOWN
        return modifiedEventDictionary
