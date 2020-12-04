from Samples.SampleDefinition import Sample
from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty
#from Samples.Uncertainties.UserUncertainties.qqHTheory import qqHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.GGZH_PTH_Differential_QCDScale_Uncertainty import GGZH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.VH_PTH_Differential_QCDScale_Uncertainty import VH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.qqH_PTH_Differential_QCDScale_Uncertainty import qqH_PTH_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.PTH_QCD_Uncertainties.ttH_PTH_Differential_QCDScale_Uncertainty import ttH_PTH_Differential_QCDScale_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VBFSample = Sample()
VBFSample.name = 'xH_PTH_45_80'
VBFSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
VBFSample.files = ['VBF.root','WHPlus.root','WHMinus.root','ZH.root','GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root','ttH.root']
VBFSample.definition = 'is_Fiducial == 1.0 && Rivet_higgsPt >= 45 && Rivet_higgsPt < 80'
VBFSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),    
    Trigger16Uncertainty(),
    #qqHTheoryUncertainty(),
    GGZH_PTH_Differential_QCDScale_Uncertainty(),
    VH_PTH_Differential_QCDScale_Uncertainty(),
    qqH_PTH_Differential_QCDScale_Uncertainty(),
    ttH_PTH_Differential_QCDScale_Uncertainty(),
]
VBFSample.eventDictionaryInstance = MuTauEventDictionary
VBFSample.CreateEventWeight = VBFSample.CreateEventWeight_Standard
