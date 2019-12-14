from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class EmbeddedTrigger16Uncertainty(Uncertainty):
    def __init__(self):
        self.name = '2016Trigger'
        self.uncertaintyNames = [
            "CMS_singlemutrg_embUp",
            "CMS_mutautrg_embUp",
            "CMS_singlemutrg_embDown",
            "CMS_mutautrg_embDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_singlemutrg_embUp":self.CreateSingleMuTrgUpDictionary,
            "CMS_mutautrg_embUp":self.CreateMuTauTrgUpDictionary,
            "CMS_singlemutrg_embDown":self.CreateSingleMuTrgDownDictionary,
            "CMS_mutautrg_embDown":self.CreateMuTauTrgDownDictionary,
            }
    def CreateSingleMuTrgUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger22_UP
        return modifiedEventDictionary
    def CreateSingleMuTrgDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger22_DOWN
        return modifiedEventDictionary
    def CreateMuTauTrgUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger1920_UP
        return modifiedEventDictionary
    def CreateMuTauTrgDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_Trigger1920_DOWN
        return modifiedEventDictionary
