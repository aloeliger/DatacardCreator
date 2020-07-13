from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty
from Samples.Uncertainties.UserUncertainties.qqHTheory import qqHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.qqH_QCD_AcceptanceUncertainties.qqH_scale_Inclusive_Uncertainty import qqH_scale_Inclusive_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VBFSample = Sample()
VBFSample.name = 'qqH_htt125'
VBFSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
VBFSample.files = ['VBF.root']
VBFSample.definition = ''
VBFSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),    
    Trigger16Uncertainty(),
    qqHTheoryUncertainty(),
    qqH_scale_Inclusive_Uncertainty(),    
]
VBFSample.eventDictionaryInstance = MuTauEventDictionary
VBFSample.CreateEventWeight = VBFSample.CreateEventWeight_Standard
