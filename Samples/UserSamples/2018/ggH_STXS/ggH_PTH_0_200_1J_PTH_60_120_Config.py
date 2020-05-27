from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.ggHTheory import ggHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
#from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.ggH_QCD_AcceptanceUncertainties.ggH_scale_1jet_lowpt_Uncertainty import ggH_scale_ggH_1jet_lowpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'ggH_PTH_0_200_1J_PTH_60_120_htt125'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
ggHSample.files = ['ggH.root']
ggHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 105'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    ggHTheoryUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    #PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    ggH_scale_ggH_1jet_lowpt_Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
