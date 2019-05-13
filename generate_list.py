year = "2018"

import os
import sys
sys.path.append(os.path.join(
os.environ["ANALYSISHOME"], "Configuration", "higgs"))
import Samples as S
import Dataset as DS

data_datasets_dic = {
    "2016": S.data_2016,
    "2017": S.data_2017,
    "2018": S.data_2018
}

cmssw_dic = {
    "2016": "94X",
    "2017": "94X",
    "2018": "102X"
}

jsonfiles = S.jsonfiles
jsonfile = jsonfiles[year]

cmssw = cmssw_dic[year]

storage = "EOS"
rootpath = "/store/user/malhusse/higgs_ntuples/final/" + year
print(rootpath)

data_ntuples = []
aux = "Mu27"

filelistdir = "/uscms_data/d3/malhusse/analysis/AnalysisCode/filelists/" + year

for d, v in data_datasets_dic[year].items():
    # print(d)
    # print(v.label)
    # print(v.aux)
    ntuple = DS.Ntuple(v,
                       json = jsonfile.filename,
                       cmssw = cmssw,
                       storage = storage,
                       rootpath = os.path.join(rootpath, "data"),
                       timestamp = None,
                       aux = aux
                       )
    data_ntuples.append(ntuple)
# print data_ntuples

timestamps = []

for ntuple in data_ntuples:
    try:
        for timestamp in S.buildTimeStamp(ntuple):
            if timestamp in timestamps:
                continue
            else:
                timestamps.append(timestamp)
                filelist_list = S.discoverFileList(ntuple, timestamp)
                filelist = os.path.join(filelistdir, S.buildFileListName(ntuple))
    except Exception as exc:
        continue

    f = open(filelist, "w")
    for x in filelist_list:
        f.write("%s\n" % x)
    f.close()
