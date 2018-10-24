"""
CMSSW Cfg Template to be submitted with crab
"""
import FWCore.ParameterSet.Config as cms
process = cms.Process("NtupleMaking")

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

thisIsData = s.isData
globalTag = s.globaltag
# globalTag = '94X_dataRun2_ReReco_EOY17_v6'

if not thisIsData:
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_MC")
else:
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_Data")

#
#
#

# JET ENERGY CORRECTIONS

from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

if thisIsData:
    corrections = cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'])
else:
    corrections = cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])

updateJetCollection(
    process,
    jetSource=cms.InputTag('slimmedJets'),
    labelName='UpdatedJEC',
    # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
    jetCorrections=('AK4PFchs', corrections, 'None')
)

# EE noise mitigation fix SEE https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_for_2

from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

runMetCorAndUncFromMiniAOD(
    process,
    isData=thisIsData,  # false for MC
    reclusterJets = True,
    CHS = True,
    fixEE2017=True,
    fixEE2017Params={'userawPt': True, 'PtThreshold': 50.0,
                     'MinEtaThreshold': 2.65, 'MaxEtaThreshold': 3.139},
    postfix="ModifiedMET"
)

# electron energy scale correction fix SEE https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
                       runVID=False,  # saves CPU time by not needlessly re-running VID
                       era='2017-Nov17ReReco')


# #
# #  Electron ID Setup - cut based
# #
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
dataFormat = DataFormat.MiniAOD
switchOnVIDElectronIdProducer(process, dataFormat)
my_id_modules = [
    'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V1_cff'
]
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process, idmod, setupVIDElectronSelection)

#
#
#
process.GlobalTag.globaltag = globalTag
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring())
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.TFileService = cms.Service("TFileService", fileName = cms.string("ntuple.root") )
process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC)
process.p = cms.Path(process.egammaPostRecoSeq * process.egmGsfElectronIDSequence *
                     process.jecSequence * process.fullPatMetSequenceModifiedMET * 
                     process.ntuplemaker_H2DiMuonMaker)