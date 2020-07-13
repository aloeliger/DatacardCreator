from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

WHSample = Sample()
WHSample.name = "WH_LJPT_60_120_htt125"
WHSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
WHSample.files = ['WHPlus.root','WHMinus.root']
WHSample.definition = 'is_Fiducial == 1.0 && Rivet_nJets30 >= 1 && Rivet_j1pt >= 60 && Rivet_j2pt <= 120'
WHSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger16Uncertainty(),
]
WHSample.eventDictionaryInstance = MuTauEventDictionary
WHSample.CreateEventWeight = WHSample.CreateEventWeight_Standard
