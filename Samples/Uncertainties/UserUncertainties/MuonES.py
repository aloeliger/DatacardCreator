from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class MuonESUncertainty(Uncertainty):
    def __init__(self):
        self.name = "MuonES"
        self.uncertaintyNames=[
            "CMS_scale_m_etalt1p2Up",
            "CMS_scale_m_etalt1p2Down",            
            "CMS_scale_m_eta1p2to2p1Up",
            "CMS_scale_m_eta1p2to2p1Down",
            "CMS_scale_m_eta2p1to2p4Up",
            "CMS_scale_m_eta2p1to2p4Down",
        ]
        self.eventDictionaryModifications = {
            "CMS_scale_m_etalt1p2Up":self.CreateMuonEtaLt1p2UpDictionary,
            "CMS_scale_m_etalt1p2Down":self.CreateMuonEtaLt1p2DownDictionary,            
            "CMS_scale_m_eta1p2to2p1Up":self.CreateMuonEta1p2to2p1UpDictionary,
            "CMS_scale_m_eta1p2to2p1Down":self.CreateMuonEta1p2to2p1DownDictionary,
            "CMS_scale_m_eta2p1to2p4Up":self.CreateMuonEta2p1to2p4UpDictionary,
            "CMS_scale_m_eta2p1to2p4Down":self.CreateMuonEta2p1to2p4DownDictionary,
            }
    def CreateMuonEtaLt1p2UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if (abs(theTree.eta_1) < 1.2):            
            muVector.SetPtEtaPhiE(theTree.muonES_Pt_UP,theTree.eta_1,theTree.phi_1,theTree.muonES_E_UP)
            metVector.SetPtEtaPhiM(theTree.muonES_MET_UP,0.0,theTree.muonES_METPhi_UP,0.0)
            new_msv = theTree.m_sv_muonESUp
        else:            
            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MuPt"] = muVector.Pt()
        modifiedEventDictionary.basicQuantities["MuM"] = muVector.M()
        modifiedEventDictionary.basicQuantities["MuE"] = muVector.E()
        modifiedEventDictionary.basicQuantities["MET"]  = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()                


        """
        nominallyBelongsInBin = False
        modifiedBelongsInBin = False
        printMe = False
        if(nominalEventDictionary.eventDictionary["Njets"] == 1.0
           and nominalEventDictionary.eventDictionary['MT'] < 50.0
           and nominalEventDictionary.eventDictionary['TauPt'] >= 30.0
           and nominalEventDictionary.eventDictionary['HiggsPt'] <= 60.0
           #and nominalEventDictionary.eventDictionary['M_sv'] >= 150.0
           #and nominalEventDictionary.eventDictionary['M_sv'] <= 170.0
        ):
            nominallyBelongsInBin = True            
        if(modifiedEventDictionary.eventDictionary["Njets"] == 1.0
           and modifiedEventDictionary.eventDictionary['MT'] < 50.0
           and modifiedEventDictionary.eventDictionary['TauPt'] >= 30.0
           and modifiedEventDictionary.eventDictionary['HiggsPt'] <= 60.0
           #and modifiedEventDictionary.eventDictionary['M_sv'] >= 150.0
           #and modifiedEventDictionary.eventDictionary['M_sv'] <= 170.0
        ):
            modifiedBelongsInBin = True
           
            
        if nominallyBelongsInBin and not modifiedBelongsInBin:
            #print("*****This event used to belong to the bin, but fell out****")
            printMe = True
        if not nominallyBelongsInBin and modifiedBelongsInBin:
            #print("*****This event used to not belong to the bin, but entered****")
            printMe = True

        if printMe:
            print("*****Up EventDictionary before:*****")
            nominalEventDictionary.Print()
            print("*****Up EventDictionary after:*****")
            modifiedEventDictionary.Print()
        """

        return modifiedEventDictionary

    def CreateMuonEtaLt1p2DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if (abs(theTree.eta_1) < 1.2):            
            muVector.SetPtEtaPhiE(theTree.muonES_Pt_DOWN,theTree.eta_1,theTree.phi_1,theTree.muonES_E_DOWN)
            metVector.SetPtEtaPhiM(theTree.muonES_MET_DOWN,0.0,theTree.muonES_METPhi_DOWN,0.0)
            new_msv = theTree.m_sv_muonESDown
        else:
            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MuPt"] = muVector.Pt()
        modifiedEventDictionary.basicQuantities["MuM"] = muVector.M()
        modifiedEventDictionary.basicQuantities["MuE"] = muVector.E()
        modifiedEventDictionary.basicQuantities["MET"]  = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities["M_sv"] = new_msv

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()        

        """
        nominallyBelongsInBin = False
        modifiedBelongsInBin = False
        printMe = False
        if(nominalEventDictionary.eventDictionary["Njets"] == 1.0
           and nominalEventDictionary.eventDictionary['MT'] < 50.0
           and nominalEventDictionary.eventDictionary['TauPt'] >= 30.0
           and nominalEventDictionary.eventDictionary['HiggsPt'] <= 60.0
           #and nominalEventDictionary.eventDictionary['M_sv'] >= 150.0
           #and nominalEventDictionary.eventDictionary['M_sv'] <= 170.0
        ):
            nominallyBelongsInBin = True            
        if(modifiedEventDictionary.eventDictionary["Njets"] == 1.0
           and modifiedEventDictionary.eventDictionary['MT'] < 50.0
           and modifiedEventDictionary.eventDictionary['TauPt'] >= 30.0
           and modifiedEventDictionary.eventDictionary['HiggsPt'] <= 60.0
           #and modifiedEventDictionary.eventDictionary['M_sv'] >= 150.0
           #and modifiedEventDictionary.eventDictionary['M_sv'] <= 170.0
        ):
            modifiedBelongsInBin = True
           
            
        if nominallyBelongsInBin and not modifiedBelongsInBin:
            print("*****This event used to belong to the bin, but fell out****")
            printMe = True
        if not nominallyBelongsInBin and modifiedBelongsInBin:
            print("*****This event used to not belong to the bin, but entered****")
            printMe = True

        if printMe:
            print("*****Down EventDictionary before:*****")
            nominalEventDictionary.Print()
            print("*****Down EventDictionary after:*****")
            modifiedEventDictionary.Print()
            print("")
        """

        return modifiedEventDictionary

    def CreateMuonEta1p2to2p1UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if (abs(theTree.eta_1) > 1.2 and abs(theTree.eta_1) < 2.1):            
            muVector.SetPtEtaPhiE(theTree.muonES_Pt_UP,theTree.eta_1,theTree.phi_1,theTree.muonES_E_UP)
            metVector.SetPtEtaPhiM(theTree.muonES_MET_UP,0.0,theTree.muonES_METPhi_UP,0.0)
            new_msv = theTree.m_sv_muonESUp
        else:
            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MuPt"] = muVector.Pt()
        modifiedEventDictionary.basicQuantities["MuM"] = muVector.M()
        modifiedEventDictionary.basicQuantities["MuE"] = muVector.E()
        modifiedEventDictionary.basicQuantities["MET"]  = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
    
    def CreateMuonEta1p2to2p1DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if (abs(theTree.eta_1) > 1.2 and abs(theTree.eta_1) < 2.1):
            muVector.SetPtEtaPhiE(theTree.muonES_Pt_DOWN,theTree.eta_1,theTree.phi_1,theTree.muonES_E_DOWN)
            metVector.SetPtEtaPhiM(theTree.muonES_MET_DOWN,0.0,theTree.muonES_METPhi_DOWN,0.0)
            new_msv = theTree.m_sv_muonESDown
        else:
            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MuPt"] = muVector.Pt()
        modifiedEventDictionary.basicQuantities["MuM"] = muVector.M()
        modifiedEventDictionary.basicQuantities["MuE"] = muVector.E()
        modifiedEventDictionary.basicQuantities["MET"]  = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
        
    def CreateMuonEta2p1to2p4UpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if (abs(theTree.eta_1) > 2.1 and abs(theTree.eta_1) < 2.4):
            muVector.SetPtEtaPhiE(theTree.muonES_Pt_UP,theTree.eta_1,theTree.phi_1,theTree.muonES_E_UP)
            metVector.SetPtEtaPhiM(theTree.muonES_MET_UP,0.0,theTree.muonES_METPhi_UP,0.0)
            new_msv = theTree.m_sv_muonESUp
        else:
            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MuPt"] = muVector.Pt()
        modifiedEventDictionary.basicQuantities["MuM"] = muVector.M()
        modifiedEventDictionary.basicQuantities["MuE"] = muVector.E()
        modifiedEventDictionary.basicQuantities["MET"]  = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
    
    def CreateMuonEta2p1to2p4DownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        new_msv = theTree.m_sv
        if (abs(theTree.eta_1) > 2.1 and abs(theTree.eta_1) < 2.4):
            muVector.SetPtEtaPhiE(theTree.muonES_Pt_DOWN,theTree.eta_1,theTree.phi_1,theTree.muonES_E_DOWN)
            metVector.SetPtEtaPhiM(theTree.muonES_MET_DOWN,0.0,theTree.muonES_METPhi_DOWN,0.0)
            new_msv = theTree.m_sv_muonESDown
        else:
            muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
            
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities["MuPt"] = muVector.Pt()
        modifiedEventDictionary.basicQuantities["MuM"] = muVector.M()
        modifiedEventDictionary.basicQuantities["MuE"] = muVector.E()
        modifiedEventDictionary.basicQuantities["MET"]  = metVector.Pt()
        modifiedEventDictionary.basicQuantities["METPhi"] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['M_sv'] = new_msv

        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
