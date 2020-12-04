from Samples.SampleDefinition import Sample
from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
#from Samples.Uncertainties.UserUncertainties.ggHTheory import ggHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.GGZH_PTH_Differential_QCDScale_Uncertainty import GGZH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.VH_PTH_Differential_QCDScale_Uncertainty import VH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.ggH_PTH_Differential_QCDScale_Uncertainty import ggH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.qqH_PTH_Differential_QCDScale_Uncertainty import qqH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.ttH_PTH_Differential_QCDScale_Uncertainty import ttH_PTH_Differential_QCDScale_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'OutsideAcceptance'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
ggHSample.files = ['ggH.root',
                   'VBF.root',
                   'WHPlus.root',
                   'WHMinus.root',
                   'ZH.root',
                   'GGZHLLTT.root',
                   'GGZHNNTT.root',
                   'GGZHQQTT.root',
                   'ttH.root',
                   'GGHWW.root',
                   'VBFHWW.root',
                   'WplusHWW.root',
                   'WminusHWW.root',
                   'ZHWW.root',
                   'GGZHWW.root']
#ggHSample.files = ['WHPlus.root']
ggHSample.definition = 'is_Fiducial == 0.0'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    #ggHTheoryUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    GGZH_PTH_Differential_QCDScale_Uncertainty(),
    VH_PTH_Differential_QCDScale_Uncertainty(),
    qqH_PTH_Differential_QCDScale_Uncertainty(),
    ttH_PTH_Differential_QCDScale_Uncertainty(),
    ggH_PTH_Differential_QCDScale_Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
