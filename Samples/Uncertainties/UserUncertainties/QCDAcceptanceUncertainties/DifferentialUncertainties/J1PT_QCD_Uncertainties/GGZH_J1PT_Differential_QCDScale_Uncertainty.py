from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class GGZH_J1PT_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'GGZH_J1PT_Differential_QCDScale'
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
            if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60UP
            elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120UP
            elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200UP
            elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350UP
            elif theTree.Rivet_j1pt > 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350UP
        except:
            try:
                if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60UP
                elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120UP
                elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200UP
                elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350UP
                elif theTree.Rivet_j1pt > 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350UP
            except:
                try:
                    if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60UP
                    elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120UP
                    elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200UP
                    elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350UP
                    elif theTree.Rivet_j1pt > 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350UP
                except:
                    pass
        return modifiedEventDictionary
    def CreateQCDScaleGGZHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_30_60DOWN
            elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_60_120DOWN
            elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_120_200DOWN
            elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_200_350DOWN
            elif theTree.Rivet_j1pt > 350:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_j1pt_gt350DOWN
        except:
            try:
                if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_30_60DOWN
                elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_60_120DOWN
                elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_120_200DOWN
                elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_200_350DOWN
                elif theTree.Rivet_j1pt > 350:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_j1pt_gt350DOWN
            except:
                try:
                    if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_30_60DOWN
                    elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_60_120DOWN
                    elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_120_200DOWN
                    elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_200_350DOWN
                    elif theTree.Rivet_j1pt > 350:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_j1pt_gt350DOWN
                except:
                    pass
        return modifiedEventDictionary
