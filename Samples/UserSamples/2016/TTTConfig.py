from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TTbarShape import TTbarShape
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

TTLSample = Sample()
TTLSample.name = 'TTT'
TTLSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
TTLSample.files = ['TT.root']
TTLSample.definition = '(gen_match_1 == 1 || gen_match_1 == 2) && gen_match_2 == 5'
TTLSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    TTbarShape(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger16Uncertainty(),
]
TTLSample.eventDictionaryInstance = MuTauEventDictionary
TTLSample.CreateEventWeight = TTLSample.CreateEventWeight_Standard
