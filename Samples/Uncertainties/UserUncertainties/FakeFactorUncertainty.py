from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class FakeFactorUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'FF_Uncertainty'
        self.uncertaintyNames = [
            "CMS_rawFF_mt_qcd_0jet_unc1Up",
            "CMS_rawFF_mt_qcd_0jet_unc2Up",
            "CMS_rawFF_mt_qcd_1jet_unc1Up",
            "CMS_rawFF_mt_qcd_1jet_unc2Up",
            "CMS_rawFF_mt_qcd_2jet_unc1Up",
            "CMS_rawFF_mt_qcd_2jet_unc2Up",
            "CMS_rawFF_mt_w_0jet_unc1Up",
            "CMS_rawFF_mt_w_0jet_unc2Up",
            "CMS_rawFF_mt_w_1jet_unc1Up",
            "CMS_rawFF_mt_w_1jet_unc2Up",
            "CMS_rawFF_mt_w_2jet_unc1Up",
            "CMS_rawFF_mt_w_2jet_unc2Up",
            "CMS_rawFF_mt_tt_unc1Up",
            "CMS_rawFF_mt_tt_unc2Up",      
            "CMS_FF_closure_lpt_xtrg_mt_qcdUp",
	    "CMS_FF_closure_lpt_xtrg_mt_wUp",
	    "CMS_FF_closure_lpt_xtrg_mt_ttUp",
	    "CMS_FF_closure_lpt_mt_qcdUp",
	    "CMS_FF_closure_lpt_mt_wUp",
	    "CMS_FF_closure_lpt_mt_ttUp",
            "CMS_FF_closure_OSSS_mvis_mt_qcdUp",            
            "CMS_FF_closure_mt_mt_w_unc1Up",
            "CMS_FF_closure_mt_mt_w_unc2Up",
            "CMS_rawFF_mt_qcd_0jet_unc1Down",
            "CMS_rawFF_mt_qcd_0jet_unc2Down",
            "CMS_rawFF_mt_qcd_1jet_unc1Down",
            "CMS_rawFF_mt_qcd_1jet_unc2Down",
            "CMS_rawFF_mt_qcd_2jet_unc1Down",
            "CMS_rawFF_mt_qcd_2jet_unc2Down",
            "CMS_rawFF_mt_w_0jet_unc1Down",
            "CMS_rawFF_mt_w_0jet_unc2Down",
            "CMS_rawFF_mt_w_1jet_unc1Down",
            "CMS_rawFF_mt_w_1jet_unc2Down",
            "CMS_rawFF_mt_w_2jet_unc1Down",
            "CMS_rawFF_mt_w_2jet_unc2Down",
            "CMS_rawFF_mt_tt_unc1Down",
            "CMS_rawFF_mt_tt_unc2Down",      
            "CMS_FF_closure_lpt_xtrg_mt_qcdDown",
	    "CMS_FF_closure_lpt_xtrg_mt_wDown",
	    "CMS_FF_closure_lpt_xtrg_mt_ttDown",
	    "CMS_FF_closure_lpt_mt_qcdDown",
	    "CMS_FF_closure_lpt_mt_wDown",
	    "CMS_FF_closure_lpt_mt_ttDown",
            "CMS_FF_closure_OSSS_mvis_mt_qcdDown",            
            "CMS_FF_closure_mt_mt_w_unc1Down",
            "CMS_FF_closure_mt_mt_w_unc2Down",
            ]
        self.eventDictionaryModifications = {
            "CMS_rawFF_mt_qcd_0jet_unc1Up":self.CreateRawQCD0JetUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_unc2Up":self.CreateRawQCD0JetUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc1Up":self.CreateRawQCD1JetUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc2Up":self.CreateRawQCD1JetUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_2jet_unc1Up":self.CreateRawQCD2JetUnc1UpDictionary,
            "CMS_rawFF_mt_qcd_2jet_unc2Up":self.CreateRawQCD2JetUnc2UpDictionary,
            "CMS_rawFF_mt_w_0jet_unc1Up":self.CreateRawW0JetUnc1UpDictionary,
            "CMS_rawFF_mt_w_0jet_unc2Up":self.CreateRawW0JetUnc2UpDictionary,
            "CMS_rawFF_mt_w_1jet_unc1Up":self.CreateRawW1JetUnc1UpDictionary,
            "CMS_rawFF_mt_w_1jet_unc2Up":self.CreateRawW1JetUnc2UpDictionary,
            "CMS_rawFF_mt_w_2jet_unc1Up":self.CreateRawW2JetUnc1UpDictionary,
            "CMS_rawFF_mt_w_2jet_unc2Up":self.CreateRawW2JetUnc2UpDictionary,
            "CMS_rawFF_mt_tt_unc1Up":self.CreateRawTT0JetUnc1UpDictionary,
            "CMS_rawFF_mt_tt_unc2Up":self.CreateRawTT0JetUnc2UpDictionary,
            "CMS_FF_closure_lpt_xtrg_mt_qcdUp":self.CreateLPTClosureXTrgQCDUpDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_wUp":self.CreateLPTClosureXTrgWUpDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_ttUp":self.CreateLPTClosureXTrgTTUpDictionary,
	    "CMS_FF_closure_lpt_mt_qcdUp":self.CreateLPTClosureQCDUpDictionary,
	    "CMS_FF_closure_lpt_mt_wUp":self.CreateLPTClosureWUpDictionary,
	    "CMS_FF_closure_lpt_mt_ttUp":self.CreateLPTClosureTTUpDictionary,
            "CMS_FF_closure_OSSS_mvis_mt_qcdUp":self.CreateOSSSClosureQCDUnc1UpDictionary,
            "CMS_FF_closure_mt_mt_w_unc1Up":self.CreateMTClosureWUnc1UpDictionary,
            "CMS_FF_closure_mt_mt_w_unc2Up":self.CreateMTClosureWUnc2UpDictionary,
            "CMS_rawFF_mt_qcd_0jet_unc1Down":self.CreateRawQCD0JetUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_0jet_unc2Down":self.CreateRawQCD0JetUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc1Down":self.CreateRawQCD1JetUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_1jet_unc2Down":self.CreateRawQCD1JetUnc2DownDictionary,
            "CMS_rawFF_mt_qcd_2jet_unc1Down":self.CreateRawQCD2JetUnc1DownDictionary,
            "CMS_rawFF_mt_qcd_2jet_unc2Down":self.CreateRawQCD2JetUnc2DownDictionary,
            "CMS_rawFF_mt_w_0jet_unc1Down":self.CreateRawW0JetUnc1DownDictionary,
            "CMS_rawFF_mt_w_0jet_unc2Down":self.CreateRawW0JetUnc2DownDictionary,
            "CMS_rawFF_mt_w_1jet_unc1Down":self.CreateRawW1JetUnc1DownDictionary,
            "CMS_rawFF_mt_w_1jet_unc2Down":self.CreateRawW1JetUnc2DownDictionary,
            "CMS_rawFF_mt_w_2jet_unc1Down":self.CreateRawW2JetUnc1DownDictionary,
            "CMS_rawFF_mt_w_2jet_unc2Down":self.CreateRawW2JetUnc2DownDictionary,
            "CMS_rawFF_mt_tt_unc1Down":self.CreateRawTT0JetUnc1DownDictionary,
            "CMS_rawFF_mt_tt_unc2Down":self.CreateRawTT0JetUnc2DownDictionary,
            "CMS_FF_closure_lpt_xtrg_mt_qcdDown":self.CreateLPTClosureXTrgQCDDownDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_wDown":self.CreateLPTClosureXTrgWDownDictionary,
	    "CMS_FF_closure_lpt_xtrg_mt_ttDown":self.CreateLPTClosureXTrgTTDownDictionary,
	    "CMS_FF_closure_lpt_mt_qcdDown":self.CreateLPTClosureQCDDownDictionary,
	    "CMS_FF_closure_lpt_mt_wDown":self.CreateLPTClosureWDownDictionary,
	    "CMS_FF_closure_lpt_mt_ttDown":self.CreateLPTClosureTTDownDictionary,
            "CMS_FF_closure_OSSS_mvis_mt_qcdDown":self.CreateOSSSClosureQCDUnc1DownDictionary,            
            "CMS_FF_closure_mt_mt_w_unc1Down":self.CreateMTClosureWUnc1DownDictionary,
            "CMS_FF_closure_mt_mt_w_unc2Down":self.CreateMTClosureWUnc2DownDictionary
            }

        #QCD raw uncerts
    def CreateRawQCD0JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD0JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD0JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD0JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_0jet_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD1JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_1jet_unc2_down
        return modifiedEventDictionary
    def CreateRawQCD2JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_unc1_up
        return modifiedEventDictionary
    def CreateRawQCD2JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_unc1_down
        return modifiedEventDictionary
    def CreateRawQCD2JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_unc2_up
        return modifiedEventDictionary
    def CreateRawQCD2JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_qcd_2jet_unc2_down
        return modifiedEventDictionary
    #W raw uncerts
    def CreateRawW0JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc1_up
        return modifiedEventDictionary
    def CreateRawW0JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc1_down
        return modifiedEventDictionary
    def CreateRawW0JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc2_up
        return modifiedEventDictionary
    def CreateRawW0JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_0jet_unc2_down
        return modifiedEventDictionary
    def CreateRawW1JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc1_up
        return modifiedEventDictionary
    def CreateRawW1JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc1_down
        return modifiedEventDictionary
    def CreateRawW1JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc2_up
        return modifiedEventDictionary
    def CreateRawW1JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_1jet_unc2_down
        return modifiedEventDictionary
    def CreateRawW2JetUnc1UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_unc1_up
        return modifiedEventDictionary
    def CreateRawW2JetUnc1DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_unc1_down
        return modifiedEventDictionary
    def CreateRawW2JetUnc2UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_unc2_up
        return modifiedEventDictionary
    def CreateRawW2JetUnc2DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.ff_w_2jet_unc2_down
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
        """
        #QCD mvis closure
    def CreateMvisClosureQCD0JetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_0jet_up
        return modifiedEventDictionary
    def CreateMvisClosureQCD0JetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_0jet_down
        return modifiedEventDictionary        
    def CreateMvisClosureQCD1JetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_1jet_up
        return modifiedEventDictionary
    def CreateMvisClosureQCD1JetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_1jet_down
        return modifiedEventDictionary        
    def CreateMvisClosureQCD2JetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_2jet_up
        return modifiedEventDictionary
    def CreateMvisClosureQCD2JetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_qcd_2jet_down
        return modifiedEventDictionary        

        #W mvis closure
    def CreateMvisClosureW0JetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_0jet_up
        return modifiedEventDictionary
    def CreateMvisClosureW0JetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_0jet_down
        return modifiedEventDictionary
    def CreateMvisClosureW1JetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_1jet_up
        return modifiedEventDictionary
    def CreateMvisClosureW1JetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_1jet_down
        return modifiedEventDictionary
    def CreateMvisClosureW2JetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_2jet_up
        return modifiedEventDictionary
    def CreateMvisClosureW2JetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_w_2jet_down
        return modifiedEventDictionary
        
        #ttbar mvis closure
    def CreateMvisClosureTTUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_tt_up
        return modifiedEventDictionary
    def CreateMvisClosureTTDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting * theTree.mvisclosure_tt_down
        return modifiedEventDictionary    
        """
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

