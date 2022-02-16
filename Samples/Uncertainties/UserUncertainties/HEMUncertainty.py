from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class HEMUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'HEM_failure'
        self.uncertaintyNames=[
            "CMS_HEM_failureDown",
            "CMS_HEM_failureUp",
        ]
        self.eventDictionaryModifications={
            "CMS_HEM_failureDown":self.CreateHEMFailureDictionaryDown,
            "CMS_HEM_failureUp":self.CreateHEMFailureDictionaryUp,
            }
    def CreateHEMFailureDictionaryDown(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #we need this too
        METVector = ROOT.TLorentzVector()
        METVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        #there's approximately three things that can happen here
        #one, there can be no jets in the event, 
        #in that case, we're done here
        if theTree.njets == 0:
            return modifiedEventDictionary
        #if there's one jet, we modify it downward
        #if it falls under pt 30, it drops out
        #otherwise,rerecord the information
        if theTree.njets == 1:
            jetOneVector = ROOT.TLorentzVector()
            jetOneVector.SetPtEtaPhiM(theTree.jpt_1,theTree.jeta_1,theTree.jphi_1,0.0)
            newJetOneVector = jetOneVector
            if(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
               jetOneVector.Eta() < -1.3 and jetOneVector.Eta() > -2.5):
                newJetOneVector = jetOneVector * 0.8
            elif(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
                 jetOneVector.Eta() < -2.5 and jetOneVector.Eta() > -3.0 ):
                newJetOneVector = jetOneVector * 0.65
            #no matter what happens, we have to recalculate met now
            newMETVector = (jetOneVector+METVector-newJetOneVector)
            modifiedEventDictionary.basicQuantities['MET'] = METVector.Phi()
            modifiedEventDictionary.basicQuantities['METPhi'] = newMETVector.Phi()
            #if the pt has fallen under 30, we just lost this jet
            if (jetOneVector.Pt() < 30.0):
                modifiedEventDictionary.basicQuantities['Njets'] = 0
                modifiedEventDictionary.basicQuantities['LJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['LJetPhi'] = 0.0        
            else:
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetOneVector.Phi()
        #in the two jet case things are complicated.
        #first let's check the leading jet
        #case one, we modify, it's fine
        # we fill in leading jet information
        #case two, it's downgraded out, and we make the second jet the leading jet
        #then, if there's still a second jet, we check it,
        #
        else:
            jetOneVector = ROOT.TLorentzVector()
            jetOneVector.SetPtEtaPhiM(theTree.jpt_1,theTree.jeta_1,theTree.jphi_1,0.0)
            newJetOneVector = jetOneVector
            if(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
               jetOneVector.Eta() < -1.3 and jetOneVector.Eta() > -2.5):
                newJetOneVector = jetOneVector * 0.8
            elif(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
                 jetOneVector.Eta() < -2.5 and jetOneVector.Eta() > -3.0 ):
                newJetOneVector = jetOneVector * 0.65
            jetTwoVector = ROOT.TLorentzVector()
            jetTwoVector.SetPtEtaPhiM(theTree.jpt_2,theTree.jeta_2,theTree.jphi_2,0.0)
            newJetTwoVector = jetTwoVector
            if(jetTwoVector.Phi() < -0.87 and jetTwoVector.Phi() > -1.57 and
               jetTwoVector.Eta() < -1.3 and jetTwoVector.Eta() > -2.5):
                newJetTwoVector = jetTwoVector * 0.8
            elif(jetTwoVector.Phi() < -0.87 and jetTwoVector.Phi() > -1.57 and
                 jetTwoVector.Eta() < -2.5 and jetTwoVector.Eta() > -3.0 ):
                newJetTwoVector = jetTwoVector * 0.65
            #no matter what happens, we have to recalculate met now
            newMETVector = (jetOneVector+jetTwoVector+METVector-newJetOneVector-newJetTwoVector)
            modifiedEventDictionary.basicQuantities['MET'] = METVector.Phi()
            modifiedEventDictionary.basicQuantities['METPhi'] = newMETVector.Phi()
            #okay, four possible cases
            #Both jets still pass
            #jet one fails, jet two passes
            #jet one passes, jet two fails
            #both jets fail
            if(newJetOneVector.Pt() > 30.0 and newJetTwoVector.Pt() > 30.0):
                modifiedEventDictionary.basicQuantities['Mjj'] = (newJetOneVector+newJetTwoVector).M()
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetOneVector.Phi()
                modifiedEventDictionary.basicQuantities['SLJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['SLJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = newJetOneVector.Phi()
            elif(newJetOneVector.Pt() < 30.0 and newJetTwoVector.Pt() > 30.0):
                modifiedEventDictionary.basicQuantities['Njets'] = 1
                modifiedEventDictionary.basicQuantities['Mjj'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetTwoVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetTwoVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetTwoVector.Phi()
                modifiedEventDictionary.basicQuantities['SLJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['SLJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = 0.0
            elif(newJetOneVector.Pt() > 30.0 and newJetTwoVector.Pt() < 30.0):
                modifiedEventDictionary.basicQuantities['Njets'] = 1
                modifiedEventDictionary.basicQuantities['Mjj'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetOneVector.Phi()
                modifiedEventDictionary.basicQuantities['SLJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['SLJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = 0.0
            else:
                modifiedEventDictionary.basicQuantities['Njets'] = 0
                modifiedEventDictionary.basicQuantities['Mjj'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['LJetPhi'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['SLJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = 0.0
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
    
    def CreateHEMFailureDictionaryUp(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        #we need this too
        METVector = ROOT.TLorentzVector()
        METVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)
        #there's approximately three things that can happen here
        #one, there can be no jets in the event, 
        #in that case, we're done here
        if theTree.njets == 0:
            return modifiedEventDictionary
        #if there's one jet, we modify it downward
        #if it falls under pt 30, it drops out
        #otherwise,rerecord the information
        if theTree.njets == 1:
            jetOneVector = ROOT.TLorentzVector()
            jetOneVector.SetPtEtaPhiM(theTree.jpt_1,theTree.jeta_1,theTree.jphi_1,0.0)
            newJetOneVector = jetOneVector
            if(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
               jetOneVector.Eta() < -1.3 and jetOneVector.Eta() > -2.5):
                newJetOneVector = jetOneVector * 1.2
            elif(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
                 jetOneVector.Eta() < -2.5 and jetOneVector.Eta() > -3.0 ):
                newJetOneVector = jetOneVector * 1.35
            #no matter what happens, we have to recalculate met now
            newMETVector = (jetOneVector+METVector-newJetOneVector)
            modifiedEventDictionary.basicQuantities['MET'] = METVector.Phi()
            modifiedEventDictionary.basicQuantities['METPhi'] = newMETVector.Phi()
            #if the pt has fallen under 30, we just lost this jet
            if (jetOneVector.Pt() < 30.0):
                modifiedEventDictionary.basicQuantities['Njets'] = 0
                modifiedEventDictionary.basicQuantities['LJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['LJetPhi'] = 0.0        
            else:
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetOneVector.Phi()
        #in the two jet case things are complicated.
        #first let's check the leading jet
        #case one, we modify, it's fine
        # we fill in leading jet information
        #case two, it's downgraded out, and we make the second jet the leading jet
        #then, if there's still a second jet, we check it,
        #
        else:
            jetOneVector = ROOT.TLorentzVector()
            jetOneVector.SetPtEtaPhiM(theTree.jpt_1,theTree.jeta_1,theTree.jphi_1,0.0)
            newJetOneVector = jetOneVector
            if(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
               jetOneVector.Eta() < -1.3 and jetOneVector.Eta() > -2.5):
                newJetOneVector = jetOneVector * 1.2
            elif(jetOneVector.Phi() < -0.87 and jetOneVector.Phi() > -1.57 and
                 jetOneVector.Eta() < -2.5 and jetOneVector.Eta() > -3.0 ):
                newJetOneVector = jetOneVector * 1.35
            jetTwoVector = ROOT.TLorentzVector()
            jetTwoVector.SetPtEtaPhiM(theTree.jpt_2,theTree.jeta_2,theTree.jphi_2,0.0)
            newJetTwoVector = jetTwoVector
            if(jetTwoVector.Phi() < -0.87 and jetTwoVector.Phi() > -1.57 and
               jetTwoVector.Eta() < -1.3 and jetTwoVector.Eta() > -2.5):
                newJetTwoVector = jetTwoVector * 1.2
            elif(jetTwoVector.Phi() < -0.87 and jetTwoVector.Phi() > -1.57 and
                 jetTwoVector.Eta() < -2.5 and jetTwoVector.Eta() > -3.0 ):
                newJetTwoVector = jetTwoVector * 1.35
            #no matter what happens, we have to recalculate met now
            newMETVector = (jetOneVector+jetTwoVector+METVector-newJetOneVector-newJetTwoVector)
            modifiedEventDictionary.basicQuantities['MET'] = METVector.Phi()
            modifiedEventDictionary.basicQuantities['METPhi'] = newMETVector.Phi()
            #okay, four possible cases
            #Both jets still pass
            #jet one fails, jet two passes
            #jet one passes, jet two fails
            #both jets fail
            if(newJetOneVector.Pt() > 30.0 and newJetTwoVector.Pt() > 30.0):
                modifiedEventDictionary.basicQuantities['Mjj'] = (newJetOneVector+newJetTwoVector).M()
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetOneVector.Phi()
                modifiedEventDictionary.basicQuantities['SLJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['SLJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = newJetOneVector.Phi()
            elif(newJetOneVector.Pt() < 30.0 and newJetTwoVector.Pt() > 30.0):
                modifiedEventDictionary.basicQuantities['Njets'] = 1
                modifiedEventDictionary.basicQuantities['Mjj'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetTwoVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetTwoVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetTwoVector.Phi()
                modifiedEventDictionary.basicQuantities['SLJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['SLJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = 0.0
            elif(newJetOneVector.Pt() > 30.0 and newJetTwoVector.Pt() < 30.0):
                modifiedEventDictionary.basicQuantities['Njets'] = 1
                modifiedEventDictionary.basicQuantities['Mjj'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetPt'] = newJetOneVector.Pt()
                modifiedEventDictionary.basicQuantities['LJetEta'] = newJetOneVector.Eta()
                modifiedEventDictionary.basicQuantities['LJetPhi'] = newJetOneVector.Phi()
                modifiedEventDictionary.basicQuantities['SLJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['SLJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = 0.0
            else:
                modifiedEventDictionary.basicQuantities['Njets'] = 0
                modifiedEventDictionary.basicQuantities['Mjj'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['LJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['LJetPhi'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPt'] = -1.0
                modifiedEventDictionary.basicQuantities['SLJetEta'] = 0.0
                modifiedEventDictionary.basicQuantities['SLJetPhi'] = 0.0
        modifiedEventDictionary.FillConstructedQuantities(modifiedEventDictionary,modifiedEventDictionary.basicQuantities)
        modifiedEventDictionary.CompileCompleteDictionary()
        
        return modifiedEventDictionary
