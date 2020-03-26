from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class TauFakeRateUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'TauFakeRate'
        self.uncertaintyNames= [
            "CMS_m_FakeTau_etalt0p4Up",
            "CMS_m_FakeTau_etalt0p4Down",
            "CMS_m_FakeTau_eta0p4to0p8Up",
            "CMS_m_FakeTau_eta0p4to0p8Down",
            "CMS_m_FakeTau_eta0p8to1p2Up",
            "CMS_m_FakeTau_eta0p8to1p2Down",
            "CMS_m_FakeTau_eta1p2to1p7Up",
            "CMS_m_FakeTau_eta1p2to1p7Down",
            "CMS_m_FakeTau_etagt1p7Up",
            "CMS_m_FakeTau_etagt1p7Down",
            "CMS_m_FakeTau_taupt30to40Up",
            "CMS_m_FakeTau_taupt30to40Down",
            "CMS_m_FakeTau_taupt40to50Up",
            "CMS_m_FakeTau_taupt40to50Down",
            "CMS_m_FakeTau_tauptgt50Up",
            "CMS_m_FakeTau_tauptgt50Down",
            ]
        self.eventDictionaryModifications = {
            "CMS_m_FakeTau_etalt0p4Up":self.CreateTauFakeRateEtaLT0p4UpDictionary,
            "CMS_m_FakeTau_etalt0p4Down":self.CreateTauFakeRateEtaLT0p4DownDictionary,
            "CMS_m_FakeTau_eta0p4to0p8Up":self.CreateTauFakeRateEta0p4to0p8UpDictionary,
            "CMS_m_FakeTau_eta0p4to0p8Down":self.CreateTauFakeRateEta0p4to0p8DownDictionary,
            "CMS_m_FakeTau_eta0p8to1p2Up":self.CreateTauFakeRateEta0p8to1p2UpDictionary,
            "CMS_m_FakeTau_eta0p8to1p2Down":self.CreateTauFakeRateEta0p8to1p2DownDictionary,
            "CMS_m_FakeTau_eta1p2to1p7Up":self.CreateTauFakeRateEta1p2to1p7UpDictionary,
            "CMS_m_FakeTau_eta1p2to1p7Down":self.CreateTauFakeRateEta1p2to1p7DownDictionary,
            "CMS_m_FakeTau_etagt1p7Up":self.CreateTauFakeRateEtaGT1p7UpDictionary,
            "CMS_m_FakeTau_etagt1p7Down":self.CreateTauFakeRateEtaGT1p7DownDictionary,
            "CMS_m_FakeTau_taupt30to40Up":self.CreateTauFakeRatePt30to40UpDictionary,
            "CMS_m_FakeTau_taupt30to40Down":self.CreateTauFakeRatePt30to40DownDictionary,
            "CMS_m_FakeTau_taupt40to50Up":self.CreateTauFakeRatePt40to50UpDictionary,
            "CMS_m_FakeTau_taupt40to50Down":self.CreateTauFakeRatePt40to50DownDictionary,
            "CMS_m_FakeTau_tauptgt50Up":self.CreateTauFakeRatePtGT50UpDictionary,
            "CMS_m_FakeTau_tauptgt50Down":self.CreateTauFakeRatePtGT50DownDictionary,
            }
    def CreateTauFakeRateEtaLT0p4UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta0to0p4_UP
        return modifiedEventDictionary
    def CreateTauFakeRateEtaLT0p4DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta0to0p4_DOWN
        return modifiedEventDictionary
    def CreateTauFakeRateEta0p4to0p8UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta0p4to0p8_UP
        return modifiedEventDictionary
    def CreateTauFakeRateEta0p4to0p8DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta0p4to0p8_DOWN
        return modifiedEventDictionary
    def CreateTauFakeRateEta0p8to1p2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta0p8to1p2_UP
        return modifiedEventDictionary
    def CreateTauFakeRateEta0p8to1p2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta0p8to1p2_DOWN
        return modifiedEventDictionary
    def CreateTauFakeRateEta1p2to1p7UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta1p2to1p7_UP
        return modifiedEventDictionary
    def CreateTauFakeRateEta1p2to1p7DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_eta1p2to1p7_DOWN
        return modifiedEventDictionary
    def CreateTauFakeRateEtaGT1p7UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_etagt1p7_UP
        return modifiedEventDictionary
    def CreateTauFakeRateEtaGT1p7DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_etagt1p7_DOWN
        return modifiedEventDictionary
        
    def CreateTauFakeRatePt30to40UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_taupt30to40_UP
        return modifiedEventDictionary
    def CreateTauFakeRatePt30to40DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_taupt30to40_DOWN
        return modifiedEventDictionary
    def CreateTauFakeRatePt40to50UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_taupt40to50_UP
        return modifiedEventDictionary
    def CreateTauFakeRatePt40to50DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_taupt40to50_DOWN
        return modifiedEventDictionary
    def CreateTauFakeRatePtGT50UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_tauptgt50_UP
        return modifiedEventDictionary
    def CreateTauFakeRatePtGT50DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_TauFakeRateWeight_tauptgt50_DOWN
        return modifiedEventDictionary
