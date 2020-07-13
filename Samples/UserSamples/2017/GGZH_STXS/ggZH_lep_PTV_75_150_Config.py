from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.ggVH_QCD_AcceptanceUncertainties.ggZH_scale_VH_lowpt_Uncertainty import ggZH_scale_VH_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ZHSample = Sample()
ZHSample.name = 'ggZH_lep_PTV_75_150_htt125'
ZHSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
#ZHSample.files = ['ZH.root','GGZHLLTT.root']
ZHSample.files = ['GGZHLLTT.root','GGZHNNTT.root']
ZHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 502'
ZHSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    ggZH_scale_VH_lowpt_Uncertainty(),
]
ZHSample.eventDictionaryInstance = MuTauEventDictionary
ZHSample.CreateEventWeight = ZHSample.CreateEventWeight_Standard
