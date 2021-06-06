#Higgs pt uncertainty

from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

class HiggsPtUncertainty(Uncertainty):
    def __init__(self):
        self.name = 'HiggsPt'
        self.uncertaintyNames = [
            'CMS_HiggsPt_0_45Up',
            'CMS_HiggsPt_0_45Down',
            'CMS_HiggsPt_45_80Up',
            'CMS_HiggsPt_45_80Down',
            'CMS_HiggsPt_80_120Up',
            'CMS_HiggsPt_80_120Down',
            'CMS_HiggsPt_120_200Up',
            'CMS_HiggsPt_120_200Down',
            'CMS_HiggsPt_200_350Up',
            'CMS_HiggsPt_200_350Down',
            'CMS_HiggsPt_350_450Up',
            'CMS_HiggsPt_350_450Down',
            'CMS_HiggsPt_gt450Up',
            'CMS_HiggsPt_gt450Down',
        ]
        self.eventDictionaryModifications = {
            'CMS_HiggsPt_0_45Up':self.CreateHiggsPt0To45UpDictionary,
            'CMS_HiggsPt_0_45Down':self.CreateHiggsPt0To45DownDictionary,
            'CMS_HiggsPt_45_80Up':self.CreateHiggsPt45To80UpDictionary,
            'CMS_HiggsPt_45_80Down':self.CreateHiggsPt45To80DownDictionary,
            'CMS_HiggsPt_80_120Up':self.CreateHiggsPt80To120UpDictionary,
            'CMS_HiggsPt_80_120Down':self.CreateHiggsPt80To120DownDictionary,
            'CMS_HiggsPt_120_200Up':self.CreateHiggsPt120To200UpDictionary,
            'CMS_HiggsPt_120_200Down':self.CreateHiggsPt120To200DownDictionary,
            'CMS_HiggsPt_200_350Up':self.CreateHiggsPt200To350UpDictionary,
            'CMS_HiggsPt_200_350Down':self.CreateHiggsPt200To350DownDictionary,
            'CMS_HiggsPt_350_450Up':self.CreateHiggsPt350To450UpDictionary,
            'CMS_HiggsPt_350_450Down':self.CreateHiggsPt350To450DownDictionary,
            'CMS_HiggsPt_gt450Up':self.CreateHiggsPtGT450UpDictionary,
            'CMS_HiggsPt_gt450Down':self.CreateHiggsPtGT450DownDictionary,
        }

    def CreateHiggsPt0To45UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 0 and theModifiedHiggsPt < 45:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt0To45DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        
        if theModifiedHiggsPt > 0 and theModifiedHiggsPt < 45:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt45To80UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 45 and theModifiedHiggsPt < 80:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt45To80DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        
        if theModifiedHiggsPt > 45 and theModifiedHiggsPt < 80:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt80To120UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 80 and theModifiedHiggsPt < 120:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt80To120DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        
        if theModifiedHiggsPt > 80 and theModifiedHiggsPt < 120:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt120To200UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 120 and theModifiedHiggsPt < 200:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt120To200DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        
        if theModifiedHiggsPt > 120 and theModifiedHiggsPt < 200:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt200To350UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 200 and theModifiedHiggsPt < 350:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt200To350DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        
        if theModifiedHiggsPt > 200 and theModifiedHiggsPt < 350:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt350To450UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 350 and theModifiedHiggsPt < 450:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPt350To450DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        
        if theModifiedHiggsPt > 350 and theModifiedHiggsPt < 450:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPtGT450UpDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        theHiggsPtCorrection = (theModifiedHiggsPt/theHiggsPt) - 1.0
        theNewCorrection = max(1.0 + (2.0 * theHiggsPtCorrection), 0.0)

        if theModifiedHiggsPt > 450:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt * theNewCorrection
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary

    def CreateHiggsPtGT450DownDictionary(self,theTree,nominalEventDictionary):
        modifiedEventDictionary = nominalEventDictionary.Clone()
        theModifiedHiggsPt = modifiedEventDictionary.constructedQuantities['differentialHiggsPt']
        theHiggsPt = modifiedEventDictionary.constructedQuantities['HiggsPt']
        
        if theModifiedHiggsPt > 450:
            modifiedEventDictionary.constructedQuantities['differentialHiggsPt'] = theHiggsPt
        
        modifiedEventDictionary.CompileCompleteDictionary()
        return modifiedEventDictionary
