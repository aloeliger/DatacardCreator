from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ZH_scale_zh_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ZH_scale_lowpt'
        self.uncertaintyNames = [
            'ZH_scale_lowptUp',
            'ZH_scale_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'ZH_scale_lowptUp':self.CreateScaleLowPtDictionaryUP,
            'ZH_scale_lowptDown':self.CreateScaleLowPtDictionaryUP,
            }
    def CreateScaleLowPtDictionaryUP(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_lowpt_UP
        return modifiedEventDictionary

    def CreateScaleLowPtDictionaryDOWN(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_lowpt_DOWN
        return modifiedEventDictionary
