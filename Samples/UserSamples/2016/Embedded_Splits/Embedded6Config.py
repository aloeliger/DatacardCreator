from Samples.SampleDefinition import Sample

# Uncertainties 
from Samples.Uncertainties.UserUncertainties.EmbeddedTES import EmbeddedTESUncertainty
from Samples.Uncertainties.UserUncertainties.TTbarContamination import TTbarContaminationUncertainty
from Samples.Uncertainties.UserUncertainties.EmbeddedTrigger16 import EmbeddedTrigger16Uncertainty
from Samples.Uncertainties.UserUncertainties.EmbeddedMuonES import EmbeddedMuonESUncertainty

# event definition
from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

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
EmbeddedSample.path  = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
EmbeddedSample.files = ['Embedded.root']
EmbeddedSample.definition = ''
EmbeddedSample.uncertainties = [
    EmbeddedTESUncertainty(),
    TTbarContaminationUncertainty(),
    EmbeddedTrigger16Uncertainty(),
    EmbeddedMuonESUncertainty(),
    ]
EmbeddedSample.eventDictionaryInstance = MuTauEventDictionary
EmbeddedSample.CreateEventWeight = EmbeddedSample.CreateEventWeight_Standard
EmbeddedSample.EndAction = PerformTTbarContaminationSubtraction
EmbeddedSample.startEntry = 2500000
EmbeddedSample.endEntry = 3000000
