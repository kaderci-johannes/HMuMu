#ifndef NTUPLEMAKER
#define NTUPLEMAKER

#include "HMuMu/NtupleMaking/interface/CommonHeaders.h"

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

class H2DiMuonMaker : public edm::EDAnalyzer
{
	public:
		explicit H2DiMuonMaker(edm::ParameterSet const&);
		~H2DiMuonMaker() {}

		virtual void beginJob();
		virtual void endJob();
		virtual void analyze(edm::Event const&, edm::EventSetup const&);
	private:
		bool passHLT(edm::Event const&);
		bool isHLTMatched(uint32_t, edm::Event const&,
			pat::Muon const&);
		bool passKinCuts(pat::Muon const&,
			edm::Handle<reco::BeamSpot> const&);

	private:
		//	ROOT
		TTree *_tEvents;
		TTree *_tMeta;

		//	Analysis Objects
		analysis::dimuon::MetaHiggs		_meta;
		analysis::core::Muons		_muons; 
        analysis::core::Electrons   _electrons;
        analysis::core::Taus        _taus;
		analysis::core::Jets		_pfjets;
		analysis::core::Vertices	_vertices;
		analysis::core::Event		_event;
		analysis::core::EventAuxiliary		_eaux;
        // analysis::dimuon::Auxiliary m_aux;
		analysis::core::MET			_met;
		analysis::core::GenJets		_genjets;

		//	Input Tags/Tokens
		edm::InputTag _muonToken;
		edm::InputTag _eleToken;
		edm::InputTag _tauToken;
		edm::InputTag _pvToken;
		edm::InputTag _trigResToken;
		edm::InputTag _trigObjToken;
		edm::InputTag _metToken;
		edm::InputTag _jetToken;
		edm::InputTag _genJetToken;
        edm::InputTag _eleVetoToken;
        edm::InputTag _eleLooseToken;
        edm::InputTag _eleMediumToken;
        edm::InputTag _eleTightToken;
        edm::InputTag _convToken;
		edm::InputTag _bsToken;
		edm::Handle<edm::TriggerResults> _hTriggerResults;
		edm::Handle<pat::TriggerObjectStandAloneCollection> _hTriggerObjects;
        // edm::ESHandle<JetCorrectorParametersCollection> m_hJetCParametersAK5, 
            // m_hJetCParametersAK4;
        // JetCorrectionUncertainty *m_jecuAK5;
        // JetCorrectionUncertainty *m_jecuAK4;

};

DEFINE_FWK_MODULE(H2DiMuonMaker);
#endif