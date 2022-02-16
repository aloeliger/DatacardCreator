from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
#from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.ggVH_QCD_AcceptanceUncertainties.ggZH_scale_VH_lowpt_Uncertainty import ggZH_scale_VH_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ZHSample = Sample()
ZHSample.name = 'ggZH_lep_PTV_150_250_0J_hww125'
ZHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
ZHSample.files = ['GGZHWW.root']
#ZHSample.files = ['ZH.root','GGZHLLTT.root']
#ZHSample.files = ['GGZHLLTT.root','GGZHNNTT.root']
ZHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 503'
ZHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),

    TauIDUncertainty(),
    Trigger1718Uncertainty(),
#    ggZH_scale_VH_lowpt_Uncertainty(),
]
ZHSample.eventDictionaryInstance = MuTauEventDictionary
ZHSample.CreateEventWeight = ZHSample.CreateEventWeight_Standard
