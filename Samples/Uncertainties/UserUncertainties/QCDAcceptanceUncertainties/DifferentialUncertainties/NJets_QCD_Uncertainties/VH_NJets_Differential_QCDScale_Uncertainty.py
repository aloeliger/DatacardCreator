from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class VH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_NJets_Differential_QCDScale'
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
            if theTree.Rivet_nJets30 == 0:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets0UP
            elif theTree.Rivet_nJets30 == 1:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets1UP
            elif theTree.Rivet_nJets30 == 2:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets2UP
            elif theTree.Rivet_nJets30 == 3:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets3UP
            elif theTree.Rivet_nJets30 >= 4:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets4UP
        except:
            try:
                if theTree.Rivet_nJets30 == 0:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets0UP
                elif theTree.Rivet_nJets30 == 1:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets1UP
                elif theTree.Rivet_nJets30 == 2:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets2UP
                elif theTree.Rivet_nJets30 == 3:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets3UP
                elif theTree.Rivet_nJets30 >= 4:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets4UP
            except:
                try:
                    if theTree.Rivet_nJets30 == 0:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets0UP
                    elif theTree.Rivet_nJets30 == 1:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets1UP
                    elif theTree.Rivet_nJets30 == 2:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets2UP
                    elif theTree.Rivet_nJets30 == 3:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets3UP
                    elif theTree.Rivet_nJets30 >= 4:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets4UP
                except:
                    pass
        return modifiedEventDictionary
    def CreateQCDScaleVHDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        try:
            if theTree.Rivet_nJets30 == 0:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets0DOWN
            elif theTree.Rivet_nJets30 == 1:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets1DOWN
            elif theTree.Rivet_nJets30 == 2:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets2DOWN
            elif theTree.Rivet_nJets30 == 3:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets3DOWN
            elif theTree.Rivet_nJets30 >= 4:
                modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets4DOWN
        except:
            try:
                if theTree.Rivet_nJets30 == 0:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets0DOWN
                elif theTree.Rivet_nJets30 == 1:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets1DOWN
                elif theTree.Rivet_nJets30 == 2:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets2DOWN
                elif theTree.Rivet_nJets30 == 3:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets3DOWN
                elif theTree.Rivet_nJets30 >= 4:
                    modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets4DOWN
            except:
                try:
                    if theTree.Rivet_nJets30 == 0:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets0DOWN
                    elif theTree.Rivet_nJets30 == 1:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets1DOWN
                    elif theTree.Rivet_nJets30 == 2:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets2DOWN
                    elif theTree.Rivet_nJets30 == 3:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets3DOWN
                    elif theTree.Rivet_nJets30 >= 4:
                        modifiedEventDictionary.Weight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets4DOWN
                except:
                    pass
        return modifiedEventDictionary
