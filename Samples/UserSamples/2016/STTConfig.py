from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

STSample = Sample()
STSample.name = 'STT'
STSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
STSample.files = ['ST_t_top.root',
                  'ST_t_antitop.root',
                  'ST_tW_top.root',
                  'ST_tW_antitop.root']
STSample.definition = 'gen_match_2 == 5'
STSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger16Uncertainty(),
]
STSample.eventDictionaryInstance = MuTauEventDictionary
STSample.CreateEventWeight = STSample.CreateEventWeight_Standard
