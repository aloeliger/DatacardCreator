from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_PTH_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_PTH_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_VHUp',
            'QCDscale_VHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_VHUp':self.CreateQCDScaleVHDictionaryUp,
            'QCDscale_VHDown':self.CreateQCDScaleVHDictionaryDown,
        }
    def CreateQCDScaleVHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_0_45UP
            elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_45_80UP
            elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_80_120UP
            elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_120_200UP
            elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_200_350UP
            elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_350_450UP
            elif theTree.Rivet_higgsPt > 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_0_45UP
        except:
            try:
                if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_0_45UP
                elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_45_80UP
                elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_80_120UP
                elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_120_200UP
                elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_200_350UP
                elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_350_450UP
                elif theTree.Rivet_higgsPt > 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_0_45UP
            except:
                try:
                    if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_0_45UP
                    elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_45_80UP
                    elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_80_120UP
                    elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_120_200UP
                    elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_200_350UP
                    elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_350_450UP
                    elif theTree.Rivet_higgsPt > 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_0_45UP
                except:
                    pass
        return modifiedEventDictionary
    def CreateQCDScaleVHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_0_45DOWN
            elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_45_80DOWN
            elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_80_120DOWN
            elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_120_200DOWN
            elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_200_350DOWN
            elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_350_450DOWN
            elif theTree.Rivet_higgsPt > 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_0_45DOWN
        except:
            try:
                if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_0_45DOWN
                elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_45_80DOWN
                elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_80_120DOWN
                elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_120_200DOWN
                elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_200_350DOWN
                elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_350_450DOWN
                elif theTree.Rivet_higgsPt > 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_0_45DOWN
            except:
                try:
                    if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_0_45DOWN
                    elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_45_80DOWN
                    elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_80_120DOWN
                    elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_120_200DOWN
                    elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_200_350DOWN
                    elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_350_450DOWN
                    elif theTree.Rivet_higgsPt > 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_0_45DOWN
                except:
                    pass
        return modifiedEventDictionary
