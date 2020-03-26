from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class eTauFakeRateUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'eTauFakeRate'
        self.uncertaintyNames= [
            "CMS_etauFR_vloose_barrelUp",
            "CMS_etauFR_vloose_barrelDown",
            "CMS_etauFR_vloose_endcapUp",
            "CMS_etauFR_vloose_endcapDown",            
            ]
        self.eventDictionaryModifications = {
            "CMS_etauFR_vloose_barrelUp":self.CreateETauFRBarrelUpDictionary,
            "CMS_etauFR_vloose_barrelDown":self.CreateETauFRBarrelDownDictionary,
            "CMS_etauFR_vloose_endcapUp":self.CreateETauFREndcapUpDictionary,
            "CMS_etauFR_vloose_endcapDown":self.CreateETauFREndcapDownDictionary, 
            }
    def CreateETauFRBarrelUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_eTauFakeRateWeight_Barrel_UP
        return modifiedEventDictionary
    def CreateETauFRBarrelDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_eTauFakeRateWeight_Barrel_DOWN
        return modifiedEventDictionary
    def CreateETauFREndcapUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_eTauFakeRateWeight_Endcap_UP
        return modifiedEventDictionary
    def CreateETauFREndcapDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_eTauFakeRateWeight_Endcap_DOWN
        return modifiedEventDictionary
        
