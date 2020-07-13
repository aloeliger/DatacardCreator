from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.qqHTheory import qqHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
#from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.qqH_QCD_AcceptanceUncertainties.qqH_scale_highmjj_lowpt_Uncertainty import qqH_scale_highmjj_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VBFSample = Sample()
VBFSample.name = 'qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125'
VBFSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
VBFSample.files = ['VBF.root']
VBFSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 210'
VBFSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    qqHTheoryUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
#   PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    qqH_scale_highmjj_lowpt_Uncertainty(),
]
VBFSample.eventDictionaryInstance = MuTauEventDictionary
VBFSample.CreateEventWeight = VBFSample.CreateEventWeight_Standard
