from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.ggHTheory_Differential_J1PT_Normalized import ggHTheory_Differential_J1PT_Normalized_Uncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.J1PT_QCD_Uncertainties.ggH_J1PT_Differential_QCDScale_Uncertainty import ggH_J1PT_Differential_QCDScale_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'ggH_recoJ1PT_30_60'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
ggHSample.files = ['ggH.root']
ggHSample.definition = 'is_Fiducial == 1.0 && jpt_1 >= 30.0 && jpt_1 <= 60.0'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    ggHTheory_Differential_J1PT_Normalized_Uncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    ggH_J1PT_Differential_QCDScale_Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
