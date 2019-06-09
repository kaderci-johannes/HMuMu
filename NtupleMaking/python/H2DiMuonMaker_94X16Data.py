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
    tagMET=cms.untracked.InputTag("slimmedMETs"),
    tagJets=cms.untracked.InputTag("updatedPatJetsUpdatedJEC"),
    tagRho=cms.untracked.InputTag("fixedGridRhoFastjetAll"),
    tagGenJets=cms.untracked.InputTag("slimmedGenJets"),
    tagConversions=cms.untracked.InputTag("reducedEgamma:reducedConversions"),
    tagCands=cms.InputTag("packedPFCandidates"),

    rochesterFile=cms.FileInPath("../data/Roccor/RoccoR2016.txt"),
    btagFile=cms.FileInPath("../data/BtagSF/DeepCSV_2016LegacySF_V1.csv"),
    muonIsoFile=cms.FileInPath("../data/MuonSF/RunBCDEF2016_SF_ISO.json"),
    muonIdFile=cms.FileInPath("../data/MuonSF/RunBCDEF2016_SF_ID.json"),
    muonTrigFile=cms.FileInPath(
        "../data/MuonSF/EfficienciesAndSF_RunBtoF_MuTrig.root"),

    muon_id_sf_wp_num=cms.string("MediumID"),
    muon_id_sf_wp_den=cms.string("genTracks"),
    muon_iso_sf_wp_num=cms.string("LooseRelIso"),
    muon_iso_sf_wp_den=cms.string("MediumID"),

    #
    #	Meta Data
    #
    checkTrigger=cms.untracked.bool(True),
    isMC=cms.untracked.bool(False),
    triggerNames=cms.untracked.vstring(
        "HLT_IsoMu%d" % pt, "HLT_IsoTkMu%d" % pt),
    metFilterNames=cms.untracked.vstring(["Flag_goodVertices", "Flag_globalSuperTightHalo2016Filter", "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter",
                                          "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter"
                                          # , "Flag_BadChargedCandidateFilter" as per https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2
                                          ]),

    nMuons=cms.untracked.int32(2),
    isGlobalMuon=cms.untracked.bool(True),
    isStandAloneMuon=cms.untracked.bool(False),
    isTrackerMuon=cms.untracked.bool(True),
    minPt=cms.untracked.double(20),
    maxeta=cms.untracked.double(2.4),
    btagNames=cms.untracked.vstring(
        ["pfDeepCSVJetTags:probb", "pfDeepCSVJetTags:probbb"]),
    tauIDNames=cms.untracked.vstring([""]),

    deepCSVL=cms.untracked.double(0.2217),
    deepCSVM=cms.untracked.double(0.6321),
    deepCSVT=cms.untracked.double(0.8953),


    #
    #  flags
    #
    useElectrons=cms.untracked.bool(True),
    useTaus=cms.untracked.bool(False),
)
