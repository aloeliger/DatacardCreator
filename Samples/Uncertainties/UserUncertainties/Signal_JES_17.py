from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class JES17Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'JES'
        self.uncertaintyNames=[
            "CMS_scale_j_AbsoluteUp",
            "CMS_scale_j_Absolute_2017Up",
            "CMS_scale_j_BBEC1Up",
            "CMS_scale_j_BBEC1_2017Up",
            "CMS_scale_j_EC2Up",
            "CMS_scale_j_EC2_2017Up",
            "CMS_scale_j_FlavorQCDUp",
            "CMS_scale_j_HFUp",
            "CMS_scale_j_HF_2017Up",
            "CMS_scale_j_RelativeSample_2017Up",
            "CMS_scale_j_RelativeBalUp",
            "CMS_scale_j_AbsoluteDown",
            "CMS_scale_j_Absolute_2017Down",
            "CMS_scale_j_BBEC1Down",
            "CMS_scale_j_BBEC1_2017Down",
            "CMS_scale_j_EC2Down",
            "CMS_scale_j_EC2_2017Down",
            "CMS_scale_j_FlavorQCDDown",
            "CMS_scale_j_HFDown",
            "CMS_scale_j_HF_2017Down",
            "CMS_scale_j_RelativeSample_2017Down",
            "CMS_scale_j_RelativeBalDown"            
            ]

        self.eventDictionaryModifications ={
            "CMS_scale_j_AbsoluteUp":self.CreateJetAbsoluteUpDictionary,
            "CMS_scale_j_Absolute_2017Up":self.CreateJetAbsolute2017UpDictionary,
            "CMS_scale_j_BBEC1Up":self.CreateJetBBEC1UpDictionary,
            "CMS_scale_j_BBEC1_2017Up":self.CreateJetBBEC12017UpDictionary,
            "CMS_scale_j_EC2Up":self.CreateJetEC2UpDictionary,
            "CMS_scale_j_EC2_2017Up":self.CreateJetEC22017UpDictionary,
            "CMS_scale_j_FlavorQCDUp":self.CreateJetFlavorQCDUpDictionary,
            "CMS_scale_j_HFUp":self.CreateJetHFUpDictionary,
            "CMS_scale_j_HF_2017Up":self.CreateJetHF2017UpDictionary,
            "CMS_scale_j_RelativeSample_2017Up":self.CreateJetRelativeSampleUpDictionary,
            "CMS_scale_j_RelativeBalUp":self.CreateJetRelativeBalUpDictionary,
            "CMS_scale_j_AbsoluteDown":self.CreateJetAbsoluteDownDictionary,
            "CMS_scale_j_Absolute_2017Down":self.CreateJetAbsolute2017DownDictionary,
            "CMS_scale_j_BBEC1Down":self.CreateJetBBEC1DownDictionary,
            "CMS_scale_j_BBEC1_2017Down":self.CreateJetBBEC12017DownDictionary,
            "CMS_scale_j_EC2Down":self.CreateJetEC2DownDictionary,
            "CMS_scale_j_EC2_2017Down":self.CreateJetEC22017DownDictionary,
            "CMS_scale_j_FlavorQCDDown":self.CreateJetFlavorQCDDownDictionary,
            "CMS_scale_j_HFDown":self.CreateJetHFDownDictionary,
            "CMS_scale_j_HF_2017Down":self.CreateJetHF2017DownDictionary,
            "CMS_scale_j_RelativeSample_2017Down":self.CreateJetRelativeSampleDownDictionary,
            "CMS_scale_j_RelativeBalDown":self.CreateJetRelativeBalDownDictionary            
            }

    def CreateJetAbsoluteUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteUp,0.0,theTree.metphi_JetAbsoluteUp,0.0)

        jetPt = theTree.jpt_1_JetAbsoluteUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetAbsoluteDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteDown,0.0,theTree.metphi_JetAbsoluteDown,0.0)

        jetPt = theTree.jpt_1_JetAbsoluteDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetAbsolute2017UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteyearUp,0.0,theTree.metphi_JetAbsoluteyearUp,0.0)

        jetPt = theTree.jpt_1_JetAbsoluteyearUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteyearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteyearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteyearUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetAbsolute2017DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteyearDown,0.0,theTree.metphi_JetAbsoluteyearDown,0.0)

        jetPt = theTree.jpt_1_JetAbsoluteyearDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteyearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteyearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteyearDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
    

    def CreateJetBBEC1UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetBBEC1Up,0.0,theTree.metphi_JetBBEC1Up,0.0)

        jetPt = theTree.jpt_1_JetBBEC1Up
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1Up
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1Up
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetBBEC1DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetBBEC1Down,0.0,theTree.metphi_JetBBEC1Down,0.0)

        jetPt = theTree.jpt_1_JetBBEC1Down
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1Down
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1Down
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetBBEC12017UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetBBEC1yearUp,0.0,theTree.metphi_JetBBEC1yearUp,0.0)

        jetPt = theTree.jpt_1_JetBBEC1yearUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1yearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1yearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1yearUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetBBEC12017DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetBBEC1yearDown,0.0,theTree.metphi_JetBBEC1yearDown,0.0)

        jetPt = theTree.jpt_1_JetBBEC1yearDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1yearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1yearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1yearDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetEC2UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetEC2Up,0.0,theTree.metphi_JetEC2Up,0.0)

        jetPt = theTree.jpt_1_JetEC2Up
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2Up
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2Up
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetEC2DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetEC2Down,0.0,theTree.metphi_JetEC2Down,0.0)

        jetPt = theTree.jpt_1_JetEC2Down
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2Down
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2Down
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetEC22017UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetEC2yearUp,0.0,theTree.metphi_JetEC2yearUp,0.0)

        jetPt = theTree.jpt_1_JetEC2yearUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2yearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2yearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2yearUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetEC22017DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetEC2yearDown,0.0,theTree.metphi_JetEC2yearDown,0.0)

        jetPt = theTree.jpt_1_JetEC2yearDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2yearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2yearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2yearDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
    
    def CreateJetFlavorQCDUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetFlavorQCDUp,0.0,theTree.metphi_JetFlavorQCDUp,0.0)

        jetPt = theTree.jpt_1_JetFlavorQCDUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFlavorQCDUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFlavorQCDUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFlavorQCDUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetFlavorQCDDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetFlavorQCDDown,0.0,theTree.metphi_JetFlavorQCDDown,0.0)

        jetPt = theTree.jpt_1_JetFlavorQCDDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFlavorQCDDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFlavorQCDDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFlavorQCDDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetHFUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetHFUp,0.0,theTree.metphi_JetHFUp,0.0)

        jetPt = theTree.jpt_1_JetHFUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetHFDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetHFDown,0.0,theTree.metphi_JetHFDown,0.0)

        jetPt = theTree.jpt_1_JetHFDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetHF2017UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetHFyearUp,0.0,theTree.metphi_JetHFyearUp,0.0)

        jetPt = theTree.jpt_1_JetHFyearUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFyearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFyearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFyearUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetHF2017DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetHFyearDown,0.0,theTree.metphi_JetHFyearDown,0.0)

        jetPt = theTree.jpt_1_JetHFyearDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFyearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFyearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFyearDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetRelativeSampleUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeSampleUp,0.0,theTree.metphi_JetRelativeSampleUp,0.0)

        jetPt = theTree.jpt_1_JetRelativeSampleUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeSampleUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeSampleUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeSampleUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetRelativeSampleDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeSampleDown,0.0,theTree.metphi_JetRelativeSampleDown,0.0)

        jetPt = theTree.jpt_1_JetRelativeSampleDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeSampleDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeSampleDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeSampleDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetRelativeBalUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeBalUp,0.0,theTree.metphi_JetRelativeBalUp,0.0)

        jetPt = theTree.jpt_1_JetRelativeBalUp
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeBalUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeBalUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeBalUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJetRelativeBalDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetRelativeBalDown,0.0,theTree.metphi_JetRelativeBalDown,0.0)

        jetPt = theTree.jpt_1_JetRelativeBalDown
        if jetPt < 0:
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeBalDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeBalDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeBalDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
