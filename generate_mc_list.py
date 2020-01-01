import os
import sys

sys.path.append(os.path.join(
    os.environ["ANALYSISHOME"], "Configuration", "higgs"))

import Dataset as DS
import Samples as S

year = sys.argv[1]

mc2016 = S.mc_background_2016
mc2016.update(S.mc_signal_2016)

mc2017 = S.mc_background_2017
mc2017.update(S.mc_signal_2017)

mc2018 = S.mc_background_2018
mc2018.update(S.mc_signal_2018)

mc_datasets_dic = {
    "2016": mc2016,
    "2017": mc2017,
    "2018": mc2018
}

cmssw_dic = {
    "2016": "94X",
    "2017": "94X",
    "2018": "102X"
}

cmssw = cmssw_dic[year]

storage = "EOS"
# change this to v6 once the new Trig24 ntuples are done
if year == "2016" or year == "2018":
    rootpath = "/store/user/malhusse/higgs_ntuples/v6/" + year
if year == "2017":
    rootpath = "/store/user/malhusse/higgs_ntuples/v5/" + year

mc_ntuples = []
aux = "Mu27"

filelistdir = "/uscms_data/d3/malhusse/analysis/AnalysisCode/filelists/" + year

for d, v in mc_datasets_dic[year].items():
    print(v.label)
    ntuple = DS.Ntuple(v,
                       json=None,
                       cmssw=cmssw,
                       storage="EOS",
                       rootpath=os.path.join(rootpath, "mc"),
                       timestamp=None,
                       aux=aux
                       )
    mc_ntuples.append(ntuple)

timestamps = []

for ntuple in mc_ntuples:
    try:
        filelist_full = []
        for timestamp in S.buildTimeStamp(ntuple):
            if timestamp in timestamps:
                continue
            else:
                timestamps.append(timestamp)
                filelist_list = S.discoverFileList(ntuple, timestamp)
                filelist = os.path.join(
                    filelistdir, S.buildFileListName(ntuple))
                filelist_full += filelist_list
    except Exception as exc:
        continue

    if filelist_full:
        f = open(filelist, "w")
        for x in filelist_full:
            f.write("%s\n" % x)
        f.close()
