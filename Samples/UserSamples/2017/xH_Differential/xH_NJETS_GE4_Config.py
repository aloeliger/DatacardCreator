from Samples.SampleDefinition import Sample
from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_17 import JES17Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
#from Samples.Uncertainties.UserUncertainties.qqHTheory import qqHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.NJets_QCD_Uncertainties.GGZH_NJets_Differential_QCDScale_Uncertainty import GGZH_NJets_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.NJets_QCD_Uncertainties.VH_NJets_Differential_QCDScale_Uncertainty import VH_NJets_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.NJets_QCD_Uncertainties.qqH_NJets_Differential_QCDScale_Uncertainty import qqH_NJets_Differential_QCDScale_Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.DifferentialUncertainties.NJets_QCD_Uncertainties.ttH_NJets_Differential_QCDScale_Uncertainty import ttH_NJets_Differential_QCDScale_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VBFSample = Sample()
VBFSample.name = 'xH_NJ_GE4'
VBFSample.path = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
VBFSample.files = ['VBF.root','WHPlus.root','WHMinus.root','ZH.root','GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root','ttH.root']
VBFSample.definition = 'is_Fiducial == 1.0 && Rivet_nJets30 >= 4'
VBFSample.uncertainties = [
    TESUncertainty(),
    JES17Uncertainty(),
    JERUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),    
    Trigger1718Uncertainty(),
    #qqHTheoryUncertainty(),
    GGZH_NJets_Differential_QCDScale_Uncertainty(),
    VH_NJets_Differential_QCDScale_Uncertainty(),
    qqH_NJets_Differential_QCDScale_Uncertainty(),
    ttH_NJets_Differential_QCDScale_Uncertainty(),
]
VBFSample.eventDictionaryInstance = MuTauEventDictionary
VBFSample.CreateEventWeight = VBFSample.CreateEventWeight_Standard
