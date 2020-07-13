from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ZHSample = Sample()
ZHSample.name = 'ZH_PTH_0_45_htt125'
ZHSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
ZHSample.files = ['ZH.root','GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root']
ZHSample.definition = 'is_Fiducial == 1.0 && Rivet_higgsPt >= 0 && Rivet_higgsPt < 45'
ZHSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger16Uncertainty(),
]
ZHSample.eventDictionaryInstance = MuTauEventDictionary
ZHSample.CreateEventWeight = ZHSample.CreateEventWeight_Standard
