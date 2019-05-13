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

year = s.year
thisIsData = s.isData
globalTag = s.globaltag

if not thisIsData:
    if year == "2016":
        process.load("HMuMu.NtupleMaking.H2DiMuonMaker_94X16MC")
    elif year == "2017":
        process.load("HMuMu.NtupleMaking.H2DiMuonMaker_94X17MC")
    elif year == "2018":
        process.load("HMuMu.NtupleMaking.H2DiMuonMaker_102X18MC")
else:
    if year == "2016":
        process.load("HMuMu.NtupleMaking.H2DiMuonMaker_94X16Data")
    elif year == "2017":
        process.load("HMuMu.NtupleMaking.H2DiMuonMaker_94X17Data")
    elif year == "2018":
        process.load("HMuMu.NtupleMaking.H2DiMuonMaker_102X18Data")

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


## only for 2017? check this

if year == "2017":

    # EE noise mitigation fix SEE https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_for_2

    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

    runMetCorAndUncFromMiniAOD(
        process,
        isData=thisIsData,  # false for MC
        fixEE2017=True,
        fixEE2017Params={'userawPt': True, 'ptThreshold': 50.0,
                        'minEtaThreshold': 2.65, 'maxEtaThreshold': 3.139},
        postfix="ModifiedMET"
    )


## era based on year 2016/2017/2018

from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq

if year == "2016":
    print("running on 2016")
    egammaEra = '2016-Legacy'
    prefire_era = "2016BtoH"
    setupEgammaPostRecoSeq(process,
                       runEnergyCorrections=False,
                       era=egammaEra)

if year == "2017":
    print("running on 2017")
    egammaEra = '2017-Nov17ReReco'
    prefire_era = "2017BtoF"
    setupEgammaPostRecoSeq(process,
                       runVID=False,  # saves CPU time by not needlessly re-running VID
                       era=egammaEra)
   
if year == "2018":
    print("running on 2018")
    egammaEra = '2018-Prompt'
    setupEgammaPostRecoSeq(process,
                       era=egammaEra)


# only applied to "2016" and 2017

if year == "2016" or year == "2017":
    ## prefiring weights
    from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
    process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
        DataEra = cms.string(prefire_era), #Use 2016BtoH for 2016
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUncty = cms.double(0.2),
        SkipWarnings = False)



# FSR RECOVERY
from FSRPhotonRecovery.FSRPhotons.FSRphotonSequence_cff import addFSRphotonSequence
PhotonMVA="FSRPhotonRecovery/FSRPhotons/data/PhotonMVAv9_BDTG800TreesDY.weights.xml"
addFSRphotonSequence(process, 'slimmedMuons', PhotonMVA)


process.GlobalTag.globaltag = globalTag

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring())

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

process.TFileService = cms.Service("TFileService", fileName = cms.string("ntuple.root") )

process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJEC * 
    process.updatedPatJetsUpdatedJEC)

if year == "2016":
    process.p = cms.Path(
    process.prefiringweight *
    process.egammaPostRecoSeq *
    process.jecSequence * 
    process.FSRphotonSequence*
    process.ntuplemaker_H2DiMuonMaker)
if year == "2017":
    process.p = cms.Path(
    process.prefiringweight *
    process.egammaPostRecoSeq *
    process.jecSequence * 
    process.fullPatMetSequenceModifiedMET * 
    process.FSRphotonSequence*
    process.ntuplemaker_H2DiMuonMaker)
if year == "2018":
        process.p = cms.Path(
    process.egammaPostRecoSeq *
    process.jecSequence * 
    process.FSRphotonSequence*
    process.ntuplemaker_H2DiMuonMaker)
