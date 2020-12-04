from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class JERUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'JER'
        self.uncertaintyNames=[
            "CMS_res_jUp",
            "CMS_res_jDown",
        ]

        self.eventDictionaryModifications = {
            "CMS_res_jUp":self.CreateJERUpDictionary,
            "CMS_res_jDown":self.CreateJERDownDictionary,
            }

    def CreateJERUpDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()

        jetPt = theTree.jpt_1_JERUp
        if jetPt < 0 :
            jetPt = 0

        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JERUp,0.0,theTree.metphi_JERUp,0.0)
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JERUp
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JERUp
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JERUp
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary

    def CreateJERDownDictionary(self,theTree,nominalEventDictionary):
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met_JERDown,0.0,theTree.metphi_JERDown,0.0)

        jetPt = theTree.jpt_1_JERDown
        if jetPt < 0 :
            jetPt = 0
        
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.basicQuantities['MET'] = metVector.Pt()
        modifiedEventDictionary.basicQuantities['METPhi'] = metVector.Phi()
        modifiedEventDictionary.basicQuantities['Njets'] = theTree.njets_JERDown
        modifiedEventDictionary.basicQuantities['mjj'] = theTree.mjj_JERDown
        modifiedEventDictionary.basicQuantities['M_sv'] = theTree.m_sv_JERDown
        modifiedEventDictionary.basicQuantities['LJetPt'] = jetPt
        
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
