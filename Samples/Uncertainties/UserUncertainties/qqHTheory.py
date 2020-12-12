from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class qqHTheoryUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'qqHTheory'
        self.uncertaintyNames = [
            'THU_qqH_yieldUp',
            'THU_qqH_PTH200Up',
            'THU_qqH_Mjj60Up',
            'THU_qqH_Mjj120Up',
            'THU_qqH_Mjj350Up',
            'THU_qqH_Mjj700Up',
            'THU_qqH_Mjj1000Up',
            'THU_qqH_Mjj1500Up',
            'THU_qqH_PTH25Up',
            'THU_qqH_JET01Up',
            'THU_qqH_yieldDown',
            'THU_qqH_PTH200Down',
            'THU_qqH_Mjj60Down',
            'THU_qqH_Mjj120Down',
            'THU_qqH_Mjj350Down',
            'THU_qqH_Mjj700Down',
            'THU_qqH_Mjj1000Down',
            'THU_qqH_Mjj1500Down',
            'THU_qqH_PTH25Down',
            'THU_qqH_JET01Down',
        ]
        self.eventDictionaryModifications = {
            'THU_qqH_yieldUp':self.CreateYieldUpDictionary,
            'THU_qqH_PTH200Up':self.CreatePTH200UpDictionary,
            'THU_qqH_Mjj60Up':self.CreateMjj60UpDictionary,
            'THU_qqH_Mjj120Up':self.CreateMjj120UpDictionary,
            'THU_qqH_Mjj350Up':self.CreateMjj350UpDictionary,
            'THU_qqH_Mjj700Up':self.CreateMjj700UpDictionary,
            'THU_qqH_Mjj1000Up':self.CreateMjj1000UpDictionary,
            'THU_qqH_Mjj1500Up':self.CreateMjj1500UpDictionary,
            'THU_qqH_PTH25Up':self.CreatePTH25UpDictionary,
            'THU_qqH_JET01Up':self.CreateJET01UpDictionary,
            'THU_qqH_yieldDown':self.CreateYieldDownDictionary,
            'THU_qqH_PTH200Down':self.CreatePTH200DownDictionary,
            'THU_qqH_Mjj60Down':self.CreateMjj60DownDictionary,
            'THU_qqH_Mjj120Down':self.CreateMjj120DownDictionary,
            'THU_qqH_Mjj350Down':self.CreateMjj350DownDictionary,
            'THU_qqH_Mjj700Down':self.CreateMjj700DownDictionary,
            'THU_qqH_Mjj1000Down':self.CreateMjj1000DownDictionary,
            'THU_qqH_Mjj1500Down':self.CreateMjj1500DownDictionary,
            'THU_qqH_PTH25Down':self.CreatePTH25DownDictionary,
            'THU_qqH_JET01Down':self.CreateJET01DownDictionary,
            }
    def CreateYieldUpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_yield_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateYieldDownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_yield_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePTH200UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_PTH200_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePTH200DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_PTH200_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj60UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj60_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj60DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj60_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj120UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj120_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj120DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj120_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj350UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj350_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj350DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj350_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj700UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj700_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj700DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj700_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj1000UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj1000_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj1000DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj1000_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj1500UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj1500_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMjj1500DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_Mjj1500_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePTH25UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_PTH25_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePTH25DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_PTH25_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateJET01UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_JET01_up)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateJET01DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting * theTree.THU_qqH_JET01_down)
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary
