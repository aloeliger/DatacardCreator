from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class ggHTheory_Differential_J1PT_Normalized_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'ggHTheory_Differential_J1PT_Normalized_Uncertainty'
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
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Mu_j1pt_UP*(1.0+theTree.THU_ggH_Mu_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMuDownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Mu_j1pt_DOWN*(1.0-theTree.THU_ggH_Mu_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateResUpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Res_j1pt_UP*(1.0+theTree.THU_ggH_Res_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateResDownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Res_j1pt_DOWN*(1.0-theTree.THU_ggH_Res_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMig01UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Mig01_j1pt_UP*(1.0+theTree.THU_ggH_Mig01_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMig01DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Mig01_j1pt_DOWN*(1.0-theTree.THU_ggH_Mig01_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMig12UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Mig12_j1pt_UP*(1.0+theTree.THU_ggH_Mig12_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateMig12DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_Mig12_j1pt_DOWN*(1.0-theTree.THU_ggH_Mig12_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateVBF2jUpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_VBF2j_j1pt_UP*(1.0+theTree.THU_ggH_VBF2j_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateVBF2jDownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_VBF2j_j1pt_DOWN*(1.0-theTree.THU_ggH_VBF2j_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateVBF3jUpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_VBF3j_j1pt_UP*(1.0+theTree.THU_ggH_VBF3j_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateVBF3jDownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_VBF3j_j1pt_DOWN*(1.0-theTree.THU_ggH_VBF3j_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePT60UpDictinoary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_PT60_j1pt_UP*(1.0+theTree.THU_ggH_PT60_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePT60DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_PT60_j1pt_DOWN*(1.0-theTree.THU_ggH_PT60_13TeV))

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePT120UpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_PT120_j1pt_UP*(1.0+theTree.THU_ggH_PT120_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreatePT120DownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_PT120_j1pt_DOWN*(1.0-theTree.THU_ggH_PT120_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateqmtopUpDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_qmtop_j1pt_UP*(1.0+theTree.THU_ggH_qmtop_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary

    def CreateqmtopDownDictionary(self,theTree,nominalEventDictionary):
        try:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            modifiedEventDictionary.Weight = (theTree.FinalWeighting_ggHTheoryNormalization_qmtop_j1pt_DOWN*(1.0-theTree.THU_ggH_qmtop_13TeV))
            if modifiedEventDictionary.Weight == 0:
                return nominalEventDictionary

            return modifiedEventDictionary
        except:
            return nominalEventDictionary
