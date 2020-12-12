from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggHTheoryUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggHTheory'
        self.uncertaintyNames = [
            'THU_ggH_MuUp',
            'THU_ggH_MuDown',
            'THU_ggH_ResUp',
            'THU_ggH_ResDown',
            'THU_ggH_Mig01Up',
            'THU_ggH_Mig01Down',
            'THU_ggH_Mig12Up',
            'THU_ggH_Mig12Down',
            'THU_ggH_VBF2jUp',
            'THU_ggH_VBF2jDown',
            'THU_ggH_VBF3jUp',
            'THU_ggH_VBF3jDown',
            'THU_ggH_PT60Up',
            'THU_ggH_PT60Down',
            'THU_ggH_PT120Up',
            'THU_ggH_PT120Down',
            'THU_ggH_qmtopUp',
            'THU_ggH_qmtopDown',
        ]
        self.eventDictionaryModifications = {
            'THU_ggH_MuUp':self.CreateMuUpDictionary,
            'THU_ggH_MuDown':self.CreateMuDownDictionary,
            'THU_ggH_ResUp':self.CreateResUpDictionary,
            'THU_ggH_ResDown':self.CreateResDownDictionary,
            'THU_ggH_Mig01Up':self.CreateMig01UpDictionary,
            'THU_ggH_Mig01Down':self.CreateMig01DownDictionary,
            'THU_ggH_Mig12Up':self.CreateMig12UpDictionary,
            'THU_ggH_Mig12Down':self.CreateMig12DownDictionary,
            'THU_ggH_VBF2jUp':self.CreateVBF2jUpDictionary,
            'THU_ggH_VBF2jDown':self.CreateVBF2jDownDictionary,
            'THU_ggH_VBF3jUp':self.CreateVBF3jUpDictionary,
            'THU_ggH_VBF3jDown':self.CreateVBF3jDownDictionary,
            'THU_ggH_PT60Up':self.CreatePT60UpDictinoary,
            'THU_ggH_PT60Down':self.CreatePT60DownDictionary,
            'THU_ggH_PT120Up':self.CreatePT120UpDictionary,
            'THU_ggH_PT120Down':self.CreatePT120DownDictionary,
            'THU_ggH_qmtopUp':self.CreateqmtopUpDictionary,
            'THU_ggH_qmtopDown':self.CreateqmtopDownDictionary,
        }
    def CreateMuUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Mu_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateMuDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Mu_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary
            
    def CreateResUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Res_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateResDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Res_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateMig01UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Mig01_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateMig01DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Mig01_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateMig12UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Mig12_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateMig12DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_Mig12_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateVBF2jUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_VBF2j_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateVBF2jDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_VBF2j_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateVBF3jUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_VBF3j_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateVBF3jDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_VBF3j_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreatePT60UpDictinoary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_PT60_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreatePT60DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_PT60_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreatePT120UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_PT120_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreatePT120DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_PT120_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateqmtopUpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_qmtop_UP
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary

    def CreateqmtopDownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        modifiedEventDictionary.Weight = theTree.FinalWeighting_ggHTheory_qmtop_DOWN
        if modifiedEventDictionary.Weight == 0:
            return nominalEventDictionary

        return modifiedEventDictionary
