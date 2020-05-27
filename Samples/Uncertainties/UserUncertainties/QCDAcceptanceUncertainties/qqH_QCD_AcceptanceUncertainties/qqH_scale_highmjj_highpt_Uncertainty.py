from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_scale_highmjj_highpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'vbf_scale_highmjj_highpt'
        self.uncertaintyNames = [
            'vbf_scale_highmjj_highptUp',
            'vbf_scale_highmjj_highptDown',
        ]
        self.eventDictionaryModifications = {
            'vbf_scale_highmjj_highptUp':self.CreateScaleHighMjjHighPtDictionaryUp,
            'vbf_scale_highmjj_highptDown':self.CreateScaleHighMjjHighPtDictionaryDown,
        }
    def CreateScaleHighMjjHighPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_highmjj_highpt_UP
        return modifiedEventDictionary
    def CreateScaleHighMjjHighPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VBF_scale_highmjj_highpt_DOWN
        return modifiedEventDictionary
