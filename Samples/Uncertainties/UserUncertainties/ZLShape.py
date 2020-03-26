import ROOT
from Samples.Uncertainties.UncertaintyDef import Uncertainty

class ZLShapeUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ZLShape'
        self.uncertaintyNames = [
            "CMS_ZLShape_mt_1prongUp",
            "CMS_ZLShape_mt_1prongDown",
            "CMS_ZLShape_mt_1prong1pizeroUp",
            "CMS_ZLShape_mt_1prong1pizeroDown"
        ]
        self.eventDictionaryModifications = {
            "CMS_ZLShape_mt_1prongUp":self.CreateOneProngUpDictionary,
            "CMS_ZLShape_mt_1prongDown":self.CreateOneProngDownDictionary,
            "CMS_ZLShape_mt_1prong1pizeroUp":self.CreateOneProngOnePizeroUpDictionary,
            "CMS_ZLShape_mt_1prong1pizeroDown":self.CreateOneProngOnePizeroDownDictionary
        }
    def CreateOneProngUpDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        modifiedEventDictionary = nominalEventDictionary.Clone()

        if(theTree.l2_decayMode == 0):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.EES_E_UP)
                metVector.SetPtEtaPhiM(theTree.EES_MET_UP,0.0,theTree.EES_METPhi_DOWN,0.0)                
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.MES_E_UP)
                metVector.SetPtEtaPhiM(theTree.MES_MET_UP,0.0,theTree.MES_METPhi_UP,0.0)
                modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_UP
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)                
            
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        """
        unmoddedTauVector = ROOT.TLorentzVector()
        unmoddedTauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        nominallyBelongsInBin = False
        modifiedBelongsInBin = False
        printMe = False
        if(nominalEventDictionary.eventDictionary["Njets"] == 1.0
           and nominalEventDictionary.eventDictionary['MT'] < 50.0
           and nominalEventDictionary.eventDictionary['TauPt'] >= 30.0
           and nominalEventDictionary.eventDictionary['M_sv'] >= 150.0
           and nominalEventDictionary.eventDictionary['M_sv'] <= 170.0):
            nominallyBelongsInBin = True            
        if(modifiedEventDictionary.eventDictionary["Njets"] == 1.0
           and modifiedEventDictionary.eventDictionary['MT'] < 50.0
           and modifiedEventDictionary.eventDictionary['TauPt'] >= 30.0
           and modifiedEventDictionary.eventDictionary['M_sv'] >= 150.0
           and modifiedEventDictionary.eventDictionary['M_sv'] <= 170.0):
            modifiedBelongsInBin = True
           
            
        if nominallyBelongsInBin and not modifiedBelongsInBin:
            #print("*****This event used to belong to the bin, but fell out****")
            printMe = True
        if not nominallyBelongsInBin and modifiedBelongsInBin:
            #print("*****This event used to not belong to the bin, but entered****")
            printMe = True
        printMe = False
        if printMe:
            print("Tau Decay: "+str(theTree.l2_decayMode))
            print("Tau gen match: "+str(theTree.gen_match_2))
            print("*****Up EventDictionary before:*****")
            nominalEventDictionary.Print()
            print("*****Up EventDictionary after:*****")
            modifiedEventDictionary.Print()
        """

        return modifiedEventDictionary

    def CreateOneProngDownDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()

        modifiedEventDictionary = nominalEventDictionary.Clone()
        
        if(theTree.l2_decayMode == 0):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.EES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.EES_MET_DOWN,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.MES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.MES_MET_DOWN,0.0,theTree.MES_METPhi_DOWN,0.0)
                modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_DOWN
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)                
            
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        """
        unmoddedTauVector = ROOT.TLorentzVector()
        unmoddedTauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        nominallyBelongsInBin = False
        modifiedBelongsInBin = False
        printMe = False
        if(nominalEventDictionary.eventDictionary["Njets"] == 1.0
           and nominalEventDictionary.eventDictionary['MT'] < 50.0
           and nominalEventDictionary.eventDictionary['TauPt'] >= 30.0
           #and nominalEventDictionary.eventDictionary['M_sv'] >= 150.0
           #and nominalEventDictionary.eventDictionary['M_sv'] <= 170.0
        ):
            nominallyBelongsInBin = True            
        if(modifiedEventDictionary.eventDictionary["Njets"] == 1.0
           and modifiedEventDictionary.eventDictionary['MT'] < 50.0
           and modifiedEventDictionary.eventDictionary['TauPt'] >= 30.0
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
            print("Tau Decay: "+str(theTree.l2_decayMode))
            print("Tau gen match: "+str(theTree.gen_match_2))
        print("*****Down EventDictionary before:*****")
            nominalEventDictionary.Print()
            print("*****Down EventDictionary after:*****")
            modifiedEventDictionary.Print()
            print("")
        """

        return modifiedEventDictionary

    def CreateOneProngOnePizeroUpDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()

        modifiedEventDictionary = nominalEventDictionary.Clone()
        
        if(theTree.l2_decayMode == 1):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.EES_E_UP)
                metVector.SetPtEtaPhiM(theTree.EES_MET_UP,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_UP,theTree.eta_2,theTree.phi_2,theTree.MES_E_UP)
                metVector.SetPtEtaPhiM(theTree.MES_MET_UP,0.0,theTree.MES_METPhi_UP,0.0)
                modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_UP
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary

    def CreateOneProngOnePizeroDownDictionary(self,theTree,nominalEventDictionary):
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()

        modifiedEventDictionary = nominalEventDictionary.Clone()
        
        if(theTree.l2_decayMode == 1):
            if(theTree.gen_match_2 == 1 or theTree.gen_match_2 == 3):
                tauVector.SetPtEtaPhiE(theTree.EES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.EES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.EES_MET_DOWN,0.0,theTree.EES_METPhi_DOWN,0.0)
            elif(theTree.gen_match_2 == 2 or theTree.gen_match_2 == 4):
                tauVector.SetPtEtaPhiE(theTree.MES_Pt_DOWN,theTree.eta_2,theTree.phi_2,theTree.MES_E_DOWN)
                metVector.SetPtEtaPhiM(theTree.MES_MET_DOWN,0.0,theTree.MES_METPhi_DOWN,0.0)
                modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_DOWN
            else:
                tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
                metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        else:
            tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
            metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        
        modifiedEventDictionary.basicQuantities['TauPt'] = tauVector.Pt()
        modifiedEventDictionary.basicQuantities['TauM'] = tauVector.M()
        modifiedEventDictionary.basicQuantities['TauE'] = tauVector.E()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()

        return modifiedEventDictionary
