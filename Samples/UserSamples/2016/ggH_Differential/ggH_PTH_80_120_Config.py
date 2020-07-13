from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_16 import JES16Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.ggHTheory import ggHTheoryUncertainty
from Samples.Uncertainties.UserUncertainties.MetRecoil import MetRecoilUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger16 import Trigger16Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'ggH_PTH_80_120_htt125'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
ggHSample.files = ['ggH.root']
ggHSample.definition = 'is_Fiducial == 1.0 && Rivet_higgsPt > 80 && Rivet_higgsPt < 120'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES16Uncertainty(),
    JERUncertainty(),
    ggHTheoryUncertainty(),
    MetRecoilUncertainty(),
    MuonESUncertainty(),
    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger16Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
