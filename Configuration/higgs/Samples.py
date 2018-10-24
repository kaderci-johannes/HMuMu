import shelve, pickle
import Dataset as DS
import os,sys,subprocess


if "ANALYSISHOME" not in os.environ.keys():
    raise NameError("Can not find ANALYSISHOME env var")
sys.path.append(os.environ["ANALYSISHOME"])

#
#   CMSSW Datasets
#   
#

#   Datasets from Collisions
data_2016 = {
}

data_2017 = {
    "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD" : DS.Dataset(
        name = "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD",
        isData = True,
        year = 2017,
        globaltag = "94X_dataRun2_v10"),
    "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD" : DS.Dataset(
        name = "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD",
        isData = True,
        year = 2017,
        globaltag = "94X_dataRun2_v10"),
    "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD" : DS.Dataset(
        name = "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD",
        isData = True,
        year = 2017,
        globaltag = "94X_dataRun2_v10"),
    "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD" : DS.Dataset(
        name = "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD",
        isData = True,
        year = 2017,
        globaltag = "94X_dataRun2_v10"),
    "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD" : DS.Dataset(
        name = "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD",
        isData = True,
        year = 2017,
        globaltag = "94X_dataRun2_v10"),

}

data_2018 = {
}

#   Datasets from Monte Carlo
mc_signal_2016 = {
}

mc_background_2016 = {
}

mc_signal_2017 = {
    "/GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/GluGluHToMuMu_M125_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = True,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.01057
),
    "/VBFHToMuMu_M125_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/VBFHToMuMu_M125_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = True,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = .0008230
),
    "/WplusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM" : DS.MCDataset(
        name = "/WplusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = True,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.0001852
),
    "/WminusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WminusH_HToMuMu_WToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = True,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.0001160
),
    "/ZH_HToMuMu_ZToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/ZH_HToMuMu_ZToAll_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = True,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.0001923
),
    "/ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM" : DS.MCDataset(
        name = "/ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = True,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.00011034
),

}

mc_background_2017 = {
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 85.656
)
,
    "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM" : DS.MCDataset(
        name = "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 11.61
)
,
    "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 5.595
)
,
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 4.42965
)
,
    "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 45.99
)
,
    "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 45.99
)
,
    "/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM" : DS.MCDataset(
        name = "/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 12.46
)
,
    "/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 12.46
)
,
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.2086
)
,
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 0.1651
)
,
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 687.1
)
,
    "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" : DS.MCDataset(
        name = "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
        isData = False,
        year = 2017,
        isSignal = False,
        initial_cmssw = "94X",
        globaltag = "94X_mc2017_realistic_v15",
        cross_section = 16.523
)
}

mc_signal_2018 = {
}

mc_background_2018 = {
}

#
#   JSON File with Good Runs, Latest JSON files can be found on:
#   https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/
#
jsonfiles = {
    #   latest
    "EOY2017ReReco" : DS.JsonFile(
        filename = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt",
        intlumi =  41368
        )
}


#
#   Useful functions to build up the name
#
def buildDatasetTagName(ntuple):
    if ntuple.isData:
        s = "%s__%s" % (ntuple.label.split("__")[1],ntuple.json[:-4])
    else:
        s = "%s" % (ntuple.cmssw)
    if ntuple.aux!=None and ntuple.aux!="":
        s+="__%s" % ntuple.aux
    return s

def buildRequestName(ntuple, *kargs):
    if ntuple.isData:
        s = ntuple.label.split("__")[1]
        s += "__%s"%kargs[0]
    else:
        if ntuple.isSignal:
            s = ntuple.label.split("__")[0] + "__%s" % ntuple.initial_cmssw
        else:
#            s = ntuple.label.split("__")[0].split("-")[0]+"__%s" % ntuple.initial_cmssw
            s = ntuple.label.split("__")[0]+"__%s" % ntuple.initial_cmssw
    if ntuple.aux!=None and ntuple.aux!="":
        s+="__%s" % ntuple.aux
    return s

def isReReco(dataset):
    if dataset.year==2015:
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
    if cmd=="eosls":
        proc = subprocess.check_output(["eos","root://cmseos.fnal.gov","ls", args])
    return proc

def buildTimeStamp(ntuple):
    fullpattern = os.path.join(ntuple.rootpath,
        ntuple.label.split("__")[0],
        buildDatasetTagName(ntuple), "*")
    cmd = "ls" if ntuple.storage=="local" else "eosls"
    if ntuple.storage=="local":
        args = fullpattern
    else:
        args = "%s" % fullpattern
    x = eos_system(cmd, args).split("\n")[0]
    return x

def discoverFileList(ntuple):
    fullpath= os.path.join(ntuple.rootpath,
        ntuple.label.split("__")[0],
        buildDatasetTagName(ntuple), buildTimeStamp(ntuple), "0000")
    fullpattern = os.path.join(fullpath, "*.root")
    cmd = "ls" if ntuple.storage=="local" else "eosls"
    args = "-d %s" % fullpattern if ntuple.storage=="local" else "%s" % fullpattern
    x = eos_system(cmd, args).split("\n")[:-1]
    if ntuple.storage=="EOS":
        xxx = []
        for f in x:
            fullpathname = os.path.join("root://cmsxrootd.fnal.gov//")
            fullpathname = fullpathname+os.path.join(fullpath, f)
            xxx.append(fullpathname)
        return xxx
    return x

def buildFileListName(ntuple):
    if ntuple.isData:
        s = "filelist__%s__%s" % (ntuple.label.split("__")[1],
                ntuple.json[:-4])
    else:
        s = "filelist__%s__%s" % (ntuple.label.split("__")[0],
            ntuple.cmssw)
    if ntuple.aux!=None and ntuple.aux!="":
        s += "__%s" % ntuple.aux
    s+=".files"
    return s

def buildResultOutputPathName(result):
    s = "result"
    if result.isData:
        s+="__%s__%s" % (result.label.split("__")[1],
            result.json[:-4])
    else:
        s += "__%s__%s__%s__%smb" % (result.label.split("__")[0],
            result.cmssw, result.pileupdata.datajson[:-4], 
            result.pileupdata.cross_section)
    if result.aux!=None and result.aux!="":
        s += "__%s" % result.aux
    s += ".root"
    return s

def discoverNtuples(ntuple):
    prefix = ""
    if ntuple.storage=="EOS":
        prefix+="/eos/cms"
        tstamp = getTimeStamp(ntuple)
        ntuple.timestamp = tstamp
        pathstring = os.path.join(prefix, ntuple.rootpath, ntuple.name.split("/")[0],
            buildDatasetTagName(ntuple), tstamp, "0000")
        x = eos_system("eos", "ls %s/*.root" % pathstring).split("\n")
        return pathstring,x
    else:
        pathstring = os.path.join(prefix, ntuple.rootpath, ntuple.name.split("/")[0],
            buildDatasetTagName(ntuple))
        x = eos_system("eos", "ls %s/*.root" % pathstring).split("\n")
        return pathstring,x

def getFileList(ntuple):
    pass

if __name__=="__main__":
    pass
