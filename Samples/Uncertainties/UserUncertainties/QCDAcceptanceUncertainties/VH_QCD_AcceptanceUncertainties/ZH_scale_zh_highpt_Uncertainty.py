from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ZH_scale_zh_highpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ZH_scale_highpt'
        self.uncertaintyNames = [
            'ZH_scale_highptUp',
            'ZH_scale_highptDown',
        ]
        self.eventDictionaryModifications = {
            'ZH_scale_highptUp':self.CreateScaleHighPtDictionaryUp,
            'ZH_scale_highptDown':self.CreateScaleHighPtDictionaryDown,
            }
    def CreateScaleHighPtDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highpt_UP
        return modifiedEventDictionary
    def CreateScaleHighPtDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_highpt_DOWN
        return modifiedEventDictionary
