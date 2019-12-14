from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VVSample = Sample()
VVSample.name = 'VVL'
VVSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
VVSample.files = [#'WW1L1Nu2Q.root',
                  #'WZ1L1Nu2Q.root',
                  #'WZ1L3Nu.root',
                  'WZ3L1Nu.root',
                  'WZ2L2Q.root',
                  'ZZ4L.root',
                  'ZZ2L2Q.root',
                  'VV2L2Nu.root']
VVSample.definition = 'gen_match_2 < 5'
VVSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    Trigger16Uncertainty(),
]
VVSample.eventDictionaryInstance = MuTauEventDictionary
VVSample.CreateEventWeight = VVSample.CreateEventWeight_Standard
