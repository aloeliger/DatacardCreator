from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class FakeFactorUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'FF_Uncertainty'
        self.uncertaintyNames = [
            "CMS_rawFF_mt_qcd_0jet_barrel_unc1Up",
            "CMS_rawFF_mt_qcd_0jet_barrel_unc2Up",
            "CMS_rawFF_mt_qcd_1jet_barrel_unc1Up",
            "CMS_rawFF_mt_qcd_1jet_barrel_unc2Up",
            "CMS_rawFF_mt_qcd_2jet_barrel_unc1Up",
            "CMS_rawFF_mt_qcd_2jet_barrel_unc2Up",
            "CMS_rawFF_mt_qcd_0jet_endcap_unc1Up",
            "CMS_rawFF_mt_qcd_0jet_endcap_unc2Up",
            "CMS_rawFF_mt_qcd_1jet_endcap_unc1Up",
            "CMS_rawFF_mt_qcd_1jet_endcap_unc2Up",
            "CMS_rawFF_mt_qcd_2jet_endcap_unc1Up",
            "CMS_rawFF_mt_qcd_2jet_endcap_unc2Up",
            "CMS_rawFF_mt_w_0jet_barrel_unc1Up",
            "CMS_rawFF_mt_w_0jet_barrel_unc2Up",
            "CMS_rawFF_mt_w_1jet_barrel_unc1Up",
            "CMS_rawFF_mt_w_1jet_barrel_unc2Up",
            "CMS_rawFF_mt_w_2jet_barrel_unc1Up",
            "CMS_rawFF_mt_w_2jet_barrel_unc2Up",
            "CMS_rawFF_mt_w_0jet_endcap_unc1Up",
            "CMS_rawFF_mt_w_0jet_endcap_unc2Up",
            "CMS_rawFF_mt_w_1jet_endcap_unc1Up",
            "CMS_rawFF_mt_w_1jet_endcap_unc2Up",
            "CMS_rawFF_mt_w_2jet_endcap_unc1Up",
            "CMS_rawFF_mt_w_2jet_endcap_unc2Up",
            "CMS_rawFF_mt_tt_unc1Up",
            "CMS_rawFF_mt_tt_unc2Up",      
            "CMS_FF_closure_lpt_xtrg_mt_qcdUp",
	    "CMS_FF_closure_lpt_xtrg_mt_wUp",
	    "CMS_FF_closure_lpt_xtrg_mt_ttUp",
	    "CMS_FF_closure_lpt_mt_qcdUp",
	    "CMS_FF_closure_lpt_mt_wUp",
	    "CMS_FF_closure_lpt_mt_ttUp",
            "CMS_FF_closure_OSSS_mvis_mt_qcdUp",            
            #"CMS_FF_closure_pth_mt_wUp",
            "CMS_FF_closure_pth_mt_0jet_wUp",
            "CMS_FF_closure_ljpt_pth0to45_mt_wUp",
            "CMS_FF_closure_ljpt_pth45to80_mt_wUp",
            "CMS_FF_closure_ljpt_pth80to120_mt_wUp",
            "CMS_FF_closure_ljpt_pth120to200_mt_wUp",
            "CMS_FF_closure_ljpt_pthgt200_mt_wUp",
            "CMS_FF_norm_mt_0jetUp",
            "CMS_FF_norm_mt_1jetUp",
            "CMS_FF_norm_mt_2jetUp",
            "CMS_FF_norm_mt_3jetUp",
            "CMS_FF_norm_mt_4jetUp",

            "CMS_rawFF_mt_qcd_0jet_barrel_unc1Down",
            "CMS_rawFF_mt_qcd_0jet_barrel_unc2Down",
            "CMS_rawFF_mt_qcd_1jet_barrel_unc1Down",
            "CMS_rawFF_mt_qcd_1jet_barrel_unc2Down",
            "CMS_rawFF_mt_qcd_2jet_barrel_unc1Down",
            "CMS_rawFF_mt_qcd_2jet_barrel_unc2Down",
            "CMS_rawFF_mt_w_0jet_barrel_unc1Down",
            "CMS_rawFF_mt_w_0jet_barrel_unc2Down",
            "CMS_rawFF_mt_w_1jet_barrel_unc1Down",
            "CMS_rawFF_mt_w_1jet_barrel_unc2Down",
            "CMS_rawFF_mt_w_2jet_barrel_unc1Down",
            "CMS_rawFF_mt_w_2jet_barrel_unc2Down",
            "CMS_rawFF_mt_qcd_0jet_endcap_unc1Down",
            "CMS_rawFF_mt_qcd_0jet_endcap_unc2Down",
            "CMS_rawFF_mt_qcd_1jet_endcap_unc1Down",
            "CMS_rawFF_mt_qcd_1jet_endcap_unc2Down",
            "CMS_rawFF_mt_qcd_2jet_endcap_unc1Down",
            "CMS_rawFF_mt_qcd_2jet_endcap_unc2Down",
            "CMS_rawFF_mt_w_0jet_endcap_unc1Down",
            "CMS_rawFF_mt_w_0jet_endcap_unc2Down",
            "CMS_rawFF_mt_w_1jet_endcap_unc1Down",
            "CMS_rawFF_mt_w_1jet_endcap_unc2Down",
            "CMS_rawFF_mt_w_2jet_endcap_unc1Down",
            "CMS_rawFF_mt_w_2jet_endcap_unc2Down",
            "CMS_rawFF_mt_tt_unc1Down",
            "CMS_rawFF_mt_tt_unc2Down",      
            "CMS_FF_closure_lpt_xtrg_mt_qcdDown",
	    "CMS_FF_closure_lpt_xtrg_mt_wDown",
	    "CMS_FF_closure_lpt_xtrg_mt_ttDown",
	    "CMS_FF_closure_lpt_mt_qcdDown",
	    "CMS_FF_closure_lpt_mt_wDown",
	    "CMS_FF_closure_lpt_mt_ttDown",
            "CMS_FF_closure_OSSS_mvis_mt_qcdDown",            
            #"CMS_FF_closure_mt_mt_w_unc1Down",
            #"CMS_FF_closure_mt_mt_w_unc2Down",
            #"CMS_FF_closure_pth_mt_wDown",
            "CMS_FF_closure_pth_mt_0jet_wDown",
            "CMS_FF_closure_ljpt_pth0to45_mt_wDown",
            "CMS_FF_closure_ljpt_pth45to80_mt_wDown",
            "CMS_FF_closure_ljpt_pth80to120_mt_wDown",
            "CMS_FF_closure_ljpt_pth120to200_mt_wDown",
            "CMS_FF_closure_ljpt_pthgt200_mt_wDown",
            "CMS_FF_norm_mt_0jetDown",
            "CMS_FF_norm_mt_1jetDown",
            "CMS_FF_norm_mt_2jetDown",
            "CMS_FF_norm_mt_3jetDown",
            "CMS_FF_norm_mt_4jetDown",
            ]
        self.eventDictionaryModifications = {
            "CMS_rawFF_mt_qcd_0jet_barrel_unc1Up":self.CreateRawQCD0JetBarrelUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_barrel_unc2Up":self.CreateRawQCD0JetBarrelUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_barrel_unc1Up":self.CreateRawQCD1JetBarrelUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_barrel_unc2Up":self.CreateRawQCD1JetBarrelUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_2jet_barrel_unc1Up":self.CreateRawQCD2JetBarrelUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_2jet_barrel_unc2Up":self.CreateRawQCD2JetBarrelUnc2UpDictionary,
            "CMS_rawFF_mt_w_0jet_barrel_unc1Up":self.CreateRawW0JetBarrelUnc1UpDictionary,
            "CMS_rawFF_mt_w_0jet_barrel_unc2Up":self.CreateRawW0JetBarrelUnc2UpDictionary,
            "CMS_rawFF_mt_w_1jet_barrel_unc1Up":self.CreateRawW1JetBarrelUnc1UpDictionary,
            "CMS_rawFF_mt_w_1jet_barrel_unc2Up":self.CreateRawW1JetBarrelUnc2UpDictionary,
            "CMS_rawFF_mt_w_2jet_barrel_unc1Up":self.CreateRawW2JetBarrelUnc1UpDictionary,
            "CMS_rawFF_mt_w_2jet_barrel_unc2Up":self.CreateRawW2JetBarrelUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_endcap_unc1Up":self.CreateRawQCD0JetEndcapUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_endcap_unc2Up":self.CreateRawQCD0JetEndcapUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_endcap_unc1Up":self.CreateRawQCD1JetEndcapUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_endcap_unc2Up":self.CreateRawQCD1JetEndcapUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_2jet_endcap_unc1Up":self.CreateRawQCD2JetEndcapUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_2jet_endcap_unc2Up":self.CreateRawQCD2JetEndcapUnc2UpDictionary,
            "CMS_rawFF_mt_w_0jet_endcap_unc1Up":self.CreateRawW0JetEndcapUnc1UpDictionary,
            "CMS_rawFF_mt_w_0jet_endcap_unc2Up":self.CreateRawW0JetEndcapUnc2UpDictionary,
            "CMS_rawFF_mt_w_1jet_endcap_unc1Up":self.CreateRawW1JetEndcapUnc1UpDictionary,
            "CMS_rawFF_mt_w_1jet_endcap_unc2Up":self.CreateRawW1JetEndcapUnc2UpDictionary,
            "CMS_rawFF_mt_w_2jet_endcap_unc1Up":self.CreateRawW2JetEndcapUnc1UpDictionary,
            "CMS_rawFF_mt_w_2jet_endcap_unc2Up":self.CreateRawW2JetEndcapUnc2UpDictionary,
            "CMS_rawFF_mt_tt_unc1Up":self.CreateRawTT0JetUnc1UpDictionary,
            "CMS_rawFF_mt_tt_unc2Up":self.CreateRawTT0JetUnc2UpDictionary,
            "CMS_FF_closure_lpt_xtrg_mt_qcdUp":self.CreateLPTClosureXTrgQCDUpDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_wUp":self.CreateLPTClosureXTrgWUpDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_ttUp":self.CreateLPTClosureXTrgTTUpDictionary,
	    "CMS_FF_closure_lpt_mt_qcdUp":self.CreateLPTClosureQCDUpDictionary,
	    "CMS_FF_closure_lpt_mt_wUp":self.CreateLPTClosureWUpDictionary,
	    "CMS_FF_closure_lpt_mt_ttUp":self.CreateLPTClosureTTUpDictionary,
            "CMS_FF_closure_OSSS_mvis_mt_qcdUp":self.CreateOSSSClosureQCDUnc1UpDictionary,
            #"CMS_FF_closure_mt_mt_w_unc1Up":self.CreateMTClosureWUnc1UpDictionary,
            #"CMS_FF_closure_mt_mt_w_unc2Up":self.CreateMTClosureWUnc2UpDictionary,
            #"CMS_FF_closure_pth_mt_wUp":self.CreatePTHClosureUncUpDictionary,
            "CMS_FF_closure_pth_mt_0jet_wUp":self.CreatePTHClosure0JetUncUpDictionary,
            "CMS_FF_closure_ljpt_pth0to45_mt_wUp":self.CreatePTH0to45ClosureUncUpDictionary,
            "CMS_FF_closure_ljpt_pth45to80_mt_wUp":self.CreatePTH45to80ClosureUncUpDictionary,
            "CMS_FF_closure_ljpt_pth80to120_mt_wUp":self.CreatePTH80to120ClosureUncUpDictionary,
            "CMS_FF_closure_ljpt_pth120to200_mt_wUp":self.CreatePTH120to200ClosureUncUpDictionary,
            "CMS_FF_closure_ljpt_pthgt200_mt_wUp":self.CreatePTHGT200ClosureUncUpDictionary,
            "CMS_FF_norm_mt_0jetUp":self.CreateNJet0NormUpDictionary,
            "CMS_FF_norm_mt_1jetUp":self.CreateNJet1NormUpDictionary,
            "CMS_FF_norm_mt_2jetUp":self.CreateNJet2NormUpDictionary,
            "CMS_FF_norm_mt_3jetUp":self.CreateNJet3NormUpDictionary,
            "CMS_FF_norm_mt_4jetUp":self.CreateNJet4NormUpDictionary,

            "CMS_rawFF_mt_qcd_0jet_barrel_unc1Down":self.CreateRawQCD0JetBarrelUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_0jet_barrel_unc2Down":self.CreateRawQCD0JetBarrelUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_barrel_unc1Down":self.CreateRawQCD1JetBarrelUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_barrel_unc2Down":self.CreateRawQCD1JetBarrelUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_2jet_barrel_unc1Down":self.CreateRawQCD2JetBarrelUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_2jet_barrel_unc2Down":self.CreateRawQCD2JetBarrelUnc2DownDictionary,
            "CMS_rawFF_mt_w_0jet_barrel_unc1Down":self.CreateRawW0JetBarrelUnc1DownDictionary,
            "CMS_rawFF_mt_w_0jet_barrel_unc2Down":self.CreateRawW0JetBarrelUnc2DownDictionary,
            "CMS_rawFF_mt_w_1jet_barrel_unc1Down":self.CreateRawW1JetBarrelUnc1DownDictionary,
            "CMS_rawFF_mt_w_1jet_barrel_unc2Down":self.CreateRawW1JetBarrelUnc2DownDictionary,
            "CMS_rawFF_mt_w_2jet_barrel_unc1Down":self.CreateRawW2JetBarrelUnc1DownDictionary,
            "CMS_rawFF_mt_w_2jet_barrel_unc2Down":self.CreateRawW2JetBarrelUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_0jet_endcap_unc1Down":self.CreateRawQCD0JetEndcapUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_0jet_endcap_unc2Down":self.CreateRawQCD0JetEndcapUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_endcap_unc1Down":self.CreateRawQCD1JetEndcapUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_endcap_unc2Down":self.CreateRawQCD1JetEndcapUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_2jet_endcap_unc1Down":self.CreateRawQCD2JetEndcapUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_2jet_endcap_unc2Down":self.CreateRawQCD2JetEndcapUnc2DownDictionary,
            "CMS_rawFF_mt_w_0jet_endcap_unc1Down":self.CreateRawW0JetEndcapUnc1DownDictionary,
            "CMS_rawFF_mt_w_0jet_endcap_unc2Down":self.CreateRawW0JetEndcapUnc2DownDictionary,
            "CMS_rawFF_mt_w_1jet_endcap_unc1Down":self.CreateRawW1JetEndcapUnc1DownDictionary,
            "CMS_rawFF_mt_w_1jet_endcap_unc2Down":self.CreateRawW1JetEndcapUnc2DownDictionary,
            "CMS_rawFF_mt_w_2jet_endcap_unc1Down":self.CreateRawW2JetEndcapUnc1DownDictionary,
            "CMS_rawFF_mt_w_2jet_endcap_unc2Down":self.CreateRawW2JetEndcapUnc2DownDictionary,
            "CMS_rawFF_mt_tt_unc1Down":self.CreateRawTT0JetUnc1DownDictionary,
            "CMS_rawFF_mt_tt_unc2Down":self.CreateRawTT0JetUnc2DownDictionary,
            "CMS_FF_closure_lpt_xtrg_mt_qcdDown":self.CreateLPTClosureXTrgQCDDownDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_wDown":self.CreateLPTClosureXTrgWDownDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_ttDown":self.CreateLPTClosureXTrgTTDownDictionary,
	    "CMS_FF_closure_lpt_mt_qcdDown":self.CreateLPTClosureQCDDownDictionary,
	    "CMS_FF_closure_lpt_mt_wDown":self.CreateLPTClosureWDownDictionary,
	    "CMS_FF_closure_lpt_mt_ttDown":self.CreateLPTClosureTTDownDictionary,
            "CMS_FF_closure_OSSS_mvis_mt_qcdDown":self.CreateOSSSClosureQCDUnc1DownDictionary,  
            #"CMS_FF_closure_mt_mt_w_unc1Down":self.CreateMTClosureWUnc1DownDictionary,
            #"CMS_FF_closure_mt_mt_w_unc2Down":self.CreateMTClosureWUnc2DownDictionary,
            #"CMS_FF_closure_pth_mt_wDown":self.CreatePTHClosureUncDownDictionary,
            "CMS_FF_closure_pth_mt_0jet_wDown":self.CreatePTHClosure0JetUncDownDictionary,
            "CMS_FF_closure_ljpt_pth0to45_mt_wDown":self.CreatePTH0to45ClosureUncDownDictionary,
            "CMS_FF_closure_ljpt_pth45to80_mt_wDown":self.CreatePTH45to80ClosureUncDownDictionary,
            "CMS_FF_closure_ljpt_pth80to120_mt_wDown":self.CreatePTH80to120ClosureUncDownDictionary,
            "CMS_FF_closure_ljpt_pth120to200_mt_wDown":self.CreatePTH120to200ClosureUncDownDictionary,
            "CMS_FF_closure_ljpt_pthgt200_mt_wDown":self.CreatePTHGT200ClosureUncDownDictionary,
            "CMS_FF_norm_mt_0jetDown":self.CreateNJet0NormDownDictionary,
            "CMS_FF_norm_mt_1jetDown":self.CreateNJet1NormDownDictionary,
            "CMS_FF_norm_mt_2jetDown":self.CreateNJet2NormDownDictionary,
            "CMS_FF_norm_mt_3jetDown":self.CreateNJet3NormDownDictionary,
            "CMS_FF_norm_mt_4jetDown":self.CreateNJet4NormDownDictionary,
            }

    #QCD raw uncerts
    def CreateRawQCD0JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD0JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD1JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD2JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_barrel_unc2_down
        return modifiedEventDictionary

    def CreateRawQCD0JetEndcapUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_endcaps_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD0JetEndcapUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_endcaps_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD0JetEndcapUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_endcaps_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD0JetEndcapUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_endcaps_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD1JetEndcapUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_endcaps_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD1JetEndcapUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_endcaps_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD1JetEndcapUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_endcaps_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD1JetEndcapUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_endcaps_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD2JetEndcapUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_endcaps_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD2JetEndcapUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_endcaps_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD2JetEndcapUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_endcaps_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD2JetEndcapUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_endcaps_unc2_down
        return modifiedEventDictionary

    #W raw uncerts
    def CreateRawW0JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawW0JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawW0JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawW0JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawW1JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawW1JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawW1JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawW1JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_barrel_unc2_down
        return modifiedEventDictionary
    def CreateRawW2JetBarrelUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_barrel_unc1_up
        return modifiedEventDictionary
    def CreateRawW2JetBarrelUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_barrel_unc1_down
        return modifiedEventDictionary
    def CreateRawW2JetBarrelUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_barrel_unc2_up
        return modifiedEventDictionary
    def CreateRawW2JetBarrelUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_barrel_unc2_down
        return modifiedEventDictionary

    def CreateRawW0JetEndcapUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_endcaps_unc1_up
        return modifiedEventDictionary
    def CreateRawW0JetEndcapUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_endcaps_unc1_down
        return modifiedEventDictionary
    def CreateRawW0JetEndcapUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_endcaps_unc2_up
        return modifiedEventDictionary
    def CreateRawW0JetEndcapUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_endcaps_unc2_down
        return modifiedEventDictionary
    def CreateRawW1JetEndcapUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_endcaps_unc1_up
        return modifiedEventDictionary
    def CreateRawW1JetEndcapUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_endcaps_unc1_down
        return modifiedEventDictionary
    def CreateRawW1JetEndcapUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_endcaps_unc2_up
        return modifiedEventDictionary
    def CreateRawW1JetEndcapUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_endcaps_unc2_down
        return modifiedEventDictionary
    def CreateRawW2JetEndcapUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_endcaps_unc1_up
        return modifiedEventDictionary
    def CreateRawW2JetEndcapUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_endcaps_unc1_down
        return modifiedEventDictionary
    def CreateRawW2JetEndcapUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_endcaps_unc2_up
        return modifiedEventDictionary
    def CreateRawW2JetEndcapUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_endcaps_unc2_down
        return modifiedEventDictionary

    #TTbar raw uncerts
    def CreateRawTT0JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc1_up        
        return modifiedEventDictionary
    def CreateRawTT0JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc1_down
        return modifiedEventDictionary
    def CreateRawTT0JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc2_up
        return modifiedEventDictionary
    def CreateRawTT0JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_tt_0jet_unc2_down
        return modifiedEventDictionary

    #cross trigger lpt
    def CreateLPTClosureXTrgQCDUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_xtrg_qcd_0jet_up
        return modifiedEventDictionary
    def CreateLPTClosureXTrgQCDDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_xtrg_qcd_0jet_down
        return modifiedEventDictionary
    def CreateLPTClosureXTrgWUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_xtrg_w_0jet_up
        return modifiedEventDictionary
    def CreateLPTClosureXTrgWDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_xtrg_w_0jet_down
        return modifiedEventDictionary
    def CreateLPTClosureXTrgTTUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_xtrg_tt_up
        return modifiedEventDictionary
    def CreateLPTClosureXTrgTTDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_xtrg_tt_down
        return modifiedEventDictionary

    #iso trigger lpt
    def CreateLPTClosureQCDUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_qcd_0jet_up
        return modifiedEventDictionary
    def CreateLPTClosureQCDDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_qcd_0jet_down
        return modifiedEventDictionary
    def CreateLPTClosureWUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_w_0jet_up
        return modifiedEventDictionary
    def CreateLPTClosureWDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_w_0jet_down
        return modifiedEventDictionary
    def CreateLPTClosureTTUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_tt_up
        return modifiedEventDictionary
    def CreateLPTClosureTTDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.lptclosure_tt_down
        return modifiedEventDictionary
        
    #W mt closure
    def CreateMTClosureWUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc1_up
        return modifiedEventDictionary
    def CreateMTClosureWUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc1_down
        return modifiedEventDictionary
    def CreateMTClosureWUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc2_up
        return modifiedEventDictionary
    def CreateMTClosureWUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_unc2_down
        return modifiedEventDictionary
        #qcd osss closure
    def CreateOSSSClosureQCDUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.osssclosure_qcd_unc1_up
        return modifiedEventDictionary
    def CreateOSSSClosureQCDUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.osssclosure_qcd_unc1_down
        return modifiedEventDictionary
    def CreatePTHClosureUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.pthclosure_w_up
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_njets_pth_ljpt_up
        return modifiedEventDictionary
    def CreatePTHClosureUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.pthclosure_w_down
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mtclosure_w_njets_pth_ljpt_dow
        return modifiedEventDictionary

    def CreatePTHClosure0JetUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets0_pth_up
        return modifiedEventDictionary
    def CreatePTHClosure0JetUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets0_pth_down
        return modifiedEventDictionary
    def CreatePTH0to45ClosureUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth0to45_ljpt_up
        return modifiedEventDictionary
    def CreatePTH0to45ClosureUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth0to45_ljpt_down
        return modifiedEventDictionary
    def CreatePTH45to80ClosureUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth45to80_ljpt_up
        return modifiedEventDictionary
    def CreatePTH45to80ClosureUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth45to80_ljpt_down
        return modifiedEventDictionary
    def CreatePTH80to120ClosureUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth80to120_ljpt_up
        return modifiedEventDictionary
    def CreatePTH80to120ClosureUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth80to120_ljpt_down
        return modifiedEventDictionary
    def CreatePTH120to200ClosureUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth120to200_ljpt_up
        return modifiedEventDictionary
    def CreatePTH120to200ClosureUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pth120to200_ljpt_down
        return modifiedEventDictionary
    def CreatePTHGT200ClosureUncUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pthgt200_ljpt_up
        return modifiedEventDictionary
    def CreatePTHGT200ClosureUncDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting*theTree.mtclosure_w_njets_pthgt200_ljpt_down
        return modifiedEventDictionary

    def CreateNJet0NormUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 0:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 1.05
        return modifiedEventDictionary
    def CreateNJet1NormUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 1:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 1.05
        return modifiedEventDictionary
    def CreateNJet2NormUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 2:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 1.05
        return modifiedEventDictionary
    def CreateNJet3NormUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 3:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 1.05
        return modifiedEventDictionary
    def CreateNJet4NormUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] >= 4:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 1.05
        return modifiedEventDictionary

    def CreateNJet0NormDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 0:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 0.95
        return modifiedEventDictionary
    def CreateNJet1NormDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 1:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 0.95
        return modifiedEventDictionary
    def CreateNJet2NormDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 2:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 0.95
        return modifiedEventDictionary
    def CreateNJet3NormDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 3:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 0.95
        return modifiedEventDictionary
    def CreateNJet4NormDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] >= 4:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight * 0.95
        return modifiedEventDictionary

