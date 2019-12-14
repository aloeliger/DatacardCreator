from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.ZPT import ZPTUncertainty
from Samples.Uncertainties.UserUncertainties.ZLShape import ZLShapeUncertainty
from Samples.Uncertainties.UserUncertainties.JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

DYLSample = Sample()
DYLSample.name = 'ZL'
DYLSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
DYLSample.files = ['DY.root','EWKZLL.root','EWKZNuNu.root']
DYLSample.definition = 'gen_match_2 < 5'
DYLSample.uncertainties = [
    TESUncertainty(),
    ZPTUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    ZLShapeUncertainty(),
    PrefiringUncertainty(),
    Trigger1718Uncertainty(),
]
DYLSample.eventDictionaryInstance = MuTauEventDictionary
DYLSample.CreateEventWeight = DYLSample.CreateEventWeight_Standard
