from Samples.SampleDefinition import Sample

from Samples.Uncertainties.UserUncertainties.TES import TESUncertainty
from Samples.Uncertainties.UserUncertainties.Signal_JES_18 import JES18Uncertainty
from Samples.Uncertainties.UserUncertainties.JER import JERUncertainty


from Samples.Uncertainties.UserUncertainties.MuonES import MuonESUncertainty
#from Samples.Uncertainties.UserUncertainties.Prefiring import PrefiringUncertainty
from Samples.Uncertainties.UserUncertainties.TauID import TauIDUncertainty
from Samples.Uncertainties.UserUncertainties.Trigger17_18 import Trigger1718Uncertainty
from Samples.Uncertainties.UserUncertainties.QCDAcceptanceUncertainties.ggVH_QCD_AcceptanceUncertainties.ggZH_scale_very_highpt_Uncertainty import ggZH_scale_very_highpt_Uncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

ggHSample = Sample()
ggHSample.name = 'ggZH_PTH_GE650_htt125'
ggHSample.path = '/data/aloeliger/SMHTT_Selected_2018_Deep/'
ggHSample.files = ['GGZHLLTT.root','GGZHNNTT.root','GGZHQQTT.root']
ggHSample.definition = 'Rivet_stage1_1_cat_pTjet30GeV == 101 && Rivet_higgsPt > 650'
ggHSample.uncertainties = [
    TESUncertainty(),
    JES18Uncertainty(),
    JERUncertainty(),

    MuonESUncertainty(),

    TauIDUncertainty(),
    Trigger1718Uncertainty(),
    ggZH_scale_very_highpt_Uncertainty(),
]
ggHSample.eventDictionaryInstance = MuTauEventDictionary
ggHSample.CreateEventWeight = ggHSample.CreateEventWeight_Standard
