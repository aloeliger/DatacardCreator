from Samples.Uncertainties.UncertaintyDef import Uncertainty
import ROOT

def getWminusH_NJETS_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets4UP
    except:
        return theWeight
    return theWeight

def getWplusH_NJETS_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets4UP
    except:
        return theWeight
    return theWeight

def getZH_NJETS_UpWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets0UP
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets1UP
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets2UP
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets3UP
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets4UP
    except:
        return theWeight
    return theWeight

def getWminusH_NJETS_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WminusH_njets4DOWN
    except:
        return theWeight
    return theWeight

def getWplusH_NJETS_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_WplusH_njets4DOWN
    except:
        return theWeight
    return theWeight

def getZH_NJETS_DownWeight(theTree):
    theWeight = 0
    try:
        if theTree.Rivet_nJets30 == 0:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets0DOWN
        elif theTree.Rivet_nJets30 == 1:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets1DOWN
        elif theTree.Rivet_nJets30 == 2:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets2DOWN
        elif theTree.Rivet_nJets30 == 3:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets3DOWN
        elif theTree.Rivet_nJets30 >= 4:
            theWeight = theTree.FinalWeighting_QCDScaleAcceptance_Differential_ZH_njets4DOWN
    except:
        return theWeight
    return theWeight


class VH_NJets_Differential_QCDScale_Uncertainty(Uncertainty):
    def __init__(self):
        self.name = 'VH_NJets_Differential_QCDScale'
        self.uncertaintyNames = [
            'QCDscale_VHUp',
            'QCDscale_VHDown',
        ]
        self.eventDictionaryModifications ={
            'QCDscale_VHUp':self.CreateQCDScaleVHDictionaryUp,
            'QCDscale_VHDown':self.CreateQCDScaleVHDictionaryDown,
        }
    def CreateQCDScaleVHDictionaryUp(self,theTree,nominalEventDictionary):
        WminusHWeight = getWminusH_NJETS_UpWeight(theTree)
        WplusHWeight = getWplusH_NJETS_UpWeight(theTree)
        ZHWeight = getZH_NJETS_UpWeight(theTree)

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
        WminusHWeight = getWminusH_NJETS_DownWeight(theTree)
        WplusHWeight = getWplusH_NJETS_DownWeight(theTree)
        ZHWeight = getZH_NJETS_DownWeight(theTree)

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

