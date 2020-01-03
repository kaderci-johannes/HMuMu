import shelve
import pickle
import Dataset as DS
import os
import sys
import subprocess


if "ANALYSISHOME" not in os.environ.keys():
    raise NameError("Can not find ANALYSISHOME env var")
sys.path.append(os.environ["ANALYSISHOME"])

#
#   Global Tags
#
data_global_tag_2016 = "94X_dataRun2_v10"
mc_global_tag_2016 = "94X_mcRun2_asymptotic_v3"

data_global_tag_2017 = "94X_dataRun2_v11"
mc_global_tag_2017 = "94X_mc2017_realistic_v17"

data_global_tag_2018_prompt = "102X_dataRun2_Prompt_v15"
data_global_tag_2018 = "102X_dataRun2_Sep2018ABC_v12"
mc_global_tag_2018 = "102X_upgrade2018_realistic_v20"

# FORMATING
#
# DATA
# "" : DS.Dataset(
#     name = "",
#     isData = True,
#     year = ,
#     globaltag = ),
#
# Monte Carlo
# "" : DS.MCDataset(
#     name = "",
#     isData = False,
#     year = 201,
#     isSignal = ,
#     initial_cmssw = "",
#     globaltag = ,
#     cross_section = ),


#   ___   ___  __   __
#  |__ \ / _ \/_ | / /
#     ) | | | || |/ /_
#    / /| | | || | '_ \
#   / /_| |_| || | (_) |
#  |____|\___/ |_|\___/

data_2016 = {
    # "/SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD": DS.Dataset(
    #     name="/SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD",
    #     isData=True,
    #     year=2016,
    #     globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),
    "/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD",
        isData=True,
        year=2016,
        globaltag=data_global_tag_2016),

}

#   Datasets from Monte Carlo
mc_signal_2016 = {
    "/GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.010571
    ),
    "/VBFHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000823
    ),
    "/ttHToMuMu_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.00011
    ),
    "/WplusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000183
    ),
    "/WminusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000116
    ),
    "/ZH_HToMuMu_ZToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000192
    )
}
mc_signal_2016_extra = {
    "/GluGluHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.012653
    ),
    "/GluGluHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.008505
    ),
    "/VBFHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000953
    ),
    "/VBFHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000683
    ),
    "/ttHToMuMu_M120_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M120_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000138
    ),
    "/ttHToMuMu_M130_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M130_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000085
    ),
    "/WplusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000232
    ),

    "/WplusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000139
    ),
    "/WminusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000148
    ),

    "/WminusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000088
    ),

    "/ZH_HToMuMu_ZToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000241
    ),

    "/ZH_HToMuMu_ZToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.000148
    )

}

mc_background_2016 = {
    "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=5765.4
    ),
    "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=87.31
    ),
    "/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=358.57
    ),
    "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=54.23
    ),
    "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=54.23
    ),
    "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM": DS.MCDataset(
        name="/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.2529
    ),
    "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM": DS.MCDataset(
        name="/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.2529
    ),
    "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.2043
    ),
    "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM": DS.MCDataset(
        name="/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.2043
    ),
    "/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.006983
    ),
    "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=35.85
    ),
    "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=35.85
    ),
    "/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=12.178
    ),
    "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=5.595
    ),
    "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=4.6660
    ),
    "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=3.22
    ),
    "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM": DS.MCDataset(
        name="/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=1.256
    ),
    "/ZZTo4L_13TeV_powheg_pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZTo4L_13TeV_powheg_pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=1.256
    ),
    "/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=1.256
    ),
    "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.1651
    ),
    "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.2086
    ),
    "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.05565
    ),
    "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=0.01398
    ),
}

mc_background_2016_extra = {
    "/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=47.12
    ),
    "/EWK_LLJJ_MLL-50_MJJ-120_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM": DS.MCDataset(
        name="/EWK_LLJJ_MLL-50_MJJ-120_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
        isData=False,
        year=2016,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2016,
        cross_section=1.611
    )
}

#   ___   ___  __ ______
#  |__ \ / _ \/_ |____  |
#     ) | | | || |   / /
#    / /| | | || |  / /
#   / /_| |_| || | / /
#  |____|\___/ |_|/_/

data_2017 = {
    "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD",
        isData=True,
        year=2017,
        globaltag=data_global_tag_2017),
    "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD",
        isData=True,
        year=2017,
        globaltag=data_global_tag_2017),
    "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD",
        isData=True,
        year=2017,
        globaltag=data_global_tag_2017),
    "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD",
        isData=True,
        year=2017,
        globaltag=data_global_tag_2017),
    "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD",
        isData=True,
        year=2017,
        globaltag=data_global_tag_2017),

}

mc_signal_2017 = {
    "/GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.010571
    ),
    "/VBFHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000823
    ),
    "/ttHToMuMu_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.00011
    ),
    "/ZH_HToMuMu_ZToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000192
    ),
    "/WplusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000183
    ),
    "/WminusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000116
    )
}

mc_signal_2017_extra = {
    "/GluGluHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.012653
    ),
    "/GluGluHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.008505
    ),
    "/VBFHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000953
    ),
    "/VBFHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000683
    ),
    "/ttHToMuMu_M120_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M120_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000138
    ),
    "/ttHToMuMu_M130_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM ": DS.MCDataset(
        name="/ttHToMuMu_M130_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000085
    ),
    "/ZH_HToMuMu_ZToAll_M120_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M120_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000241
    ),
    "/ZH_HToMuMu_ZToAll_M130_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M130_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000148
    ),
    "/WplusH_HToMuMu_WToAll_M120_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M120_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000232
    ),
    "/WplusH_HToMuMu_WToAll_M130_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M130_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000139
    ),
    "/WminusH_HToMuMu_WToAll_M120_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M120_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000148
    ),
    "/WminusH_HToMuMu_WToAll_M130_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M130_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=True,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.000088
    )
}

mc_background_2017 = {
    "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=6225.42
    ),
    "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=6225.42
    ),
    "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=87.31
    ),
    "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=54.23
    ),
    "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=34.91
    ),
    "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=34.97
    ),
    "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=11.61
    ),
    "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=5.595
    ),
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=4.42965
    ),
    "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=45.99
    ),
    "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=45.99
    ),
    "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=12.178
    ),
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.2086
    ),
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.1651
    ),
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=358.57
    ),
    "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=16.523
    ),
    "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.2043
    ),    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.2043
    ),
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.2529
    ),
    "/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.2529
    ),
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.006983
    ),
    "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=3.22
    ),
    "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM": DS.MCDataset(
        name="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=1.256
    ),
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.05565
    ),
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=0.01398
    )

}

mc_background_2017_extra = {
    "/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=47.12
    ),
    "/EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=4.321
    ),
    "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM": DS.MCDataset(
        name="/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData=False,
        year=2017,
        isSignal=False,
        initial_cmssw="94X",
        globaltag=mc_global_tag_2017,
        cross_section=831.76
    )
}

#   ___   ___  __  ___
#  |__ \ / _ \/_ |/ _ \
#     ) | | | || | (_) |
#    / /| | | || |> _ <
#   / /_| |_| || | (_) |
#  |____|\___/ |_|\___/

data_2018 = {
    "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD",
        isData=True,
        year=2018,
        globaltag=data_global_tag_2018),
    "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD",
        isData=True,
        year=2018,
        globaltag=data_global_tag_2018),
    "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD",
        isData=True,
        year=2018,
        globaltag=data_global_tag_2018),
    "/SingleMuon/Run2018D-PromptReco-v2/MINIAOD": DS.Dataset(
        name="/SingleMuon/Run2018D-PromptReco-v2/MINIAOD",
        isData=True,
        year=2018,
        globaltag=data_global_tag_2018_prompt),

}

mc_signal_2018 = {

    "/GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.010571
    ),
    "/VBFHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M125_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000823
    ),
    "/ttHToMuMu_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.00011
    ),
    "/WplusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000183
    ),
    "/WminusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000116
    ),
    "/ZH_HToMuMu_ZToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000192
    )
}

mc_signal_2018_extra = {
    "/GluGluHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.012653
    ),
    "/GluGluHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/GluGluHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.008505
    ),
    "/VBFHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M120_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000953
    ),
    "/VBFHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/VBFHToMuMu_M130_TuneCP5_PSweights_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000683
    ),
    "/ttHToMuMu_M120_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M120_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000138
    ),
    "/ttHToMuMu_M130_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/ttHToMuMu_M130_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000085
    ),
    "/WplusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000232
    ),
    "/WplusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WplusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000139
    ),
    "/WminusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000148
    ),
    "/WminusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WminusH_HToMuMu_WToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000088
    ),
    "/ZH_HToMuMu_ZToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M120_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000241
    ),
    "/ZH_HToMuMu_ZToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/ZH_HToMuMu_ZToAll_M130_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=True,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.000148
    ),
}

mc_background_2018 = {
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=6225.42
    ),
    "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=6225.42
    ),
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=87.31
    ),
    "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=54.23
    ),
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=358.57
    ),
    "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=35.85
    ),
    "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=35.85
    ),
    "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=12.178
    ),
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=4.6660
    ),
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=4.6660
    ),
    "/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=4.42965
    ),
    "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=5.595
    ),
    "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=3.22
    ),
    "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=1.256
    ),
    "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=1.256
    ),
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.2043
    ),
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.2529
    ),
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.006983
    ),
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM": DS.MCDataset(
        name="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.006983
    ),
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.2086
    ),
    "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.1651
    ),
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.05565
    ),
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
        name="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=0.01398
    )
}

mc_background_2018_extra = {
    "/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=47.12
    ),
    "/EWKZ2Jets_ZToLL_M-50_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM": DS.MCDataset(
        name="/EWKZ2Jets_ZToLL_M-50_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
        isData=False,
        year=2018,
        isSignal=False,
        initial_cmssw="102X",
        globaltag=mc_global_tag_2018,
        cross_section=4.321
    ),
    "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM": DS.MCDataset(
    name="/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",
    isData=False,
    year=2018,
    isSignal=False,
    initial_cmssw="102X",
    globaltag=mc_global_tag_2018,
    cross_section=86.61
    )
}
#
#   JSON File with Good Runs, Latest JSON files can be found on:
#   https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/
#
jsonfiles = {
    #   latest
    "2016": DS.JsonFile(
        filename="Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
        intlumi=35920
    ),
    "2017": DS.JsonFile(
        filename="Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt",
        intlumi=41530
    ),
    "2018": DS.JsonFile(
        filename="Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt",
        intlumi=59970
    )
}


#
#   Useful functions to build up the name
#
def buildDatasetTagName(ntuple):
    if ntuple.isData:
        s = "%s__%s" % (ntuple.label.split("__")[1], ntuple.json[:-4])
    else:
        s = "%s" % (ntuple.cmssw)
    if ntuple.aux != None and ntuple.aux != "":
        s += "__%s" % ntuple.aux
    return s


def buildRequestName(ntuple, *kargs):
    if ntuple.isData:
        s = ntuple.label.split("__")[1]
        s += "__%s" % kargs[0]
    else:
        if ntuple.isSignal:
            s = ntuple.label.split("__")[0] + "__%s" % ntuple.initial_cmssw
        else:
            #            s = ntuple.label.split("__")[0].split("-")[0]+"__%s" % ntuple.initial_cmssw
            s = ntuple.label.split("__")[0]+"__%s" % ntuple.initial_cmssw
    if ntuple.aux != None and ntuple.aux != "":
        s += "__%s" % ntuple.aux
    return s


def isReReco(dataset):
    if dataset.year == 2015:
        if "16Dec2015" in dataset.name:
            return True
        else:
            return False
    else:
        return False


def buildPUfilename(ntuple):
    if ntuple.isData:
        sdata = "pileup__%s__%smb.root" % (ntuple.pileupdata.datajson[:-4],
                                           ntuple.pileupdata.cross_section)
        return sdata
    else:
        smc = "pileup__%s__%s.root" % (ntuple.label.split("__")[0],
                                       ntuple.cmssw)
        return smc


def buildPUfilenames(result):
    sdata = "pileup__%s__%smb.root" % (result.pileupdata.datajson[:-4],
                                       result.pileupdata.cross_section)
    smc = "pileup__%s__%s.root" % (result.label.split("__")[0],
                                   result.cmssw)
    return (smc, sdata)


def eos_system(cmd, args):
    import subprocess
    if cmd == "eosls":
        proc = subprocess.check_output(
            ["eos", "root://cmseos.fnal.gov", "ls", args])
    return proc


def buildTimeStamp(ntuple):
    fullpattern = os.path.join(ntuple.rootpath,
                               ntuple.label.split("__")[0],
                               buildDatasetTagName(ntuple), "*")
    cmd = "ls" if ntuple.storage == "local" else "eosls"
    if ntuple.storage == "local":
        args = fullpattern
    else:
        args = "%s" % fullpattern
    x = eos_system(cmd, args).split("\n")[:-1]
    return x


def multipleDirectories(ntuple, timestamp):
    fullpattern = os.path.join(ntuple.rootpath,
                               ntuple.label.split("__")[0],
                               buildDatasetTagName(ntuple), timestamp)
    cmd = "eosls"
    args = "%s" % fullpattern
    x = eos_system(cmd, args).split("\n")[:-1]
    return x


def discoverFileList(ntuple, timestamp):
    files = []
    for directory in multipleDirectories(ntuple, timestamp):
        fullpath = os.path.join(ntuple.rootpath,
                                ntuple.label.split("__")[0],
                                buildDatasetTagName(ntuple),
                                timestamp,
                                directory)
        fullpattern = os.path.join(fullpath, "*.root")
        cmd = "eosls"
        args = fullpattern
        x = eos_system(cmd, args).split("\n")[:-1]
        if ntuple.storage == "EOS":
            for f in x:
                fullpathname = os.path.join("root://cmsxrootd.fnal.gov/")
                fullpathname = fullpathname+os.path.join(fullpath, f)
                files.append(fullpathname)
    return files


def buildFileListName(ntuple):
    s = ntuple.label
    s += ".files"
    return s


def buildResultOutputPathName(result):
    s = "result"
    if result.isData:
        s += "__%s__%s" % (result.label.split("__")[1],
                           result.json[:-4])
    else:
        s += "__%s__%s__%s__%smb" % (result.label.split("__")[0],
                                     result.cmssw, result.pileupdata.datajson[:-4],
                                     result.pileupdata.cross_section)
    if result.aux != None and result.aux != "":
        s += "__%s" % result.aux
    s += ".root"
    return s


def discoverNtuples(ntuple):
    prefix = ""
    if ntuple.storage == "EOS":
        prefix += "/eos/cms"
        tstamp = getTimeStamp(ntuple)
        ntuple.timestamp = tstamp
        pathstring = os.path.join(prefix, ntuple.rootpath, ntuple.name.split("/")[0],
                                  buildDatasetTagName(ntuple), tstamp, "0000")
        x = eos_system("eos", "ls %s/*.root" % pathstring).split("\n")
        return pathstring, x
    else:
        pathstring = os.path.join(prefix, ntuple.rootpath, ntuple.name.split("/")[0],
                                  buildDatasetTagName(ntuple))
        x = eos_system("eos", "ls %s/*.root" % pathstring).split("\n")
        return pathstring, x


def getFileList(ntuple):
    pass


if __name__ == "__main__":
    pass
