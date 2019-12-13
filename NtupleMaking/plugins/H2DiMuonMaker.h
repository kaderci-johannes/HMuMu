#ifndef NTUPLEMAKER
#define NTUPLEMAKER

#include "HMuMu/NtupleMaking/interface/CommonHeaders.h"
//#include "HMuMu/NtupleMaking/interface/KinematicFitMuonCorrections.h"
//	MY Classes
#include "HMuMu/Core/interface/GenJet.h"
#include "HMuMu/Core/interface/Constants.h"
#include "HMuMu/Core/interface/MET.h"
#include "HMuMu/Core/interface/Track.h"
#include "HMuMu/Core/interface/Event.h"
#include "HMuMu/Core/interface/MetaHiggs.h"
#include "HMuMu/Core/interface/GenParticle.h"
#include "HMuMu/Core/interface/Jet.h"
#include "HMuMu/Core/interface/Muon.h"
#include "HMuMu/Core/interface/Vertex.h"
#include "HMuMu/Core/interface/Electron.h"
#include "HMuMu/Core/interface/Tau.h"
#include "HMuMu/NtupleMaking/data/Roccor/RoccoR.cc"

// classes for json
#include "boost/property_tree/ptree.hpp"
#include "boost/property_tree/json_parser.hpp"

class H2DiMuonMaker : public edm::EDAnalyzer
{
public:
	explicit H2DiMuonMaker(edm::ParameterSet const &);
	~H2DiMuonMaker() {}

	virtual void beginJob();
	virtual void endJob();
	virtual void analyze(edm::Event const &, edm::EventSetup const &);

private:
	bool passHLT(edm::Event const &);
	bool isHLTMatched(uint32_t, edm::Event const &,
					  pat::Muon const &);
	bool passKinCuts(pat::Muon const &);
	double getPFMiniIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
							  const reco::Candidate *ptcl,
							  double r_iso_min, double r_iso_max, double kt_scale,
							  bool use_pfweight, bool charged_only, double rho);

private:
	//	ROOT
	TTree *_tEvents;
	TTree *_tMeta;

	//	Analysis Objects
	analysis::dimuon::MetaHiggs _meta;
	analysis::core::Muons _muons;
	analysis::core::Electrons _electrons;
	analysis::core::Taus _taus;
	analysis::core::Jets _pfjets;
	analysis::core::Vertices _vertices;
	analysis::core::Event _event;
	analysis::core::EventAuxiliary _eaux;
	analysis::dimuon::Auxiliary m_aux;
	analysis::core::MET _met;
	analysis::core::GenJets _genjets;

	//	Input Tags/Tokens
	edm::InputTag _muonToken;
	edm::InputTag _eleToken;
	edm::InputTag _tauToken;
	edm::InputTag _pvToken;
	edm::InputTag _trigResToken;
	edm::InputTag _trigObjToken;
	edm::InputTag _metToken;
	edm::InputTag _jetToken;
	edm::InputTag _rhoToken;
	edm::InputTag _genJetToken;

	/* edm::InputTag _eleVetoToken; */
	/* edm::InputTag _eleLooseToken; */
	/* edm::InputTag _eleMediumToken; */
	/* edm::InputTag _eleTightToken; */
	edm::InputTag _convToken;
	edm::InputTag _bsToken;
	edm::InputTag _metFilterToken;
	edm::InputTag _prunedGenParticlesToken;
	edm::InputTag _packedGenParticlesToken;
	edm::FileInPath roch_file;
	edm::FileInPath btag_file;

	edm::FileInPath muon_isoSF_file;
	edm::FileInPath muon_idSF_file;
	edm::FileInPath muon_trigSF_file;
	TFile *muon_trigSF_root;
	TH2F *muon_trigSF_histo;

	std::string _id_wp_num;  // = "MediumID";
	std::string _id_wp_den;  // = "genTracks";
	std::string _iso_wp_num; // = "LooseRelIso";
	std::string _iso_wp_den; // = "MediumID";

	boost::property_tree::ptree _muon_isoSF_ptree;
	boost::property_tree::ptree _muon_idSF_ptree;

	edm::EDGetTokenT<std::vector<pat::PFParticle>> tokenFSRphotons;

	edm::EDGetTokenT<LHEEventProduct> _lheToken;
	edm::EDGetTokenT<GenEventInfoProduct> _genInfoToken;
	edm::EDGetTokenT<std::vector<PileupSummaryInfo>> _puToken;
	edm::EDGetTokenT<pat::PackedCandidateCollection> _candToken;
 	edm::EDGetTokenT<edm::ValueMap<float> > qg_token;
	 
	edm::Handle<edm::TriggerResults> _hTriggerResults;
	edm::Handle<pat::TriggerObjectStandAloneCollection> _hTriggerObjects;
	edm::Handle<edm::TriggerResults> _hMetFilterResults;
	edm::ESHandle<JetCorrectorParametersCollection> m_hJetCParametersAK4;
	JetCorrectionUncertainty *m_jecuAK4;

	edm::EDGetTokenT<double> prefweight_token;
	edm::EDGetTokenT<double> prefweightup_token;
	edm::EDGetTokenT<double> prefweightdown_token;

	BTagCalibration *calib;
	BTagCalibrationReader *btreader;

	bool _useElectrons;
	bool _useTaus;
};

DEFINE_FWK_MODULE(H2DiMuonMaker);
#endif
