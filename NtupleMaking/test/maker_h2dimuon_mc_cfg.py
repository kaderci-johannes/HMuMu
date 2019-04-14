#
#   Ntuple Making Stage
#

import FWCore.ParameterSet.Config as cms
process = cms.Process("NtupleMaking")

#
#   loading sequences
#
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

import os
import sys
import shelve
import pickle
if "ANALYSISHOME" not in os.environ.keys():
    raise NameError("Can not find ANALYSISHOME env var")
sys.path.append(os.path.join(
    os.environ["ANALYSISHOME"], "Configuration", "higgs"))
import Samples as S
thisIsData = False
year = "2017"

globalTag = S.mc_global_tag_2017

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

print("")
print('Loading Global Tag: ' + globalTag)
process.GlobalTag.globaltag = globalTag
print("")
print('Running over MC sample')

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

runVid = True
runCorrections = False
egammaEra = '2017-Nov17ReReco'
if year == "2016":
    print("running on 2016")
    egammaEra = '2016-Legacy'
    prefire_era = '2016BtoH'
if year == "2017":
    print("running on 2017")
    egammaEra = '2017-Nov17ReReco'
    runVid = False
    runCorrections = True
    prefire_eta = '2017BtoF'
if year == "2018":
    print("running on 2018")
    egammaEra = '2018-Prompt'

    # vid = False
# electron energy scale correction fix SEE https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
                       runEnergyCorrections=runCorrections,
                       runVID=runVid,  # saves CPU time by not needlessly re-running VID
                       era=egammaEra)



# only applied to "2016" and 2017

if year == "2016" or year == "2017":
    ## prefiring weights
    from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer

    process.prefiringweight = cms.EDProducer("L1ECALPrefiringWeightProducer",
                                    ThePhotons = cms.InputTag("slimmedPhotons"),
                                    TheJets = cms.InputTag("slimmedJets"),
                                    L1Maps = cms.string("/afs/cern.ch/work/m/malhusse/private/h2mu/CMSSW_9_4_9_cand2/src/L1Prefiring/EventWeightProducer/files/L1PrefiringMaps_new.root"), # update this line with the location of this file
                                    DataEra = cms.string("2017BtoF"), #Use 2016BtoH for 2016
                                    UseJetEMPt = cms.bool(False), #can be set to true to use jet prefiring maps parametrized vs pt(em) instead of pt
                                    PrefiringRateSystematicUncty = cms.double(0.2) #Minimum relative prefiring uncty per object
                                    )




# FSR RECOVERY
from FSRPhotonRecovery.FSRPhotons.FSRphotonSequence_cff import addFSRphotonSequence
PhotonMVA="FSRPhotonRecovery/FSRPhotons/data/PhotonMVAv9_BDTG800TreesDY.weights.xml"
addFSRphotonSequence(process, 'slimmedMuons', PhotonMVA)


process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJEC * 
    process.updatedPatJetsUpdatedJEC)

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(1000))

process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(
    # 'file:DE1721FC-10D9-E711-B475-0025907B4F04.root'))
    'file:/eos/cms/store/user//amarini/Sync/5AC9148F-9842-E811-892B-3417EBE535DA.root'))

# readFiles)
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False))
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()

process.TFileService = cms.Service(
    "TFileService", fileName=cms.string("ntuple_MC.root"))

process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC)

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