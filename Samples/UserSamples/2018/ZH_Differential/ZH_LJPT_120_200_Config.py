from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ZHSample = Sample()
ZHSample.name = 'ZH_LJPT_120_200_htt125'
ZHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
ZHSample.files = ['ZH.root','GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root']
ZHSample.definition = 'is_Fiducial == 1.0 && Rivet_nJets30 >= 1 && Rivet_j1pt >= 120.0 && Rivet_j1pt <= 200.0'
ZHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
ZHSample.eventDictionaryInstance = MuTauEventDictionary
ZHSample.CreateEventWeight = ZHSample.CreateEventWeight_Standard
