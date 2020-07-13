from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty
from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
#from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

WHSample = Sample()
WHSample.name = "WH_lep_FWDH_htt125"
WHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
WHSample.files = ['WHPlus.root','WHMinus.root']
WHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 300'
WHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),
    MuonESUncertainty(),
#    PrefiringUncertainty(),
    TauIDUncertainty(),
    Trigger1718Uncertainty(),
]
WHSample.eventDictionaryInstance = MuTauEventDictionary
WHSample.CreateEventWeight = WHSample.CreateEventWeight_Standard
