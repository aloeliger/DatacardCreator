from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class EmbeddedZeroJetUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'EmbeddedZeroJet'
        self.uncertaintyNames=[
            'CMS_EmbeddedZeroJetUp',
            'CMS_EmbeddedZeroJetDown'
        ]
        
        self.eventDictionaryModifications = {
            'CMS_EmbeddedZeroJetUp':self.CreateEmbeddedZeroJetUpDictionary,
            'CMS_EmbeddedZeroJetDown':self.CreateEmbeddedZeroJetDownDictionary,
        }
        
    def CreateEmbeddedZeroJetUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 0:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight*1.15
        return modifiedEventDictionary
    
    def CreateEmbeddedZeroJetDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        if modifiedEventDictionary.basicQuantities['Njets'] == 0:
            modifiedEventDictionary.Weight = modifiedEventDictionary.Weight*0.85
        return modifiedEventDictionary
