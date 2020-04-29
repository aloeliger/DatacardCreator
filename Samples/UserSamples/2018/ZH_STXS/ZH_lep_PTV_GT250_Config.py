from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ZHSample = Sample()
ZHSample.name = 'ZH_lep_PTV_GT250_htt125'
ZHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
#ZHSample.files = ['ZH.root','GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root']
ZHSample.files = ['ZH.root']
ZHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 405'
ZHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
ZHSample.eventDictionaryInstance = MuTauEventDictionary
ZHSample.CreateEventWeight = ZHSample.CreateEventWeight_Standard
