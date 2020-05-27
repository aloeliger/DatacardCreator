from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class WH_scale_wh_lowpt_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'WH_scale_lowpt'
        self.uncertaintyNames = [
            'WH_scale_lowptUp',
            'WH_scale_lowptDown',
        ]
        self.eventDictionaryModifications = {
            'WH_scale_lowptUp':self.CreateScaleLowPtDictionaryUP,
            'WH_scale_lowptDown':self.CreateScaleLowPtDictionaryUP,
            }
    def CreateScaleLowPtDictionaryUP(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_lowpt_UP
        return modifiedEventDictionary

    def CreateScaleLowPtDictionaryDOWN(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_VH_scale_lowpt_DOWN
        return modifiedEventDictionary
