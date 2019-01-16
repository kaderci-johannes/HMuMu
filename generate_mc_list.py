import os
import sys
sys.path.append(os.path.join(
os.environ["ANALYSISHOME"], "Configuration", "higgs"))
import Samples as S
import Dataset as DS

bkg_datasets = S.mc_background_2017
sig_datasets = S.mc_signal_2017

cmssw = "94X"
storage = "EOS"
rootpath = "/store/user/malhusse/higgs_ntuples/2017v2"
mc_ntuples = []
aux = "Mu27"
filelistdir = "/uscms/home/malhusse/nobackup/build/AnalysisCode/filelistsV2"

for d in bkg_datasets:
    ntuple = DS.Ntuple(bkg_datasets[d],
                       json = None,
                       cmssw = bkg_datasets[d].initial_cmssw,
                       storage = "EOS",
                       rootpath = os.path.join(rootpath, "mc"),
                       timestamp = None,
                       aux = aux
                       )
    mc_ntuples.append(ntuple)

for dd in sig_datasets:
    ntuple = DS.Ntuple(sig_datasets[dd],
                       json = None,
                       cmssw = sig_datasets[dd].initial_cmssw,
                       storage = "EOS",
                       rootpath = os.path.join(rootpath, "mc"),
                       timestamp = None,
                       aux = aux
                       )
    mc_ntuples.append(ntuple)

for ntuple in mc_ntuples:
    print ntuple
    try:
        filelist_list = S.discoverFileList(ntuple)
        filelist = os.path.join(filelistdir, S.buildFileListName(ntuple))
   #     print filelist
    except Exception as exc:
        continue

    if filelist_list:
        print "create filelist"
        f = open(filelist, "w")
        for x in filelist_list:
            f.write("%s\n" % x)
        f.close()
