from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_scale_vbf_highmjj_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_highmjj_lowpt'
        self.uncertaintyNames = [
            'VH_scale_highmjj_lowptUp',
            'VH_scale_highmjj_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'VH_scale_highmjj_lowptUp':self.CreateScaleHighMjjLowPtDictionaryUp,
            'VH_scale_highmjj_lowptDown':self.CreateScaleHighMjjLowPtDictionaryDown,
        }
    def CreateScaleHighMjjLowPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highmjj_lowpt_UP
        return modifiedEventDictionary

    def CreateScaleHighMjjLowPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highmjj_lowpt_DOWN
        return modifiedEventDictionary
