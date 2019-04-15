year = "2016"

import FWCore.ParameterSet.Config as cms
process = cms.Process("NtupleMaking")

#
#   loading sequences
#
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10
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
os.environ["CMSSW_SEARCH_PATH"] += os.pathsep + os.getcwd()
import Samples as S
thisIsData = False

globaltags = {
    "2016": S.mc_global_tag_2016,
    "2017": S.mc_global_tag_2017,
    "2018": S.mc_global_tag_2018
}
globalTag = globaltags[year]


if year == "2016":
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_94X16MC")
elif year == "2017":
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_94X17MC")
elif year == "2018":
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_102X18MC")


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
    prefire_era = '2017BtoF'
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
    process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
        DataEra = cms.string(prefire_era), #Use 2016BtoH for 2016
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUncty = cms.double(0.2),
        SkipWarnings = False)




# FSR RECOVERY
from FSRPhotonRecovery.FSRPhotons.FSRphotonSequence_cff import addFSRphotonSequence
PhotonMVA="FSRPhotonRecovery/FSRPhotons/data/PhotonMVAv9_BDTG800TreesDY.weights.xml"
addFSRphotonSequence(process, 'slimmedMuons', PhotonMVA)


process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJEC *
    process.updatedPatJetsUpdatedJEC)

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(100))
files = {
    "2016" : "file:/afs/cern.ch/user/m/malhusse/files/0EFDF441-B135-E911-B24F-AC1F6B1AEFEE.root",
    "2017" : "file:/afs/cern.ch/user/m/malhusse/files/0AEB8E40-E03D-E911-8E67-0CC47AA98A0E.root",
    "2018" : "file:/afs/cern.ch/user/m/malhusse/files/E7FAE092-29DE-AA4B-9891-6958578145DA.root",
}
process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(
    files[year]
))

# readFiles)
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False))
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()

outputfname = "ntuple_MC{}.root".format(year)

process.TFileService = cms.Service(
    "TFileService", fileName=cms.string(outputfname))

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
