from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

WHSample = Sample()
WHSample.name = "WH_PTH_80_120_htt125"
WHSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
WHSample.files = ['WHPlus.root','WHMinus.root']
WHSample.definition = 'is_Fiducial == 1.0 && Rivet_higgsPt > 80.0 && Rivet_higgsPt < 120.0'
WHSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
WHSample.eventDictionaryInstance = MuTauEventDictionary
WHSample.CreateEventWeight = WHSample.CreateEventWeight_Standard
