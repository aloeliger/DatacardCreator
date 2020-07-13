from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.VH_QCD_AcceptanceUncertainties.VH_scale_vbf_highmjj_lowpt_Uncertainty import VH_scale_vbf_highmjj_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

WHSample = Sample()
WHSample.name = "WH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125"
WHSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
WHSample.files = ['WHPlus.root','WHMinus.root']
WHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 210'
WHSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    VH_scale_vbf_highmjj_lowpt_Uncertainty(),
]
WHSample.eventDictionaryInstance = MuTauEventDictionary
WHSample.CreateEventWeight = WHSample.CreateEventWeight_Standard
