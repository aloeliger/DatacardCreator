from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

def getWminusH_PTH_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_gt450UP
    except:
        return theWeight
    return theWeight

def getWminusH_PTH_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_pth_gt450DOWN
    except:
        return theWeight
    return theWeight

def getWplusH_PTH_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_gt450UP
    except:
        return theWeight
    return theWeight

def getWplusH_PTH_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_pth_gt450DOWN
    except:
        return theWeight
    return theWeight

def getZH_PTH_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_0_45UP
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_45_80UP
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_80_120UP
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_120_200UP
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_200_350UP
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_350_450UP
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_gt450UP
    except:
        return theWeight
    return theWeight

def getZH_PTH_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt <= 45:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_0_45DOWN
        elif theTree.Rivet_higgsPt > 45 and theTree.Rivet_higgsPt <= 80:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_45_80DOWN
        elif theTree.Rivet_higgsPt > 80 and theTree.Rivet_higgsPt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_80_120DOWN
        elif theTree.Rivet_higgsPt > 120 and theTree.Rivet_higgsPt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_120_200DOWN
        elif theTree.Rivet_higgsPt > 200 and theTree.Rivet_higgsPt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_200_350DOWN
        elif theTree.Rivet_higgsPt > 350 and theTree.Rivet_higgsPt <= 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_350_450DOWN
        elif theTree.Rivet_higgsPt > 450:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_pth_gt450DOWN
    except:
        return theWeight
    return theWeight


class VH_PTH_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_PTH_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_VHUp',
            'QCDscale_VHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_VHUp':self.CreateQCDScaleVHDictionaryUp,
            'QCDscale_VHDown':self.CreateQCDScaleVHDictionaryDown,
        }
    def CreateQCDScaleVHDictionaryUp(self,theTree,nominalEventDictionary):
        WminusHWeight = getWminusH_PTH_UpWeight(theTree)
        WplusHWeight = getWplusH_PTH_UpWeight(theTree)
        ZHWeight = getZH_PTH_UpWeight(theTree)

        if WminusHWeight == 0 and WplusHWeight == 0 and ZHWeight == 0:
            return nominalEventDictionary
        else:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            if WminusHWeight != 0:
                modifiedEventDictionary.Weight = WminusHWeight
            elif WplusHWeight != 0:
                modifiedEventDictionary.Weight = WplusHWeight
            elif ZHWeight != 0:
                modifiedEventDictionary.Weight = ZHWeight
            return modifiedEventDictionary

    def CreateQCDScaleVHDictionaryDown(self,theTree,nominalEventDictionary):
        WminusHWeight = getWminusH_PTH_DownWeight(theTree)
        WplusHWeight = getWplusH_PTH_DownWeight(theTree)
        ZHWeight = getZH_PTH_DownWeight(theTree)

        if WminusHWeight == 0 and WplusHWeight == 0 and ZHWeight == 0:
            return nominalEventDictionary
        else:
            modifiedEventDictionary = nominalEventDictionary.Clone()
            if WminusHWeight != 0:
                modifiedEventDictionary.Weight = WminusHWeight
            elif WplusHWeight != 0:
                modifiedEventDictionary.Weight = WplusHWeight
            elif ZHWeight != 0:
                modifiedEventDictionary.Weight = ZHWeight
            return modifiedEventDictionary


