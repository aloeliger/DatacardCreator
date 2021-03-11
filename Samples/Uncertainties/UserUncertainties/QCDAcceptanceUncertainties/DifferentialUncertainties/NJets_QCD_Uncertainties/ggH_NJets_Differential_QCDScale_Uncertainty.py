from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_NJets_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggHUp',
            'QCDscale_ggHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggHUp':self.CreateQCDScaleggHDictionaryUp,
            'QCDscale_ggHDown':self.CreateQCDScaleggHDictionaryDown,
        }
    def CreateQCDScaleggHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if theTree.Rivet_nJets30 == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets4UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

    def CreateQCDScaleggHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if theTree.Rivet_nJets30 == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_njets4DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

