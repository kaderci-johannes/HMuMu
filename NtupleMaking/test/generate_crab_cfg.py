"""
Crab Config Generator.
- Retrieve the CMSSW Datasets that you need to be processed
- Create and Commit new Ntuples that will be generated with Crab
- Generate the crab cfg files to be submitted
"""
import os,sys, shelve, pickle

#   import the Analysis dependency
if "ANALYSISHOME" not in os.environ.keys():
    raise NameError("Can not find ANALYSISHOME env var")

sys.path.append(os.path.join(os.environ["ANALYSISHOME"], "Configuration", "higgs"))

import Samples as Samples
import Dataset as DS

config_filename = "maker_h2dimuon_cfg_crabtemplate.py"

jsonfiles = Samples.jsonfiles

#   select the datasets to be submitted for grid processing
datasets = []
sets_to_consider = {}
sets_to_consider.update(Samples.data_2017)
sets_to_consider.update(Samples.mc_signal_2017)
#sets_to_consider.update(Samples.mc_signal_2017_extra)
sets_to_consider.update(Samples.mc_background_2017)
#sets_to_consider.update(Samples.mc_background_2017_extra)
for k in sets_to_consider:
    datasets.append(sets_to_consider[k])

#   create the Ntuple objects for all of the datasets
samples = []
for d in datasets:
    if d.isData:
        if d.year == 2016 or d.year == 2017:
            cmssw = "94X"
        elif d.year == 2018:
            cmssw = "102X"
    else:
        cmssw = d.initial_cmssw        
    jsontag = str(d.year)
    storage = "EOS"
    rootpath = "/store/user/malhusse/higgs_ntuples/v3/"
    rootpath += str(d.year)
    if d.isData:
        rootpath+="/data"
    else:
        rootpath+="/mc"
    s = DS.Ntuple(d, 
        json = jsonfiles[jsontag].filename,
        cmssw = cmssw,
        storage = storage,
        rootpath=rootpath,
        timestamp=None,
        aux="Mu27"
    )
    samples.append(s)

#   iterate/generate/commit and create config files
print "Generating Config Files..."
cccc = 0
for s in samples:

    "Generating...."
    print "-"*80
    print s
    
    cfgname = 'dimu_'
    cfgname += s.label.replace(".", "_")
    if s.isData:cfgname += str(jsontag)
    cfgname += '_for_crab.py'
    outfile = open(cfgname, 'w')
    
    #   open the cmssw config template to update
    file = open('templates/%s' % config_filename, 'r')
    for line in file:
        if 's.isData' in line: 
            line = line.replace('s.isData', str(s.isData))
        if 's.globaltag' in line: 
            line = line.replace('s.globaltag', '\"' + s.globaltag + '\"')
        if 's.year' in line:
            line = line.replace('s.year', '\"' +str(s.year) + '\"')
        outfile.write(line)
    
    # close the generated cmssw config file
    outfile.close()
    #   close the cmssw config template
    file.close()
    
    #   open the crab cfg template
    file = open('templates/crab_template.py', 'r')
    if s.isData: 
        #   and open the crab cfg to be generated
        outfile = open('crab_auto_submit_'+s.label.replace(".", "_")+
			'_'+jsontag+'.py', 'w')

    else:
        outfile = open('crab_auto_submit_'+s.label.replace(".", "_")+'.py', 'w')
    
    # read in the template and replace the parameters to make a
    # crab submission file that uses the above cmssw script
    for line in file:
        if 'psetName' in line: 
            line = line.replace('cfgname', cfgname)
        if s.isData and 'FileBased' in line: 
            line = line.replace('FileBased', 'EventAwareLumiBased')
        if s.isData and 'config.Data.lumiMask' in line: 
            line = line.replace('#', '')
            line = line.replace('JSONFILE', "json/"+s.json)
        if "REQUESTNAME" in line:
                line = line.replace("REQUESTNAME", Samples.buildRequestName(s, jsontag) + "__%s" % cccc)
        if 'DATASETTAGNAME' in line: 
            datasettag = Samples.buildDatasetTagName(s)
            line = line.replace('DATASETTAGNAME', datasettag)
        if 's.name' in line: 
            line = line.replace('s.name', s.name)
        if 'ROOTPATH' in line:
            line = line.replace("ROOTPATH", s.rootpath)
        if "JOBUNITS" in line:
            if s.isData:
                line = line.replace("JOBUNITS", "100000")
            else:
                line = line.replace("JOBUNITS", "1")
        outfile.write(line)
    
    outfile.close()
    file.close()
    cccc+=1
