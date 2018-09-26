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
#import Dataset as DS

#data_datasets = S.datadatasets
#mc_datasets = Samples.mcMoriond2017datasets
jsonfiles = S.jsonfiles
# print(data_datasets)

jsontag = "2017_Synch"
jsonfile = jsonfiles[jsontag]
#dataset = None
#dataset = data_datasets["/SingleMuon/Run2017B-17Nov2017-v1/MINIAOD"]
# print(dataset)

# if dataset == None:
#    print("-" * 40)
#    print("dataset is None")
#    print("-" * 40)
#    sys.exit(1)

# ntuple = DS.Ntuple(
#    dataset,
json = "json/" + jsonfile.filename
#    storage=None,
#    rootpath=None,
#    timestamp=None,
#    cmssw="94X")

#
#   a few settings
#
#thisIsData = ntuple.isData
thisIsData = True
#globalTag = ntuple.globaltag
#globalTag = '94X_dataRun2_v10'
globalTag = '94X_dataRun2_ReReco_EOY17_v6'
#readFiles = cms.untracked.vstring()
#readFiles.extend(open(("sample_file_lists/%s/" % ("data" if ntuple.isData else "mc"))+ntuple.test_file).read().splitlines())

# print(readFiles)
#
#   Differentiate between DATA and MC
#
if not thisIsData:
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_MC")
else:
    process.load("HMuMu.NtupleMaking.H2DiMuonMaker_Data")
    print("DATA")

# #
# #   Debug/Loggin
# #
print("")
print("")
print('Loading Global Tag: ' + globalTag)
process.GlobalTag.globaltag = globalTag
print("")
print("")
if thisIsData:
    print('Running over data sample')
else:
    print('Running over MC sample')

#print("Sample Name:    " + ntuple.name)
print("")
print("")

# JET ENERGY CORRECTIONS

from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

updateJetCollection(
    process,
    jetSource=cms.InputTag('slimmedJets'),
    labelName='UpdatedJEC',
    # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
    jetCorrections=('AK4PFchs', cms.vstring(
        ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')
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
# #   Pool Source with proper LSs
# #
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(
    # 'file:DE1721FC-10D9-E711-B475-0025907B4F04.root'))
    'file:/eos/cms/store/user/amarini/Sync/0E555487-7241-E811-9209-002481CFC92C.root'))

# readFiles)
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False))
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
if thisIsData:
    import FWCore.PythonUtilities.LumiList as LumiList
    process.source.lumisToProcess = LumiList.LumiList(
        #        filename=ntuple.json).getVLuminosityBlockRange()
        filename=json).getVLuminosityBlockRange()

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

process.TFileService = cms.Service(
    "TFileService", fileName=cms.string("ntuple_Data.root"))
process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC)
process.p = cms.Path(process.egammaPostRecoSeq * process.egmGsfElectronIDSequence *
                     process.jecSequence * process.fullPatMetSequenceModifiedMET * 
                     process.ntuplemaker_H2DiMuonMaker)

# this outputs the original file with all info!
# process.out = cms.OutputModule(
#    "PoolOutputModule", fileName=cms.untracked.string("test.root"))
#process.finalize = cms.EndPath(process.out)
#
