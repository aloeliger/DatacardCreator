from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class JES17Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'JES'
        self.uncertaintyNames=[
            "CMS_JetAbsoluteUp",
            "CMS_JetAbsolute_2017Up",
            "CMS_JetBBEC1Up",
            "CMS_JetBBEC1_2017Up",
            "CMS_JetEC2Up",
            "CMS_JetEC2_2017Up",
            "CMS_JetFlavorQCDUp",
            "CMS_JetHFUp",
            "CMS_JetHF_2017Up",
            "CMS_JetRelativeSample_2017Up",
            "CMS_JetRelativeBalUp",
            "CMS_JetAbsoluteDown",
            "CMS_JetAbsolute_2017Down",
            "CMS_JetBBEC1Down",
            "CMS_JetBBEC1_2017Down",
            "CMS_JetEC2Down",
            "CMS_JetEC2_2017Down",
            "CMS_JetFlavorQCDDown",
            "CMS_JetHFDown",
            "CMS_JetHF_2017Down",
            "CMS_JetRelativeSample_2017Down",
            "CMS_JetRelativeBalDown"            
            ]

        self.eventDictionaryModifications ={
            "CMS_JetAbsoluteUp":self.CreateJetAbsoluteUpDictionary,
            "CMS_JetAbsolute_2017Up":self.CreateJetAbsolute2017UpDictionary,
            "CMS_JetBBEC1Up":self.CreateJetBBEC1UpDictionary,
            "CMS_JetBBEC1_2017Up":self.CreateJetBBEC12017UpDictionary,
            "CMS_JetEC2Up":self.CreateJetEC2UpDictionary,
            "CMS_JetEC2_2017Up":self.CreateJetEC22017UpDictionary,
            "CMS_JetFlavorQCDUp":self.CreateJetFlavorQCDUpDictionary,
            "CMS_JetHFUp":self.CreateJetHFUpDictionary,
            "CMS_JetHF_2017Up":self.CreateJetHF2017UpDictionary,
            "CMS_JetRelativeSample_2017Up":self.CreateJetRelativeSampleUpDictionary,
            "CMS_JetRelativeBalUp":self.CreateJetRelativeBalUpDictionary,
            "CMS_JetAbsoluteDown":self.CreateJetAbsoluteDownDictionary,
            "CMS_JetAbsolute_2017Down":self.CreateJetAbsolute2017DownDictionary,
            "CMS_JetBBEC1Down":self.CreateJetBBEC1DownDictionary,
            "CMS_JetBBEC1_2017Down":self.CreateJetBBEC12017DownDictionary,
            "CMS_JetEC2Down":self.CreateJetEC2DownDictionary,
            "CMS_JetEC2_2017Down":self.CreateJetEC22017DownDictionary,
            "CMS_JetFlavorQCDDown":self.CreateJetFlavorQCDDownDictionary,
            "CMS_JetHFDown":self.CreateJetHFDownDictionary,
            "CMS_JetHF_2017Down":self.CreateJetHF2017DownDictionary,
            "CMS_JetRelativeSample_2017Down":self.CreateJetRelativeSampleDownDictionary,
            "CMS_JetRelativeBalDown":self.CreateJetRelativeBalDownDictionary            
            }

    def CreateJetAbsoluteUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JetAbsoluteUp,0.0,theTree.metphi_JetAbsoluteUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteyearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteyearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteyearUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetAbsoluteyearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetAbsoluteyearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetAbsoluteyearDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1Up
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1Up
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1Down
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1Down
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1yearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1yearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1yearUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetBBEC1yearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetBBEC1yearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetBBEC1yearDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2Up
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2Up
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2Up
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2Down
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2Down
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2Down
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2yearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2yearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2yearUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetEC2yearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetEC2yearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetEC2yearDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFlavorQCDUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFlavorQCDUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFlavorQCDUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetFlavorQCDDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetFlavorQCDDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetFlavorQCDDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFyearUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFyearUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFyearUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetHFyearDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetHFyearDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetHFyearDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeSampleUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeSampleUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeSampleUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeSampleDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeSampleDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeSampleDown
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeBalUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeBalUp
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeBalUp
        
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
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        #modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JetRelativeBalDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JetRelativeBalDown
        #modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JetRelativeBalDown
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
