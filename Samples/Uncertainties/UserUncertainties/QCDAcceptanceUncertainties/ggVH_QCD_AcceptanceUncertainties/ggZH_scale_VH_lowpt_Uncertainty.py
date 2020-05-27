from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggZH_scale_VH_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ZH_scale_lowpt'
        self.uncertaintyNames = [
            'ZH_scale_lowptUp',
            'ZH_scale_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'ZH_scale_lowptUp':self.CreateScaleLowPtDictionaryUP,
            'ZH_scale_lowptDown':self.CreateScaleLowPtDictionaryDOWN,
        }
    def CreateScaleLowPtDictionaryUP(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleacceptance_ggVH_scale_VH_lowpt_UP
        return modifiedEventDictionary
    def CreateScaleLowPtDictionaryDOWN(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleacceptance_ggVH_scale_VH_lowpt_DOWN
        return modifiedEventDictionary
        
