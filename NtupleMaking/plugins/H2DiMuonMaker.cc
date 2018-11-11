/*
 *	Author:
 *	Date:
 *	Description:
 */

#include "HMuMu/NtupleMaking/plugins/H2DiMuonMaker.h"

H2DiMuonMaker::H2DiMuonMaker(edm::ParameterSet const &ps) : _muonToken(ps.getUntrackedParameter<edm::InputTag>("tagMuons")),
															_eleToken(ps.getUntrackedParameter<edm::InputTag>("tagElectrons")),
															_tauToken(ps.getUntrackedParameter<edm::InputTag>("tagTaus")),
															_pvToken(ps.getUntrackedParameter<edm::InputTag>("tagPV")),
															_trigResToken(ps.getUntrackedParameter<edm::InputTag>("tagTriggerResults")),
															_trigObjToken(ps.getUntrackedParameter<edm::InputTag>("tagTriggerObjects")),
															_metToken(ps.getUntrackedParameter<edm::InputTag>("tagMET")),
															_jetToken(ps.getUntrackedParameter<edm::InputTag>("tagJets")),
															_genJetToken(ps.getUntrackedParameter<edm::InputTag>("tagGenJets")),
															_eleVetoToken(ps.getUntrackedParameter<edm::InputTag>("tagElectronCutBasedId_veto")),
															_eleLooseToken(ps.getUntrackedParameter<edm::InputTag>("tagElectronCutBasedId_loose")),
															_eleMediumToken(ps.getUntrackedParameter<edm::InputTag>("tagElectronCutBasedId_medium")),
															_eleTightToken(ps.getUntrackedParameter<edm::InputTag>("tagElectronCutBasedId_tight")),
															_convToken(ps.getUntrackedParameter<edm::InputTag>("tagConversions")),
															_bsToken(ps.getUntrackedParameter<edm::InputTag>("tagBS")),
															_metFilterToken(ps.getUntrackedParameter<edm::InputTag>("tagMetFilterResults")),
															_prunedGenParticlesToken(ps.getUntrackedParameter<edm::InputTag>("tagPrunedGenParticles")),
							    _packedGenParticlesToken(ps.getUntrackedParameter<edm::InputTag>("tagPackedGenParticles")),
							    roch_file(ps.getParameter<edm::FileInPath>("rochesterFile"))
{
	//
	//	init the Trees and create branches
	//
	edm::Service<TFileService> fs;
	_tEvents = fs->make<TTree>("Events", "Events");
	_tMeta = fs->make<TTree>("Meta", "Meta");

	using namespace analysis::core;
	using namespace analysis::dimuon;
	_tEvents->Branch("Muons", (Muons *)&_muons);
	// _tEvents->Branch("CorrectedMuons",(Muons *)&_correctedMuons);
	_tEvents->Branch("Jets", (Jets *)&_pfjets);
	_tEvents->Branch("Vertices", (Vertices *)&_vertices);
	_tEvents->Branch("Event", (Event *)&_event);
	_tEvents->Branch("EventAuxiliary", (EventAuxiliary *)&_eaux);
	_tEvents->Branch("MET", (MET *)&_met);
	_tMeta->Branch("Meta", (MetaHiggs *)&_meta);
	_tEvents->Branch("Auxiliary", &m_aux);

	consumes<pat::MuonCollection>(_muonToken);
	consumes<edm::View<pat::Electron>>(_eleToken);
	consumes<pat::TauCollection>(_tauToken);
	consumes<reco::VertexCollection>(_pvToken);
	consumes<edm::TriggerResults>(_trigResToken);
	consumes<pat::TriggerObjectStandAloneCollection>(_trigObjToken);
	consumes<pat::METCollection>(_metToken);
	consumes<pat::JetCollection>(_jetToken);
	consumes<reco::GenJetCollection>(_genJetToken);
	consumes<edm::ValueMap<bool>>(_eleVetoToken);
	consumes<edm::ValueMap<bool>>(_eleLooseToken);
	consumes<edm::ValueMap<bool>>(_eleMediumToken);
	consumes<edm::ValueMap<bool>>(_eleTightToken);
	consumes<reco::BeamSpot>(_bsToken);
	consumes<edm::TriggerResults>(_metFilterToken);
	consumes<reco::GenParticleCollection>(_prunedGenParticlesToken);
	consumes<pat::PackedGenParticleCollection>(_packedGenParticlesToken);

	_genInfoToken = consumes<GenEventInfoProduct>(edm::InputTag("generator"));
	_lheToken = consumes<LHEEventProduct>(edm::InputTag("externalLHEProducer"));

	mayConsume<reco::ConversionCollection>(_convToken);

	_meta._checkTrigger = ps.getUntrackedParameter<bool>("checkTrigger");
	_meta._isMC = ps.getUntrackedParameter<bool>("isMC");
	_meta._triggerNames = ps.getUntrackedParameter<std::vector<std::string>>(
		"triggerNames");
	_meta._nMuons = ps.getUntrackedParameter<int>("nMuons");
	_meta._isGlobalMuon = ps.getUntrackedParameter<bool>("isGlobalMuon");
	_meta._isTrackerMuon = ps.getUntrackedParameter<bool>("isTrackerMuon");
	_meta._isStandAloneMuon = ps.getUntrackedParameter<bool>("isStandAloneMuon");
	_meta._minPt = ps.getUntrackedParameter<double>("minPt");
	_meta._maxeta = ps.getUntrackedParameter<double>("maxeta");
	_meta._btagNames = ps.getUntrackedParameter<std::vector<std::string>>("btagNames");
	_meta._tauIDNames = ps.getUntrackedParameter<std::vector<std::string>>("tauIDNames");
	_meta._metFilterNames = ps.getUntrackedParameter<std::vector<std::string>>("metFilterNames");
	_useElectrons = ps.getUntrackedParameter<bool>("useElectrons");
	_useTaus = ps.getUntrackedParameter<bool>("useTaus");

	//  additional branching based on flags
	if (_useElectrons)
	{
		_tEvents->Branch("Electrons", (Electrons *)&_electrons);
	}
	if (_useTaus)
	{
		_tEvents->Branch("Taus", (Taus *)&_taus);
	}
	//	additional branching for MC
	if (_meta._isMC)
	{
		_tEvents->Branch("GenJets", (GenJets *)&_genjets);
	}
}

void H2DiMuonMaker::beginJob()
{
}

void H2DiMuonMaker::endJob()
{
  _tMeta->Fill();
}

void H2DiMuonMaker::analyze(edm::Event const &e, edm::EventSetup const &esetup)
{
	// count total
	_meta._nEventsProcessed++;

	//
	//	Reset all objects or clear the containers
	//
	_event.reset();
	_eaux.reset();
	_met.reset();

	_vertices.clear();
	_pfjets.clear();
	_genjets.clear();
	_muons.clear();
	// _correctedMuons.clear();
	_electrons.clear();
	_taus.clear();
	_genjets.clear();
	m_aux.reset();

	//
	//	For MC
	//
	if (!_meta._isMC)
		_meta._sumEventWeights += 1;
	else
	{
		//
		//	MC Weights
		//
		edm::Handle<GenEventInfoProduct> hGenEvtInfo;
		e.getByToken(_genInfoToken, hGenEvtInfo);
		_eaux._genWeight = (hGenEvtInfo->weight() > 0) ? 1 : -1;
		_meta._sumEventWeights += _eaux._genWeight;

		//
		// LHE Event Product - to get the total - HT
		//
		edm::Handle<LHEEventProduct> hLHE;
		e.getByToken(_lheToken, hLHE);
		if (!hLHE.isValid())
		{
			std::cout << " LHE Event Product is not found" << std::endl;
		}
		else
		{
			for (int i = 0; i < hLHE->hepeup().NUP; i++)
			{
				int pdgId = abs(hLHE->hepeup().IDUP[i]);
				int status = hLHE->hepeup().ISTUP[i];
				int mother1_idx = hLHE->hepeup().MOTHUP[i].first;
				int mother2_idx = hLHE->hepeup().MOTHUP[i].second;
				int mom1id = mother1_idx == 0 ? 0 : abs(hLHE->hepeup().IDUP[mother1_idx - 1]);
				int mom2id = mother2_idx == 0 ? 0 : abs(hLHE->hepeup().IDUP[mother2_idx - 1]);
				double px = (hLHE->hepeup().PUP[i])[0];
				double py = (hLHE->hepeup().PUP[i])[1];
				double pt = sqrt(px * px + py * py);

				// select properly
				if (status == 1 && (pdgId < 6 || pdgId == 21) && mom1id != 6 && mom2id != 6 &&
					abs(mom1id - 24) > 1 && abs(mom2id - 24) > 1)
				{
					m_aux.m_numHT++;
					m_aux.m_ptSum += pt;
				}
			}
		}
		//
		//	PILEUP
		//	look into this - Mo 9/17/18
		//
		// edm::Handle<std::vector< PileupSummaryInfo > > hPUInfo;
		// e.getByLabel(_tokPU, hPUInfo);
		// std::vector<PileupSummaryInfo>::const_iterator pus;
		// for (pus=hPUInfo->begin(); pus!=hPUInfo->end(); ++pus)
		// {
		// 	int bx = pus->getBunchCrossing();
		// 	if (bx==0)
		// 		_eaux._nPU = pus->getTrueNumInteractions();
		// }

		//
		//	Gen Jet
		//
		edm::Handle<reco::GenJetCollection> hGenJets;
		e.getByLabel(_genJetToken, hGenJets);
		if (!hGenJets.isValid())
		{
			std::cout << "Gen Jet Product is not found" << std::endl;
		}
		else
		{
			reco::GenJetCollection sortedGenJets = (*hGenJets);
			sort(sortedGenJets.begin(), sortedGenJets.end(),
				 [](reco::GenJet it, reco::GenJet jt) -> bool { return it.pt() > jt.pt(); });
			int n = 0;
			for (uint32_t i = 0; i < sortedGenJets.size(); i++)
			{
				analysis::core::GenJet genjet;
				genjet._px = sortedGenJets[i].px();
				genjet._py = sortedGenJets[i].py();
				genjet._pz = sortedGenJets[i].pz();
				genjet._py = sortedGenJets[i].pt();
				genjet._eta = sortedGenJets[i].eta();
				genjet._phi = sortedGenJets[i].phi();
				genjet._mass = sortedGenJets[i].mass();
				genjet._charge = sortedGenJets[i].charge();
				_genjets.push_back(genjet);
				n++;
			}
		}
	}

	//
	//	HLT
	//	- Skip the event if HLT has not fired
	//
	e.getByLabel(_trigResToken, _hTriggerResults);
	e.getByLabel(_trigObjToken, _hTriggerObjects);
	if (!_hTriggerResults.isValid())
	{
		std::cout << "Trigger Results Product is not found" << std::endl;
		return;
	}
	if (!_hTriggerObjects.isValid())
	{
		std::cout << "Trigger Objects Product is not found" << std::endl;
		return;
	}
	if (_meta._checkTrigger)
		if (!passHLT(e))
			return;

	// MetFilterResults
	e.getByLabel(_metFilterToken, _hMetFilterResults);
	if (!_hMetFilterResults.isValid())
	{
		std::cout << " met Filter Results Product not found" << std::endl;
	}
	else
	{
		edm::TriggerNames const &metNames = e.triggerNames(*_hMetFilterResults);

		for (unsigned int i = 0, n = _hMetFilterResults->size(); i < n; ++i)
		{
			std::string filterName = metNames.triggerName(i);
			for (std::vector<std::string>::const_iterator dit = _meta._metFilterNames.begin(); dit != _meta._metFilterNames.end(); ++dit)
				if (*dit == filterName)
				{
					_eaux._metFilterBits[filterName] = _hMetFilterResults->accept(i);
					_eaux._passedMetFilters = _eaux._passedMetFilters && _hMetFilterResults->accept(i);
				}
		}
	}

	//
	//	Event Info
	//
	_event._run = e.id().run();
	_event._lumi = e.id().luminosityBlock();
	_event._event = e.id().event();
	_event._bx = e.bunchCrossing();
	_event._orbit = e.orbitNumber();

	//
	//	Vertices
	//
	edm::Handle<reco::VertexCollection> hVertices;
	e.getByLabel(_pvToken, hVertices);
	if (!hVertices.isValid())
		std::cout << "VertexCollection Product is not found" << std::endl;
	else
	{
		for (reco::VertexCollection::const_iterator it = hVertices->begin();
			 it != hVertices->end(); ++it)
		{
			analysis::core::Vertex vtx;
			if (!it->isValid())
				vtx._isValid = 0;
			else
			{
				vtx._isValid = 1;
				vtx._x = it->position().X();
				vtx._y = it->position().Y();
				vtx._z = it->position().Z();
				vtx._xerr = it->xError();
				vtx._yerr = it->yError();
				vtx._zerr = it->zError();
				vtx._chi2 = it->chi2();
				vtx._ndf = it->ndof();
				vtx._normChi2 = it->normalizedChi2();
			}
			_vertices.push_back(vtx);
		}
	}

	//
	//	Beam Spot
	//
	edm::Handle<reco::BeamSpot> hBS;
	e.getByLabel(_bsToken, hBS);

	//
	//	MET
	//
	edm::Handle<std::vector<pat::MET>> hMET;
	e.getByLabel(_metToken, hMET);
	if (!hMET.isValid())
	{
		std::cout << "MET Product is not found" << std::endl;
	}
	else
	{
		_met._px = (*hMET)[0].px();
		_met._py = (*hMET)[0].py();
		_met._pt = (*hMET)[0].pt();
		_met._phi = (*hMET)[0].phi();
		_met._sumEt = (*hMET)[0].sumEt();
	}

	//
	//	Jet
	//
	edm::Handle<std::vector<pat::Jet>> hJets;
	e.getByLabel(_jetToken, hJets);
	if (!hJets.isValid())
	{
		std::cout << "Jet Product is not found" << std::endl;
	}
	else
	{
		for (uint32_t i = 0; i < hJets->size(); i++)
		{
			if (i == 10)
				break;

			const pat::Jet &jet = hJets->at(i);
			analysis::core::Jet myjet;
			myjet._px = jet.px();
			myjet._py = jet.py();
			myjet._pz = jet.pz();
			myjet._pt = jet.pt();
			myjet._eta = jet.eta();
			myjet._phi = jet.phi();
			myjet._mass = jet.mass();
			myjet._partonFlavour = jet.partonFlavour();

			myjet._chf = jet.chargedHadronEnergyFraction();
			myjet._nhf = jet.neutralHadronEnergyFraction();
			myjet._cef = jet.chargedEmEnergyFraction();
			myjet._nef = jet.neutralEmEnergyFraction();
			myjet._muf = jet.muonEnergyFraction();
			myjet._hfhf = jet.HFHadronEnergyFraction();
			myjet._hfef = jet.HFEMEnergyFraction();

			myjet._cm = jet.chargedMultiplicity();
			myjet._nm = jet.neutralMultiplicity();
			myjet._chm = jet.chargedHadronMultiplicity();
			myjet._nhm = jet.neutralHadronMultiplicity();
			myjet._cem = jet.electronMultiplicity();
			myjet._nem = jet.photonMultiplicity();
			myjet._mum = jet.muonMultiplicity();
			myjet._hfhm = jet.HFHadronMultiplicity();
			myjet._hfem = jet.HFEMMultiplicity();

			myjet._jecu = -1.;
			myjet._jecf = jet.jecFactor("Uncorrected");
			myjet._puid = jet.userFloat("pileupJetId:fullDiscriminant");
			myjet._fullid = jet.userInt("pileupJetId:fullId");

			//  b-tagging information
			float btagDisc = 0.0;
			for (std::vector<std::string>::const_iterator btt = _meta._btagNames.begin();
				 btt != _meta._btagNames.end(); ++btt)
			{
				btagDisc += jet.bDiscriminator(*btt);
			}
			myjet._btag.push_back(btagDisc);

			// energy correction uncertainty -- look into this Mo 5/2018
			// m_jecuAK5->setJetEta(jet.eta());
			// m_jecuAK4->setJetEta(jet.eta());
			// m_jecuAK5->setJetPt(jet.pt());
			// m_jecuAK4->setJetPt(jet.pt());

			// double uncAK5 = m_jecuAK5->getUncertainty(true);
			// double uncAK4 = m_jecuAK4->getUncertainty(true);

			// double pt_upAK5 = jet.pt()*(1 + uncAK5);
			// double pt_downAK5 = jet.pt()*(1 - uncAK5);
			// double pt_upAK4 = jet.pt()*(1 + uncAK4);
			// double pt_downAK4 = jet.pt()*(1 - uncAK4);

			// myjet._uncAK5 = uncAK5;
			// myjet._uncAK4 = uncAK4;
			// myjet._pt_upAK5 = pt_upAK5;
			// myjet._pt_upAK4 = pt_upAK4;
			// myjet._pt_downAK5 = pt_downAK5;
			// myjet._pt_downAK4 = pt_downAK4;

			//	matche gen jet
			const reco::GenJet *genJet = jet.genJet();
			if (genJet != NULL)
			{
				myjet._genMatched = true;
				myjet._genjet._px = genJet->px();
				myjet._genjet._py = genJet->py();
				myjet._genjet._pz = genJet->pz();
				myjet._genjet._pt = genJet->pt();
				myjet._genjet._eta = genJet->eta();
				myjet._genjet._phi = genJet->phi();
				myjet._genjet._mass = genJet->mass();
				myjet._genemf = genJet->emEnergy() / genJet->energy();
				myjet._genhadf = genJet->hadEnergy() / genJet->energy();
				myjet._geninvf = genJet->invisibleEnergy() / genJet->energy();
				myjet._genauxf = genJet->auxiliaryEnergy() / genJet->energy();
			}
			else
				myjet._genMatched = false;

			_pfjets.push_back(myjet);
		}
	}

	//
	//  Electrons
	//
	if (_useElectrons)
	{
		edm::Handle<edm::ValueMap<bool>> hId_veto, hId_loose, hId_medium, hId_tight;
		e.getByLabel(_eleVetoToken, hId_veto);
		e.getByLabel(_eleLooseToken, hId_loose);
		e.getByLabel(_eleMediumToken, hId_medium);
		e.getByLabel(_eleTightToken, hId_tight);

		edm::Handle<edm::View<pat::Electron>> hElectrons;
		e.getByLabel(_eleToken, hElectrons);

		edm::Handle<reco::ConversionCollection> hConversions;
		e.getByLabel(_convToken, hConversions);

		for (size_t i = 0; i < hElectrons->size(); ++i)
		{
			auto const ele = hElectrons->ptrAt(i);
			//  >= 10GeV for electrons
			if (ele->pt() < 10)
				continue;

			analysis::core::Electron mye;
			mye._charge = ele->charge();
			mye._pt = ele->pt();
			mye._eta = ele->eta();
			mye._phi = ele->phi();

			reco::GsfTrackRef theTrack = ele->gsfTrack();
			mye._dz = theTrack->dz(hBS->position());
			mye._sumChargedHadronPt = ele->pfIsolationVariables().sumChargedHadronPt;
			mye._sumNeutralHadronEt = ele->pfIsolationVariables().sumNeutralHadronEt;
			mye._sumPhotonEt = ele->pfIsolationVariables().sumPhotonEt;
			mye._sumPUPt = ele->pfIsolationVariables().sumPUPt;
			mye._sumChargedParticlePt = ele->pfIsolationVariables().sumChargedParticlePt;
			mye._isPF = ele->isPF();
			mye._convVeto = !ConversionTools::hasMatchedConversion(*ele,
																   hConversions, hBS->position());

			// cut based id

			bool id_veto = (*hId_veto)[ele];
			mye._ids.push_back(id_veto);
			bool id_loose = (*hId_loose)[ele];
			mye._ids.push_back(id_loose);
			bool id_medium = (*hId_medium)[ele];
			mye._ids.push_back(id_medium);
			bool id_tight = (*hId_tight)[ele];
			mye._ids.push_back(id_tight);

			_electrons.push_back(mye);
		}
	}

	//
	//  Taus
	//

	if (_useTaus)
	{
		edm::Handle<pat::TauCollection> hTaus;
		e.getByLabel(_tauToken, hTaus);
		for (pat::TauCollection::const_iterator it = hTaus->begin();
			 it != hTaus->end(); ++it)
		{
			//  >=20GeV for Taus only
			if (it->pt() < 20)
				continue;

			analysis::core::Tau mytau;
			mytau._pt = it->pt();
			mytau._eta = it->eta();
			mytau._phi = it->phi();
			mytau._isPF = it->isPFTau();
			mytau._charge = it->charge();

			for (std::vector<std::string>::const_iterator tt = _meta._tauIDNames.begin();
				 tt != _meta._tauIDNames.end(); ++tt)
				mytau._ids.push_back(it->tauID(*tt));

			_taus.push_back(mytau);
		}
	}

	//
	//	Muons
	//
	edm::Handle<pat::MuonCollection> hMuons;
	e.getByLabel(_muonToken, hMuons);
	pat::MuonCollection muonsSelected;

	// gen particles for muon rochester corrections

	edm::Handle<reco::GenParticleCollection> hGenParticles;
	if (_meta._isMC)
		e.getByLabel(_prunedGenParticlesToken, hGenParticles);
	// initilize the rochester correction thing
	//	edm::FileInPath fp = "HMuMu/NtupleMaking/Roccor/RoccoR2017.txt";
	//		std::cout << roch_file.location() << std::endl;
	//	std::cout << roch_file.fullPath() << std::endl;
		//	return;
	RoccoR rc;
	//	rc.init(edm::FileInPath("/afs/cern.ch/work/m/malhusse/private/h2mu/CMSSW_9_4_9_cand2/src/HMuMu/NtupleMaking/Roccor/RoccoR2017.txt").fullPath());
       	rc.init(roch_file.fullPath().c_str());
		//
	//	Muon Pre-Selection
	//
	for (pat::MuonCollection::const_iterator it = hMuons->begin();
		 it != hMuons->end(); ++it)
	{
		//	global vs tracker vs standalone
		if (!it->isGlobalMuon() && _meta._isGlobalMuon)
			continue;
		if (!it->isTrackerMuon() && _meta._isTrackerMuon)
			continue;
		if (!it->isGlobalMuon() && !it->isTrackerMuon())
			continue;

		//	kinematic
		if (!passKinCuts(*it))
			continue;

		muonsSelected.push_back(*it);
	}

	//	skip the event if the #muons is not what we need
	if (muonsSelected.size() < _meta._nMuons)
		return;

	//
	//	Muon Pre-Selection 2 based on #muons @1
	//
	// if (muonsSelected.size() == 0 || muonsSelected.size() == 1) // 0 muons
	// return;
	else // 2 or more muons
	{
		// make sure Muons are sorted..
		sort(muonsSelected.begin(), muonsSelected.end(), [](pat::Muon it, pat::Muon jt) -> bool { return it.pt() > jt.pt(); });
		for (pat::MuonCollection::const_iterator it = muonsSelected.begin();
			 it != muonsSelected.end(); ++it)
		{
			pat::Muon mu1 = *it;
			analysis::core::Muon _muon1;

			double isovar1 = mu1.isolationR03().sumPt;
			isovar1 += mu1.isolationR03().hadEt;
			isovar1 /= mu1.pt();

			_muon1._relCombIso = isovar1;
			_muon1._trackIsoSumPt = mu1.isolationR03().sumPt;
			_muon1._trackIsoSumPtCorr = mu1.isolationR03().sumPt;

			_muon1._isPF = mu1.isPFMuon();
			if (mu1.isPFMuon())
			{
				reco::Candidate::LorentzVector pfm = mu1.pfP4();
				_muon1._pt = pfm.Pt();
				_muon1._eta = pfm.Eta();
				_muon1._phi = pfm.Phi();
				_muon1._sumChargedHadronPtR03 =
					mu1.pfIsolationR03().sumChargedHadronPt;
				_muon1._sumChargedParticlePtR03 =
					mu1.pfIsolationR03().sumChargedParticlePt;
				_muon1._sumNeutralHadronEtR03 =
					mu1.pfIsolationR03().sumNeutralHadronEt;
				_muon1._sumPhotonEtR03 = mu1.pfIsolationR03().sumPhotonEt;
				_muon1._sumPUPtR03 = mu1.pfIsolationR03().sumPUPt;
				_muon1._sumChargedHadronPtR04 =
					mu1.pfIsolationR04().sumChargedHadronPt;
				_muon1._sumChargedParticlePtR04 =
					mu1.pfIsolationR04().sumChargedParticlePt;
				_muon1._sumNeutralHadronEtR04 =
					mu1.pfIsolationR04().sumNeutralHadronEt;
				_muon1._sumPhotonEtR04 = mu1.pfIsolationR04().sumPhotonEt;
				_muon1._sumPUPtR04 = mu1.pfIsolationR04().sumPUPt;
			}

			//	fill the muon1 information
			_muon1._isGlobal = mu1.isGlobalMuon();
			_muon1._isTracker = mu1.isTrackerMuon();
			_muon1._isStandAlone = mu1.isStandAloneMuon();
			reco::Track track1;
			if (mu1.isGlobalMuon())
				track1 = *(mu1.globalTrack());
			else if (mu1.isTrackerMuon())
				track1 = *(mu1.innerTrack());
			else
				continue;

			_muon1._charge = mu1.charge();
			_muon1._pt = mu1.pt();
			_muon1._pterr = track1.ptError();
			_muon1._eta = mu1.eta();
			_muon1._phi = mu1.phi();
			if (mu1.isTrackerMuon())
			{
				_muon1._track._pt = mu1.innerTrack()->pt();
				_muon1._track._pterr = mu1.innerTrack()->ptError();
				_muon1._track._eta = mu1.innerTrack()->eta();
				_muon1._track._phi = mu1.innerTrack()->phi();
			}
			_muon1._normChi2 = track1.normalizedChi2();
			_muon1._d0BS = track1.dxy(hBS->position());
			_muon1._dzBS = track1.dz(hBS->position());
			reco::Vertex bestVtx1;
			for (reco::VertexCollection::const_iterator vt = hVertices->begin();
				 vt != hVertices->end(); ++vt)
			{
				if (!vt->isValid())
					continue;
				_muon1._d0PV = track1.dxy(vt->position());
				_muon1._dzPV = track1.dz(vt->position());
				bestVtx1 = *vt;
				break;
			}
			_muon1._isTight = muon::isTightMuon(mu1, bestVtx1);
			_muon1._isMedium = muon::isMediumMuon(mu1);
			_muon1._isLoose = muon::isLooseMuon(mu1);
			_muon1._nTLs =
				mu1.innerTrack()->hitPattern().trackerLayersWithMeasurement();
			_muon1._nPLs =
				mu1.innerTrack()->hitPattern().pixelLayersWithMeasurement();
			_muon1._nSLs =
				mu1.innerTrack()->hitPattern().stripLayersWithMeasurement();

			_muon1._vfrTrk = mu1.innerTrack()->validFraction();
			_muon1._nvMHits = track1.hitPattern().numberOfValidMuonHits();
			_muon1._nvPHits =
				mu1.innerTrack()->hitPattern().numberOfValidPixelHits();
			_muon1._nvTHits =
				mu1.innerTrack()->hitPattern().numberOfValidTrackerHits();
			_muon1._nvSHits =
				mu1.innerTrack()->hitPattern().numberOfValidStripHits();
			_muon1._nSegMts = mu1.numberOfMatches();
			_muon1._nMtsStations = mu1.numberOfMatchedStations();
			_muon1._eIso = mu1.isolationR03().emEt;
			_muon1._hIso = mu1.isolationR03().hadEt;
			_muon1._segmentCompatibility = muon::segmentCompatibility(mu1);
			_muon1._combinedQChi2LocalPosition =
				mu1.combinedQuality().chi2LocalPosition;
			_muon1._combinedQTrkKink = mu1.combinedQuality().trkKink;
			for (uint32_t i = 0; i < _meta._triggerNames.size(); i++)
			{
				bool match = isHLTMatched(i, e, mu1);
				_muon1._isHLTMatched.push_back(match);
			}

			// Apply Rochester Correction Here?

			double muSF = 1.0;
			double genPT = -1.0;
			// double minDR = 1.0;

			if (_meta._isMC && hGenParticles.isValid())
			{
				for (auto genPar_it = hGenParticles->begin(); genPar_it != hGenParticles->end(); ++genPar_it)
				{
					if (fabs(genPar_it->pdgId()) != 13)
						continue;
					if (!genPar_it->fromHardProcessFinalState())
						continue;
					if (genPar_it->charge() != _muon1._charge)
						continue;
					double dR = deltaR(genPar_it->eta(), genPar_it->phi(), _muon1._eta, _muon1._phi);
					if (dR > 0.005)
						continue;
					genPT = genPar_it->pt();
				}
			}

			float f_rand = gRandom->Rndm();
			if (!_meta._isMC)
				muSF = rc.kScaleDT(_muon1._charge, _muon1._pt, _muon1._eta, _muon1._phi, 0, 0);
			else if (_meta._isMC && genPT > 0.0)
				muSF = rc.kSpreadMC(_muon1._charge, _muon1._pt, _muon1._eta, _muon1._phi, genPT, 0, 0);
			else if (_meta._isMC && genPT <= 0.0)
				muSF = rc.kSmearMC(_muon1._charge, _muon1._pt, _muon1._eta, _muon1._phi, _muon1._nTLs, f_rand, 0, 0);
			_muon1._SF = muSF;
			_muon1._corrPT = muSF * _muon1._pt;
			_muons.push_back(_muon1);
		}
	}

	//
	//	Dump objects to The ROOT Tree - ONLY after passing all the cuts
	//
	_tEvents->Fill();
}

//
//	true - passes HLT selections
//	false - doesn't pass
//
bool H2DiMuonMaker::passHLT(edm::Event const &e)
{
	const boost::regex re("_v[0-9]+");
	edm::TriggerNames const &triggerNames = e.triggerNames(*_hTriggerResults);

	bool pass = false;
	for (uint32_t i = 0; i < _hTriggerResults->size(); i++)
	{
		std::string triggerName = triggerNames.triggerName(i);
		std::string tstripped = boost::regex_replace(triggerName, re, "",
													 boost::match_default | boost::format_sed);
		for (std::vector<std::string>::const_iterator dit =
				 _meta._triggerNames.begin();
			 dit != _meta._triggerNames.end(); ++dit)
			if (*dit == tstripped)
			{
				if (_hTriggerResults->accept(i))
				{
					_eaux._hasHLTFired.push_back(true);
					pass = true;
				}
				else
					_eaux._hasHLTFired.push_back(false);
			}
	}

	return pass;
}

//
//	true - matched
//	false - didn't match
//
bool H2DiMuonMaker::isHLTMatched(uint32_t itrigger, edm::Event const &e,
								 pat::Muon const &mu)
{
	const boost::regex re("_v[0-9]+");
	edm::TriggerNames const &triggerNames = e.triggerNames(*_hTriggerResults);
	for (uint32_t i = 0; i < _hTriggerResults->size(); i++)
	{
		std::string triggerName = triggerNames.triggerName(i);
		std::string tstripped = boost::regex_replace(triggerName, re, "",
													 boost::match_default | boost::format_sed);
		if (_meta._triggerNames[itrigger] == tstripped &&
			_hTriggerResults->accept(i))
		{
			for (pat::TriggerObjectStandAloneCollection::const_iterator it =
					 _hTriggerObjects->begin();
				 it != _hTriggerObjects->end(); ++it)
			{
				pat::TriggerObjectStandAlone tmp(*it);
				tmp.unpackPathNames(triggerNames);
				bool right = tmp.hasPathName(triggerName, true, true);
				if (right && (deltaR(tmp, mu) < 0.1))
					return true;
			}
		}
	}

	return false;
}

//
//	true - passes Kinematic Cuts
//	false - doesn't pass
//
bool H2DiMuonMaker::passKinCuts(pat::Muon const &muon)
{
	reco::Track track;
	if (muon.isGlobalMuon())
		track = *(muon.globalTrack());
	else if (muon.isTrackerMuon())
		track = *(muon.innerTrack());
	else
		return false;

	if (muon.pt() < _meta._minPt)
		return false;
	if (fabs(muon.eta()) > _meta._maxeta)
		return false;

	return true;
}
