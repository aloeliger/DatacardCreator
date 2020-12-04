from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class GGZH_PTH_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'GGZH_PTH_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_ggZHUp',
            'QCDscale_ggZHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_ggZHUp':self.CreateQCDScaleGGZHDictionaryUp,
            'QCDscale_ggZHDown':self.CreateQCDScaleGGZHDictionaryDown,
        }
    def CreateQCDScaleGGZHDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45UP
            elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80UP
            elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120UP
            elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200UP
            elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350UP
            elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450UP
            elif theTree.Rivet_higgsPt > 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45UP
        except:
            try:
                if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45UP
                elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80UP
                elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120UP
                elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200UP
                elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350UP
                elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450UP
                elif theTree.Rivet_higgsPt > 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45UP
            except:
                try:
                    if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45UP
                    elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80UP
                    elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120UP
                    elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200UP
                    elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350UP
                    elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450UP
                    elif theTree.Rivet_higgsPt > 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45UP
                except:
                    pass
        return modifiedEventDictionary
    def CreateQCDScaleGGZHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45DOWN
            elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_45_80DOWN
            elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_80_120DOWN
            elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_120_200DOWN
            elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_200_350DOWN
            elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_350_450DOWN
            elif theTree.Rivet_higgsPt > 450:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_pth_0_45DOWN
        except:
            try:
                if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45DOWN
                elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_45_80DOWN
                elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_80_120DOWN
                elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_120_200DOWN
                elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_200_350DOWN
                elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_350_450DOWN
                elif theTree.Rivet_higgsPt > 450:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_pth_0_45DOWN
            except:
                try:
                    if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45DOWN
                    elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_45_80DOWN
                    elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_80_120DOWN
                    elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_120_200DOWN
                    elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_200_350DOWN
                    elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_350_450DOWN
                    elif theTree.Rivet_higgsPt > 450:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_pth_0_45DOWN
                except:
                    pass
        return modifiedEventDictionary
