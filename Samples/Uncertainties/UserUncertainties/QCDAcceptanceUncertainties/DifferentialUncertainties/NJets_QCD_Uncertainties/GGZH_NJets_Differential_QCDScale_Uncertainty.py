from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class GGZH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'GGZH_NJets_Differential_QCDScale'
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
            if theTree.Rivet_nJets30 == 0:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets0UP
            elif theTree.Rivet_nJets30 == 1:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets1UP
            elif theTree.Rivet_nJets30 == 2:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets2UP
            elif theTree.Rivet_nJets30 == 3:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets3UP
            elif theTree.Rivet_nJets30 >= 4:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets4UP
        except:
            try:
                if theTree.Rivet_nJets30 == 0:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets0UP
                elif theTree.Rivet_nJets30 == 1:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets1UP
                elif theTree.Rivet_nJets30 == 2:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets2UP
                elif theTree.Rivet_nJets30 == 3:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets3UP
                elif theTree.Rivet_nJets30 >= 4:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets4UP
            except:
                try:
                    if theTree.Rivet_nJets30 == 0:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets0UP
                    elif theTree.Rivet_nJets30 == 1:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets1UP
                    elif theTree.Rivet_nJets30 == 2:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets2UP
                    elif theTree.Rivet_nJets30 == 3:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets3UP
                    elif theTree.Rivet_nJets30 >= 4:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets4UP
                except:
                    pass
        return modifiedEventDictionary
    def CreateQCDScaleGGZHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_nJets30 == 0:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets0DOWN
            elif theTree.Rivet_nJets30 == 1:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets1DOWN
            elif theTree.Rivet_nJets30 == 2:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets2DOWN
            elif theTree.Rivet_nJets30 == 3:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets3DOWN
            elif theTree.Rivet_nJets30 >= 4:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHLLTT_njets4DOWN
        except:
            try:
                if theTree.Rivet_nJets30 == 0:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets0DOWN
                elif theTree.Rivet_nJets30 == 1:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets1DOWN
                elif theTree.Rivet_nJets30 == 2:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets2DOWN
                elif theTree.Rivet_nJets30 == 3:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets3DOWN
                elif theTree.Rivet_nJets30 >= 4:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHNNTT_njets4DOWN
            except:
                try:
                    if theTree.Rivet_nJets30 == 0:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets0DOWN
                    elif theTree.Rivet_nJets30 == 1:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets1DOWN
                    elif theTree.Rivet_nJets30 == 2:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets2DOWN
                    elif theTree.Rivet_nJets30 == 3:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets3DOWN
                    elif theTree.Rivet_nJets30 >= 4:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_GGZHQQTT_njets4DOWN
                except:
                    pass
        return modifiedEventDictionary
