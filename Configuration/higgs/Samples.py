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

#   Datasets from Data, Currently 2017 ReReco

datadatasets = {
    "/SingleMuon/Run2017B-17Nov2017-v1/MINIAOD" : DS.Dataset(
        name = "/SingleMuon/Run2017B-17Nov2017-v1/MINIAOD",
        isData = True,
        year = 2017,
        globaltag = "94X_dataRun2_v6"),
}

#   Datasets from Monte Carlo
mcdatasets = {
}

#
#   JSON File with Good Runs, Latest JSON files can be found on:
#   https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/
#
jsonfiles = {
    #   latest
    "2017_Synch" : DS.JsonFile(
        filename = "Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt",
        intlumi =  41368
        ),
    "run297113" : DS.JsonFile(
        filename = "json297113.txt",
        intlumi = 1
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
