import ROOT
from Samples.EventDefinition.EventDictionary import EventDictionary
import math

def FillMuTauBasicQuantities(theEventDictionary,theTree):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()
    jetOneVector = ROOT.TLorentzVector()
    jetTwoVector = ROOT.TLorentzVector()
    leadingJetPt = 0
    if theTree.jpt_1 < 0:
        leadingJetPt = 0
    else:
        leadingJetPt = theTree.jpt_1
    muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
    tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
    METVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
    jetOneVector.SetPtEtaPhiM(leadingJetPt,theTree.jeta_1,theTree.jphi_1,0.0)
    jetTwoVector.SetPtEtaPhiM(theTree.jpt_2,theTree.jeta_2,theTree.jphi_2,0.0)
    theEventDictionary.basicQuantities = {
        "MuPt": muVector.Pt(),
        "MuEta": muVector.Eta(),
        "MuPhi": muVector.Phi(),
        "MuM": muVector.M(),
        "MuE": muVector.E(),
        "TauPt": tauVector.Pt(),
        "TauEta": tauVector.Eta(),
        "TauPhi": tauVector.Phi(),
        "TauM": tauVector.M(),
        "TauE": tauVector.E(),
        "MET": theTree.met,
        "METPhi": theTree.metphi,
        "Njets": theTree.njets,
        "mjj": theTree.mjj,
        "M_sv": theTree.m_sv,
        "LJetPt": jetOneVector.Pt(),
        "LJetPhi": jetOneVector.Phi(),
        "LJetEta": jetOneVector.Eta(),
        "SLJetPt": jetTwoVector.Pt(),
        "SLJetPhi": jetTwoVector.Phi(),
        "SLJetEta": jetTwoVector.Eta(),        
        #"run": theTree.run,
        #"lumi": theTree.lumi,
        #"evt": theTree.evt,
    }
def FillMuTauConstructedQuantities(theEventDictionary,theBasicQuantities):
    tauVector = ROOT.TLorentzVector()
    muVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()
    jetOneVector = ROOT.TLorentzVector()
    jetTwoVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theBasicQuantities["TauPt"],theBasicQuantities["TauEta"],theBasicQuantities["TauPhi"],theBasicQuantities["TauM"])
    muVector.SetPtEtaPhiM(theBasicQuantities["MuPt"],theBasicQuantities["MuEta"],theBasicQuantities["MuPhi"],theBasicQuantities["MuM"])
    METVector.SetPtEtaPhiM(theBasicQuantities["MET"],0.0,theBasicQuantities["METPhi"],0.0)    
    jetOneVector.SetPtEtaPhiM(theBasicQuantities["LJetPt"],
                              theBasicQuantities["LJetPhi"],
                              theBasicQuantities["LJetEta"],
                              0.0)
    jetTwoVector.SetPtEtaPhiM(theBasicQuantities["SLJetPt"],
                              theBasicQuantities["SLJetPhi"],
                              theBasicQuantities["SLJetEta"],
                              0.0)
    MVis = (tauVector+muVector).M()
    HiggsPt = (tauVector+muVector+METVector).Pt()
    differentialHiggsPt = (tauVector+muVector+METVector).Pt() * 1.05 #factor added here for differential. This is the calculated shift off gen truth.
    MT = math.sqrt(2.0*muVector.Pt()*METVector.Pt()*(1.0-math.cos(muVector.DeltaPhi(METVector))))
    Higgs_jjPt = (tauVector+muVector+METVector+jetOneVector+jetTwoVector).Pt()
    DeltaR = tauVector.DeltaR(muVector)    
    theEventDictionary.constructedQuantities = {
        "MT": MT,
        "MVis": MVis,
        "HiggsPt": HiggsPt,
        "differentialHiggsPt": differentialHiggsPt,
        "Higgs_jjPt": Higgs_jjPt,
        "DeltaR":DeltaR,
        "DEtaJJ": (abs(jetOneVector.Eta()-jetTwoVector.Eta())),
    }

MuTauEventDictionary = EventDictionary()
MuTauEventDictionary.FillBasicQuantities = FillMuTauBasicQuantities
MuTauEventDictionary.FillConstructedQuantities = FillMuTauConstructedQuantities
