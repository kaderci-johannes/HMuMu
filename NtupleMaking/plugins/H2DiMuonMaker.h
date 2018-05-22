#ifndef NTUPLEMAKER
#define NTUPLEMAKER

#include "Analysis/NtupleMaking/interface/CommonHeaders.h"

//	MY Classes
#include "Analysis/Core/interface/GenJet.h"
#include "Analysis/Core/interface/Constants.h"
#include "Analysis/Core/interface/MET.h"
#include "Analysis/Core/interface/Track.h"
#include "Analysis/Core/interface/Event.h"
#include "Analysis/Core/interface/MetaHiggs.h"
#include "Analysis/Core/interface/GenParticle.h"
#include "Analysis/Core/interface/Jet.h"
#include "Analysis/Core/interface/Muon.h"
#include "Analysis/Core/interface/Vertex.h"
#include "Analysis/Core/interface/Electron.h"
#include "Analysis/Core/interface/Tau.h"

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
		edm::InputTag _tagMuons;
		edm::InputTag _tagElectrons;
		edm::InputTag _tagTaus;
		edm::InputTag _tagPV;
		edm::InputTag _tagTriggerResults;
		edm::InputTag _tagTriggerObjects;
		edm::InputTag _tagMET;
		edm::InputTag _tagPFJets;
		edm::InputTag _tagGenJets;
        edm::InputTag _tagElectronCutBasedId_veto;
        edm::InputTag _tagElectronCutBasedId_loose;
        edm::InputTag _tagElectronCutBasedId_medium;
        edm::InputTag _tagElectronCutBasedId_tight;
        edm::InputTag _tagConversions;
		edm::InputTag _tagBS;
		edm::Handle<edm::TriggerResults> _hTriggerResults;
		edm::Handle<pat::TriggerObjectStandAloneCollection> _hTriggerObjects;
        // edm::ESHandle<JetCorrectorParametersCollection> m_hJetCParametersAK5, 
            // m_hJetCParametersAK4;
        // JetCorrectionUncertainty *m_jecuAK5;
        // JetCorrectionUncertainty *m_jecuAK4;

};

DEFINE_FWK_MODULE(H2DiMuonMaker);
#endif