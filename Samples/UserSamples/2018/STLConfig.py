from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.eTauFakeRate import eTauFakeRateUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

STSample = Sample()
STSample.name = 'STL'
STSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
STSample.files = ['ST_t_top.root',
                  'ST_t_antitop.root',
                  'ST_tW_top.root',
                  'ST_tW_antitop.root']
STSample.definition = 'gen_match_2 < 5'
STSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    Trigger1718Uncertainty(),
    eTauFakeRateUncertainty(),
]
STSample.eventDictionaryInstance = MuTauEventDictionary
STSample.CreateEventWeight = STSample.CreateEventWeight_Standard
