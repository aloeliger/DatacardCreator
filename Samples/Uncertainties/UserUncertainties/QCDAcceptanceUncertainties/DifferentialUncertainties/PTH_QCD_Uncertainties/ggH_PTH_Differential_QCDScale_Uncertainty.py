from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggH_PTH_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggH_PTH_Differential_QCDScale'
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
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_gt450UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

    def CreateQCDScaleggHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ggH_pth_gt450DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary
        return modifiedEventDictionary

