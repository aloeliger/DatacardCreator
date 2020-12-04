from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ttH_PTH_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ttH_PTH_Differential_QCDScale'
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
        try:
            if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_0_45UP
            elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_45_80UP
            elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_80_120UP
            elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_120_200UP
            elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_200_350UP
            elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_350_450UP
            elif theTree.Rivet_higgsPt > 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_0_45UP
        except:
            pass
        return modifiedEventDictionary
    def CreateQCDScalettHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_0_45DOWN
            elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_45_80DOWN
            elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_80_120DOWN
            elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_120_200DOWN
            elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_200_350DOWN
            elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_350_450DOWN
            elif theTree.Rivet_higgsPt > 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ttH_pth_0_45DOWN
        except:
            pass
        return modifiedEventDictionary
