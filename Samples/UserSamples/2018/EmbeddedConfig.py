from Samples.SampleDefinition import Sample

# Uncertainties 
from Samples.Uncertainties.UserUncertainties.EmbeddedTES import EmbeddedTESUncertainty
from Samples.Uncertainties.UserUncertainties.TTbarContamination import TTbarContaminationUncertainty
from Samples.Uncertainties.UserUncertainties.EmbeddedTrigger17_18 import EmbeddedTrigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.EmbeddedMuonES import EmbeddedMuonESUncertainty
from Samples.Uncertainties.UserUncertainties.EmbeddedTauID import EmbeddedTauIDUncertainty
from Samples.Uncertainties.UserUncertainties.EmbeddedTrackingUncertainty import EmbeddedTrackingUncertainty

from Samples.Uncertainties.UserUncertainties.EmbeddedZeroJetUncertainty import EmbeddedZeroJetUncertainty

# event definition
from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

#just something to check the embedded normalizationa nd whether that is causing us problems
def CreateEventWeight_Standard_Reduced(theEventDictionary,theTree):
    theEventDictionary.Weight = theTree.FinalWeighting * 0.95

#subtraction and final histogram creation
def PerformTTbarContaminationSubtraction(theOutputHistograms,analysisCategory):    
    EmbeddedHistogram = theOutputHistograms[analysisCategory.name]["embedded_CMS_htt_emb_ttbar"]
    TTContaminationHistogram = theOutputHistograms[analysisCategory.name]["TTContamination_CMS_htt_emb_ttbar"]
    EmbeddedHistogram_Up = EmbeddedHistogram.Clone()
    EmbeddedHistogram_Up.SetNameTitle("embedded_CMS_htt_emb_ttbarUp","embedded_CMS_htt_emb_ttbarUp")
    EmbeddedHistogram_Up.Add(TTContaminationHistogram,0.1)
    EmbeddedHistogram_Down = EmbeddedHistogram.Clone()
    EmbeddedHistogram_Down.SetNameTitle("embedded_CMS_htt_emb_ttbarDown","embedded_CMS_htt_emb_ttbarDown")
    EmbeddedHistogram_Down.Add(TTContaminationHistogram,-0.1)
    theOutputHistograms[analysisCategory.name]["embedded_CMS_htt_emb_ttbarUp"] = EmbeddedHistogram_Up
    theOutputHistograms[analysisCategory.name]["embedded_CMS_htt_emb_ttbarDown"] = EmbeddedHistogram_Down

EmbeddedSample = Sample()
EmbeddedSample.name = 'embedded'
EmbeddedSample.path  = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
EmbeddedSample.files = ['Embedded.root']
EmbeddedSample.definition = ''
EmbeddedSample.uncertainties = [
    EmbeddedTESUncertainty(),
    TTbarContaminationUncertainty(),
    EmbeddedTrigger1718Uncertainty(),
    EmbeddedMuonESUncertainty(),
    EmbeddedTauIDUncertainty(),
    EmbeddedTrackingUncertainty(),
    EmbeddedZeroJetUncertainty(),
    ]
EmbeddedSample.eventDictionaryInstance = MuTauEventDictionary
EmbeddedSample.CreateEventWeight = EmbeddedSample.CreateEventWeight_Standard
#EmbeddedSample.CreateEventWeight = CreateEventWeight_Standard_Reduced
EmbeddedSample.EndAction = PerformTTbarContaminationSubtraction
