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

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VBFSample = Sample()
VBFSample.name = 'qqH_MJJ_1000_1400_htt125'
VBFSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
VBFSample.files = ['VBF.root']
VBFSample.definition = 'is_Fiducial == 1.0 && Rivet_mjj >= 1000 && Rivet_mjj < 1400'
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
]
VBFSample.eventDictionaryInstance = MuTauEventDictionary
VBFSample.CreateEventWeight = VBFSample.CreateEventWeight_Standard
