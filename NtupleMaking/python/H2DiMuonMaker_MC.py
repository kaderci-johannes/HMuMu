import FWCore.ParameterSet.Config as cms
pt = 27

name = "H2DiMuonMaker"

ntuplemaker_H2DiMuonMaker = cms.EDAnalyzer(
    name,
    #   Tags
    tagMuons=cms.untracked.InputTag("slimmedMuons"),
    tagElectrons=cms.untracked.InputTag("slimmedElectrons"),
    tagTaus=cms.untracked.InputTag("slimmedTaus"),
    tagPV=cms.untracked.InputTag("offlineSlimmedPrimaryVertices"),
    tagBS=cms.untracked.InputTag("offlineBeamSpot"),
    tagPrunedGenParticles=cms.untracked.InputTag("prunedGenParticles"),
    tagPackedGenParticles=cms.untracked.InputTag("packedGenParticles"),
    tagTriggerResults=cms.untracked.InputTag("TriggerResults", "", "HLT"),
    tagTriggerObjects=cms.untracked.InputTag("slimmedPatTrigger"),
    tagMetFilterResults=cms.untracked.InputTag("TriggerResults", "", "RECO"),
    tagMET=cms.untracked.InputTag("slimmedMETsModifiedMET"),
    tagJets=cms.untracked.InputTag("updatedPatJetsUpdatedJEC"),
    tagRho = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
    tagGenJets=cms.untracked.InputTag("slimmedGenJets"),
    tagConversions=cms.untracked.InputTag("reducedEgamma:reducedConversions"),

    rochesterFile=cms.FileInPath("RoccoR2017.txt"),
    btagFile=cms.FileInPath("DeepCSV_94XSF_V3_B_F.csv"),

    # electron cut based id
    tagElectronCutBasedId_veto=cms.untracked.InputTag(
        "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto"),
    tagElectronCutBasedId_loose=cms.untracked.InputTag(
        "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose"),
    tagElectronCutBasedId_medium=cms.untracked.InputTag(
        "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium"),
    tagElectronCutBasedId_tight=cms.untracked.InputTag(
        "egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight"),

    #
    #	Meta Data
    #
    checkTrigger=cms.untracked.bool(True),
    isMC=cms.untracked.bool(True),
    triggerNames=cms.untracked.vstring(
        "HLT_IsoMu%d" % pt, "HLT_IsoTkMu%d" % pt),
    metFilterNames=cms.untracked.vstring(["Flag_goodVertices",
                                          # "Flag_globalSuperTightHalo2016Filter", NOT SUGGESTED
                                          "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter",
                                          "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter", "Flag_BadChargedCandidateFilter"]),
    #   , "Flag_eeBadScFilter"]), NOT SUGGESTED

    nMuons=cms.untracked.int32(2),
    isGlobalMuon=cms.untracked.bool(True),
    isStandAloneMuon=cms.untracked.bool(False),
    isTrackerMuon=cms.untracked.bool(True),
    minPt=cms.untracked.double(20),
    maxeta=cms.untracked.double(2.4),
    btagNames=cms.untracked.vstring(
        ["pfDeepCSVJetTags:probb", "pfDeepCSVJetTags:probbb"]),
    tauIDNames=cms.untracked.vstring([""]),

    #
    #   Some flags
    #
    useElectrons=cms.untracked.bool(True),
    useTaus=cms.untracked.bool(False))
