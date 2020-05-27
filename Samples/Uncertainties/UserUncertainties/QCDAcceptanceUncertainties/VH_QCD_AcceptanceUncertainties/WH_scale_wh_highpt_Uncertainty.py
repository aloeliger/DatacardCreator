from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class WH_scale_wh_highpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'wh_scale_highpt'
        self.uncertaintyNames = [
            'WH_scale_highptUp',
            'WH_scale_highptDown',
        ]
        self.eventDictionaryModifications = {
            'WH_scale_highptUp':self.CreateScaleHighPtDictionaryUp,
            'WH_scale_highptDown':self.CreateScaleHighPtDictionaryDown,
            }
    def CreateScaleHighPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highpt_UP
        return modifiedEventDictionary
    def CreateScaleHighPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highpt_DOWN
        return modifiedEventDictionary
