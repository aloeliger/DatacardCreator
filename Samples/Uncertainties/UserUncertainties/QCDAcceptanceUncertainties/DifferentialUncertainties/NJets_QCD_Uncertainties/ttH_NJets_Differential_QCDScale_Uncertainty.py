from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ttH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ttH_NJets_Differential_QCDScale'
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
        if theTree.Rivet_nJets30 == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets4UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

    def CreateQCDScalettHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if theTree.Rivet_nJets30 == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_njets4DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

