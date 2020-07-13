from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty

from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.ggVH_QCD_AcceptanceUncertainties.ggZH_scale_1jet_lowpt_Uncertainty import ggZH_scale_1jet_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'ggZH_PTH_0_200_1J_PTH_0_60_htt125'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
ggHSample.files = ['GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root']
ggHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 104'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),

    MuonESUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    PrefiringUncertainty(),
    ggZH_scale_1jet_lowpt_Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
