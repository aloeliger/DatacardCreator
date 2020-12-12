from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ttH_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ttH_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ttHUp',
            'QCDscale_ttHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ttHUp':self.CreateQCDScalettHDictionaryUp,
            'QCDscale_ttHDown':self.CreateQCDScalettHDictionaryDown,
        }
    def CreateQCDScalettHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_ttHUP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary


    def CreateQCDScalettHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_RawQCDScaleAcceptance_ttHDOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

