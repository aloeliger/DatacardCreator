from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.qqHTheory import qqHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

VBFSample = Sample()
VBFSample.name = 'qqH_hww125'
VBFSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
VBFSample.files = ['VBFHWW.root']
VBFSample.definition = ''
VBFSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    qqHTheoryUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
VBFSample.eventDictionaryInstance = MuTauEventDictionary
VBFSample.CreateEventWeight = VBFSample.CreateEventWeight_Standard
