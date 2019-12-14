from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.METUES import METUESUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VVSample = Sample()
VVSample.name = 'VVL'
VVSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
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
    JES18Uncertainty(),
    JERUncertainty(),
    METUESUncertainty(),
    MuonESUncertainty(),
    Trigger1718Uncertainty(),
]
VVSample.eventDictionaryInstance = MuTauEventDictionary
VVSample.CreateEventWeight = VVSample.CreateEventWeight_Standard
