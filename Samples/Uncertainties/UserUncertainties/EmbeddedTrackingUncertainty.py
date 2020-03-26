from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class EmbeddedTrackingUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'EmbeddedTrackingUncertainty'
        self.uncertaintyNames = [
            "CMS_eff_prong_embUp",
            "CMS_eff_1prong1pizero_embUp",
            "CMS_eff_3prong1pizero_embUp",
            "CMS_eff_prong_embDown",
            "CMS_eff_1prong1pizero_embDown",
            "CMS_eff_3prong1pizero_embDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_eff_prong_embUp":self.CreateTrackProngUpDictionary,
            "CMS_eff_1prong1pizero_embUp":self.CreateTrack1Prong1PizeroUpDictionary,
            "CMS_eff_3prong1pizero_embUp":self.CreateTrack3Prong1PizeroUpDictionary,
            "CMS_eff_prong_embDown":self.CreateTrackProngDownDictionary,
            "CMS_eff_1prong1pizero_embDown":self.CreateTrack1Prong1PizeroDownDictionary,
            "CMS_eff_3prong1pizero_embDown":self.CreateTrack3Prong1PizeroDownDictionary,
            }
    def CreateTrackProngUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        if theTree.l2_decayMode == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 1.01
        elif theTree.l2_decayMode == 10:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 1.03
        return modifiedEventDictionary
    def CreateTrackProngDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        if theTree.l2_decayMode == 0:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 0.99
        elif theTree.l2_decayMode == 10:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 0.97
        return modifiedEventDictionary
    def CreateTrack1Prong1PizeroUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        if theTree.l2_decayMode == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 1.025
        return modifiedEventDictionary
    def CreateTrack1Prong1PizeroDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        if theTree.l2_decayMode == 1:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 0.975
        return modifiedEventDictionary
    def CreateTrack3Prong1PizeroUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        if theTree.l2_decayMode == 11:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 1.06
        return modifiedEventDictionary
    def CreateTrack3Prong1PizeroDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary=nominalEventDictionary.Clone()
        if theTree.l2_decayMode == 11:
            modifiedEventDictionary.Weight = theTree.FinalWeighting * 0.94
        return modifiedEventDictionary
