from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TTbarShape import TTbarShape
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.eTauFakeRate import eTauFakeRateUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

TTLSample = Sample()
TTLSample.name = 'TTL'
TTLSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
TTLSample.files = ['TTTo2L2Nu.root','TTToHadronic.root','TTToSemiLeptonic.root']
TTLSample.definition = 'gen_match_2 < 5'
TTLSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    TTbarShape(),
    PrefiringUncertainty(),
    Trigger1718Uncertainty(),
    eTauFakeRateUncertainty(),
]
TTLSample.eventDictionaryInstance = MuTauEventDictionary
TTLSample.CreateEventWeight = TTLSample.CreateEventWeight_Standard
