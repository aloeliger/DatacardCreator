from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class EmbeddedTauIDUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'EmbeddedTauID'
        self.uncertaintyNames = [
            "CMS_eff_t_embedded_pt30to35Up",
            "CMS_eff_t_embedded_pt35to40Up",
            "CMS_eff_t_embedded_ptgt40Up",
            "CMS_eff_t_embedded_pt30to35Down",
            "CMS_eff_t_embedded_pt35to40Down",
            "CMS_eff_t_embedded_ptgt40Down",
        ]
        self.eventDictionaryModifications = {
            "CMS_eff_t_embedded_pt30to35Up":self.CreateTauIDPT30to35UpDictionary,
            "CMS_eff_t_embedded_pt35to40Up":self.CreateTauIDPT35to40UpDictionary,
            "CMS_eff_t_embedded_ptgt40Up":self.CreateTauIDPTGT40UpDictionary,
            "CMS_eff_t_embedded_pt30to35Down":self.CreateTauIDPT30to35DownDictionary,
            "CMS_eff_t_embedded_pt35to40Down":self.CreateTauIDPT35to40DownDictionary,
            "CMS_eff_t_embedded_ptgt40Down":self.CreateTauIDPTGT40DownDictionary,
        }

    def CreateTauIDPT30to35UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauID_pT0to35_UP
        return modifiedEventDictionary
    def CreateTauIDPT30to35DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauID_pT0to35_DOWN
        return modifiedEventDictionary
    def CreateTauIDPT35to40UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauID_pT35to40_UP
        return modifiedEventDictionary
    def CreateTauIDPT35to40DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauID_pT35to40_DOWN
        return modifiedEventDictionary
    def CreateTauIDPTGT40UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauID_pTgt40_UP
        return modifiedEventDictionary
    def CreateTauIDPTGT40DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauID_pTgt40_DOWN
        return modifiedEventDictionary
