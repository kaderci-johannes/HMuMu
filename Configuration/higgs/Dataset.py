#!/usr/bin/python

class Dataset(object):
    def __init__(self, *args, **kwargs):
        """
        name - dataset name as in CMS DAS
        label - shorthand name for this DataSet
        isData - if this is a data or MC
        """
        if len(args)>0:
            Dataset.startup(self, args[0])
            return

        object.__init__(self)
        self.name = kwargs["name"]
        self.isData = kwargs["isData"]
        if 'label' not in kwargs.keys():
            self.label = self.name[1:].replace("/", "__")
        else:
            self.label = kwargs["label"]
        if "plotLabel" not in kwargs.keys():
            self.plotLabel = ""
        else:
            self.plotLabel = kwargs["plotLabel"]
        self.year = kwargs["year"]
        self.globaltag = kwargs["globaltag"]
        if 'test_file' not in kwargs.keys():
            self.test_file = self.label+".files"
        else:
            self.test_file = kwargs["test_file"]

    def startup(self, other):
        object.__init__(self)
        self.name = other.name
        self.label = other.label
        self.isData = other.isData
        self.year = other.year
        self.test_file = other.test_file
        self.globaltag = other.globaltag
        self.plotLabel = other.plotLabel

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        s = "-"*80 + "\n" +\
            "Dataset:" + "\n" +\
            ">>> name="+self.name+"\n" +\
            ">>> label="+self.label+"\n" +\
            ">>> isData="+str(self.isData)+"\n" +\
            ">>> year="+str(self.year)+"\n"+\
            ">>> globaltag="+str(self.globaltag)+"\n"+\
            ">>> test_file="+str(self.test_file)+"\n"+\
            "-"*80 +\
            "\n"
        return s

class MCDataset(Dataset):
    def __init__(self, *args, **kwargs):
        if len(args)>0:
            MCDataset.startup(self, args[0])
            return

        Dataset.__init__(self, **kwargs)
        if "isSignal" not in kwargs.keys():
            self.isSignal = None
        else:
            self.isSignal = kwargs["isSignal"]
        if "initial_cmssw" not in kwargs.keys():
            self.initial_cmssw = None
        else:
            self.initial_cmssw = kwargs["initial_cmssw"]

        if "cross_section" not in kwargs.keys():
            self.cross_section = None
        else:
            self.cross_section = kwargs["cross_section"]

    def __str__(self):
        s = "-"*80 + "\n" +\
            "MCDataset:" + "\n" +\
            ">>> name="+self.name+"\n" +\
            ">>> label="+self.label+"\n" +\
            ">>> isData="+str(self.isData)+"\n" +\
            ">>> year="+str(self.year)+"\n"+\
            ">>> test_file="+str(self.test_file)+"\n"+\
            ">>> isSignal="+str(self.isSignal)+"\n"+\
            ">>> initial_cmssw="+str(self.initial_cmssw)+"\n"+\
            "-"*80 +\
            "\n"
        return s
    def __repr__(self):
        return self.__str__()

    def startup(self, other):
        Dataset.__init__(self, other)
        if hasattr(other, "isSignal"):
            self.isSignal = other.isSignal
        else:
            self.isSignal = None
        if hasattr(other, "initial_cmssw"):
            self.initial_cmssw = other.initial_cmssw
        else:
            self.initial_cmssw = None
        if hasattr(other, "cross_section"):
            self.cross_section=other.cross_section
        else:
            self.cross_section=None

    def buildProcessName(self):
        return self.name.split("/")[1].split("_")[0]

class Ntuple(MCDataset):
    """
    Data/MC Ntuple - the output of CMSSW Ntuple Making
    Location of Ntuples:
    rootpath<storagebased>/DATA.jsontag/label/timestamp/counter/files.root
    rootpath<storagebased>/MC.cmssw/label/timestamp/counter/files.root
    """
    def __init__(self, *args, **kwargs):
        if len(args)>0:
            Ntuple.startup(self, args[0], **kwargs)
            return

        MCDataset.__init__(self, **kwargs)
        self.json = kwargs["json"]
        self.cmssw = kwargs["cmssw"]

        self.timestamp = kwargs["timestamp"]
        self.storage = kwargs["storage"]
        self.rootpath = kwargs["rootpath"]

        if "aux" not in kwargs.keys():
            self.aux=None
        else:
            self.aux = kwargs["aux"]

    def __str__(self):
        s = "-"*80 + "\n" +\
            "Ntuple:" + "\n" +\
            ">>> name="+self.name+"\n" +\
            ">>> label="+self.label+"\n" +\
            ">>> isData="+str(self.isData)+"\n" +\
            ">>> year="+str(self.year)+"\n"+\
            ">>> test_file="+str(self.test_file)+"\n"+\
            ">>> isSignal="+str(self.isSignal)+"\n"+\
            ">>> initial_cmssw="+str(self.initial_cmssw)+"\n"+\
            ">>> globaltag="+str(self.globaltag)+"\n"+\
            ">>> json="+str(self.json)+"\n"+\
            ">>> cmssw="+str(self.cmssw)+"\n"+\
            ">>> timestamp="+str(self.timestamp)+"\n"+\
            ">>> storage="+str(self.storage)+"\n"+\
            ">>> rootpath="+str(self.rootpath)+"\n"+\
            "-"*80 +\
            "\n"
        return s

    def __repr__(self):
        return self.__str__()

    def startup(self, otherds, **kwargs):
        MCDataset.__init__(self, otherds)
        self.json = kwargs["json"]
        self.cmssw = kwargs["cmssw"]

        self.timestamp = kwargs["timestamp"]
        self.storage = kwargs["storage"]
        self.rootpath = kwargs["rootpath"]
        if "aux" not in kwargs.keys():
            self.aux=None
        else:
            self.aux = kwargs["aux"]

class DataResult(Ntuple):
    """
    Data Result of Data Ntuple Processing
    """
    def __init__(self, *args, **kwargs):
        if len(args)>0:
            DataResult.startup(self, args[0], **kwargs)
            return
        Ntuple.__init__(self, **kwargs)
        self.filelist = kwargs["filelist"]

    def startup(self, other, **kwargs):
        Ntuple.__init__(self, other,
            json = other.json,
            cmssw = other.cmssw,
            timestamp = other.timestamp,
            storage=other.storage,
            rootpath=other.rootpath,
            aux=other.aux
        )
        self.filelist = kwargs["filelist"]

class JsonFile(object):
    """
    Represents our Json files
    """
    def __init__(self, **kwargs):
        object.__init__(self)
        self.filename = kwargs["filename"]
        self.intlumi = kwargs["intlumi"]
        self.url = None
        if "url" in kwargs:
            self.url = kwargs["url"]

    def __str__(self):
        s = "-"*80 + "\n" +\
            "JsonFile:" + "\n" +\
            ">>> filename="+str(self.filename)+"\n"+\
            ">>> intlumi="+str(self.intlumi)+"\n"+\
            ">>> url="+str(self.url)+"\n"+\
            "-"*80 +\
            "\n"
        return s

    def __repr__(self):
        return self.__str__()

class MCResult(DataResult):
    """
    MC Result of MC Ntuple Processing
    """
    def __init__(self, *args, **kwargs):
        if len(args)>0:
            MCResult.startup(self, args[0], **kwargs)
            return
        DataResult.__init__(self, **kwargs)
        self.pileupdata = kwargs["pileupdata"]
    def startup(self, other, **kwargs):
        DataResult.__init__(self, other, **kwargs)
        self.pileupdata = kwargs["pileupdata"]

class PileUp(object):
    """
    """
    def __init__(self, **kwargs):
        object.__init__(self)
        self.cross_section = kwargs["cross_section"]
        self.datajson = kwargs["datajson"]

    def __str__(self):
        s = "-"*80 + "\n" + \
            "PileUp: " + "\n" + \
            ">>> cross_section="+self.cross_section + "\n" + \
            ">>> datajson="+self.datajson + "\n" + \
            "-"*80 + \
            "\n"
        return s
    def __repr__(self):
        return self.__str__()

if __name__=="__main__":
    pass
