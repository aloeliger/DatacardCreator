from Samples.SampleDefinition import Sample

#
from Samples.Uncertainties.UserUncertainties.TTbarContamination import TTbarContaminationUncertainty

from Samples.EventDefinition.UserEventDictionaries.MuTauEventDictionary import MuTauEventDictionary

TTContamination = Sample()
TTContamination.name = 'TTContamination'
TTContamination.path = '/data/aloeliger/SMHTT_Selected_2018_TTContamination/'
TTContamination.files = ['TTTo2L2Nu.root','TTToHadronic.root','TTToSemiLeptonic.root']
TTContamination.definition = ''
TTContamination.uncertainties = [
    TTbarContaminationUncertainty()
    ]
TTContamination.eventDictionaryInstance = MuTauEventDictionary
TTContamination.CreateEventWeight = TTContamination.CreateEventWeight_Standard
TTContamination.startEntry = 96000
TTContamination.endEntry =  120000
