import FWCore.ParameterSet.Config as cms
pt = 27

name = "H2DiMuonMaker_NoPairing"
hlt = "HLT"

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
    tagTriggerResults=cms.untracked.InputTag("TriggerResults", "", hlt),
    tagTriggerObjects=cms.untracked.InputTag("slimmedPatTrigger"),
    tagMET=cms.untracked.InputTag("slimmedMETs"),
    tagPFJets=cms.untracked.InputTag("slimmedJets"),
    tagGenJets=cms.untracked.InputTag("slimmedGenJets"),
    tagConversions=cms.untracked.InputTag("reducedEgamma:reducedConversions"),

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
    triggerNames=cms.untracked.vstring("HLT_IsoMu%d" % pt, "HLT_IsoTkMu%d" % pt),
    nMuons=cms.untracked.int32(2),
    isGlobalMuon=cms.untracked.bool(True),
    isStandAloneMuon=cms.untracked.bool(False),
    isTrackerMuon=cms.untracked.bool(True),
    minPt=cms.untracked.double(10),
    maxeta=cms.untracked.double(2.4),
    btagNames=cms.untracked.vstring(["pfDeepCSVJetTags:probb", "pfDeepCSVJetTags:probbb"]),
    tauIDNames=cms.untracked.vstring([""]),

    #
    #   Some flags
    #
    useElectrons=cms.untracked.bool(True),
    useTaus=cms.untracked.bool(False))
