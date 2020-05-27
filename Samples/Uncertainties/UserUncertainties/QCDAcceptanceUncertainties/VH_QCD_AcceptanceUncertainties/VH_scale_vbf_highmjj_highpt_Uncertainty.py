from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_scale_vbf_highmjj_highpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_scale_highmjj_highpt'
        self.uncertaintyNames=[
            'VH_scale_highmjj_highptUp',
            'VH_scale_highmjj_highptDown',
        ]
        self.eventDictionaryModifications = {
            'VH_scale_highmjj_highptUp':self.CreateScaleHighMjjHighPtDictionaryUp,
            'VH_scale_highmjj_highptDown':self.CreateScaleHighMjjHighPtDictionaryDown,
            }
    def CreateScaleHighMjjHighPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highmjj_highpt_UP
        return modifiedEventDictionary

    def CreateScaleHighMjjHighPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highmjj_highpt_DOWN
        return modifiedEventDictionary
