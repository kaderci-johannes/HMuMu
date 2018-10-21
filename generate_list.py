import os
import sys
sys.path.append(os.path.join(
os.environ["ANALYSISHOME"], "Configuration", "higgs"))
import Samples as S
import Dataset as DS

data_datasets = S.data_2017

jsonfiles = S.jsonfiles
jsontag = "EOY2017ReReco"
jsonfile = jsonfiles[jsontag]
cmssw = "94X"
storage = "EOS"
rootpath = "/store/user/malhusse/higgs_ntuples/2017"
data_ntuples = []
aux = "Mu27"
filelistdir = "/afs/cern.ch/work/m/malhusse/private/h2mu/filelists"

#for d in data_datasets:
d = "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD"
ntuple = DS.Ntuple(data_datasets[d],
                   json = jsonfile.filename,
                   cmssw = cmssw,
                   storage = "EOS",
                   rootpath = os.path.join(rootpath, "data"),
                   timestamp = None,
                   aux = aux
                   )
data_ntuples.append(ntuple)
print data_ntuples

for ntuple in data_ntuples:
    try:
        filelist_list = S.discoverFileList(ntuple)
        print filelist_list
        filelist = os.path.join(filelistdir, S.buildFileListName(ntuple))
    except Exception as exc:
        continue

    f = open(filelist, "w")
    for x in filelist_list:
        f.write("%s\n" % x)
    f.close()
