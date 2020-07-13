from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty

from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.ggVH_QCD_AcceptanceUncertainties.ggZH_scale_2jet_lowpt_Uncertainty import ggZH_scale_2jet_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'ggZH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
ggHSample.files = ['GGZHLLTT.root','GGZHQQTT.root','GGZHNNTT.root']
ggHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 109'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),

    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    ggZH_scale_2jet_lowpt_Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
