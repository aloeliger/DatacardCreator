from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

def getWminusH_J1PT_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_30_60UP
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_60_120UP
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_120_200UP
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_200_350UP
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_gt350UP
    except:
        return theWeight
    return theWeight

def getWplusH_J1PT_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_30_60UP
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_60_120UP
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_120_200UP
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_200_350UP
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_gt350UP
    except:
        return theWeight
    return theWeight

def getZH_J1PT_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_30_60UP
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_60_120UP
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_120_200UP
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_200_350UP
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_gt350UP
    except:
        return theWeight
    return theWeight

def getWminusH_J1PT_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_30_60DOWN
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_60_120DOWN
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_120_200DOWN
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_200_350DOWN
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_j1pt_gt350DOWN
    except:
        return theWeight
    return theWeight

def getWplusH_J1PT_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_30_60DOWN
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_60_120DOWN
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_120_200DOWN
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_200_350DOWN
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_j1pt_gt350DOWN
    except:
        return theWeight
    return theWeight

def getZH_J1PT_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_j1pt > 30 and theTree.Rivet_j1pt <= 60:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_30_60DOWN
        elif theTree.Rivet_j1pt > 60 and theTree.Rivet_j1pt <= 120:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_60_120DOWN
        elif theTree.Rivet_j1pt > 120 and theTree.Rivet_j1pt <= 200:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_120_200DOWN
        elif theTree.Rivet_j1pt > 200 and theTree.Rivet_j1pt <= 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_200_350DOWN
        elif theTree.Rivet_j1pt > 350:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_j1pt_gt350DOWN
    except:
        return theWeight
    return theWeight


class VH_J1PT_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_J1PT_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_VHUp',
            'QCDscale_VHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_VHUp':self.CreateQCDScaleVHDictionaryUp,
            'QCDscale_VHDown':self.CreateQCDScaleVHDictionaryDown,
        }
    def CreateQCDScaleVHDictionaryUp(self,theTree,nominalEventDictionary):
        WminusHWeight = getWminusH_J1PT_UpWeight(theTree)
        WplusHWeight = getWplusH_J1PT_UpWeight(theTree)
        ZHWeight = getZH_J1PT_UpWeight(theTree)

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
        WminusHWeight = getWminusH_J1PT_DownWeight(theTree)
        WplusHWeight = getWplusH_J1PT_DownWeight(theTree)
        ZHWeight = getZH_J1PT_DownWeight(theTree)

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
