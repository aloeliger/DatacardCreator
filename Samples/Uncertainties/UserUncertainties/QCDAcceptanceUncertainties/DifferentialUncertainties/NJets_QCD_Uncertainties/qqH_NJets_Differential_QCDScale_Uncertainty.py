from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'qqH_NJets_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_qqHUp',
            'QCDscale_qqHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_qqHUp':self.CreateQCDScaleqqHDictionaryUp,
            'QCDscale_qqHDown':self.CreateQCDScaleqqHDictionaryDown,
        }
    def CreateQCDScaleqqHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if theTree.Rivet_nJets30 == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets4UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

    def CreateQCDScaleqqHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if theTree.Rivet_nJets30 == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_qqH_njets4DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

