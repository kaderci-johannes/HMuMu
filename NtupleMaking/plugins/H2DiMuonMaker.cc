/*
 *	Author: Mohammmad
 */

#include "HMuMu/NtupleMaking/plugins/H2DiMuonMaker.h"
// #include "HMuMu/NtupleMaking/interface/KinematicFitMuonCorrections.h"

H2DiMuonMaker::H2DiMuonMaker(edm::ParameterSet const &ps) : _muonToken(ps.getUntrackedParameter<edm::InputTag>("tagMuons")),
                                                            _eleToken(ps.getUntrackedParameter<edm::InputTag>("tagElectrons")),
                                                            _tauToken(ps.getUntrackedParameter<edm::InputTag>("tagTaus")),
                                                            _pvToken(ps.getUntrackedParameter<edm::InputTag>("tagPV")),
                                                            _trigResToken(ps.getUntrackedParameter<edm::InputTag>("tagTriggerResults")),
                                                            _trigObjToken(ps.getUntrackedParameter<edm::InputTag>("tagTriggerObjects")),
                                                            _metToken(ps.getUntrackedParameter<edm::InputTag>("tagMET")),
                                                            _jetToken(ps.getUntrackedParameter<edm::InputTag>("tagJets")),
                                                            _rhoToken(ps.getUntrackedParameter<edm::InputTag>("tagRho")),
                                                            _genJetToken(ps.getUntrackedParameter<edm::InputTag>("tagGenJets")),
                                                            _convToken(ps.getUntrackedParameter<edm::InputTag>("tagConversions")),
                                                            _bsToken(ps.getUntrackedParameter<edm::InputTag>("tagBS")),
                                                            _metFilterToken(ps.getUntrackedParameter<edm::InputTag>("tagMetFilterResults")),
                                                            _prunedGenParticlesToken(ps.getUntrackedParameter<edm::InputTag>("tagPrunedGenParticles")),
                                                            _packedGenParticlesToken(ps.getUntrackedParameter<edm::InputTag>("tagPackedGenParticles")),
                                                            roch_file(ps.getParameter<edm::FileInPath>("rochesterFile")),
                                                            btag_file(ps.getParameter<edm::FileInPath>("btagFile")),
                                                            muon_isoSF_file(ps.getParameter<edm::FileInPath>("muonIsoFile")),
                                                            muon_idSF_file(ps.getParameter<edm::FileInPath>("muonIdFile")),
                                                            muon_trigSF_file(ps.getParameter<edm::FileInPath>("muonTrigFile")),
                                                            _id_wp_num(ps.getParameter<std::string>("muon_id_sf_wp_num")),
                                                            _id_wp_den(ps.getParameter<std::string>("muon_id_sf_wp_den")),
                                                            _iso_wp_num(ps.getParameter<std::string>("muon_iso_sf_wp_num")),
                                                            _iso_wp_den(ps.getParameter<std::string>("muon_iso_sf_wp_den"))

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
    _tEvents->Branch("Jets", (Jets *)&_pfjets);
    _tEvents->Branch("Vertices", (Vertices *)&_vertices);
    _tEvents->Branch("Event", (Event *)&_event);
    _tEvents->Branch("EventAuxiliary", (EventAuxiliary *)&_eaux);
    _tEvents->Branch("MET", (MET *)&_met);
    _tMeta->Branch("Meta", (MetaHiggs *)&_meta);
    _tEvents->Branch("Auxiliary", &m_aux);

    consumes<pat::MuonCollection>(_muonToken);
    consumes<pat::ElectronCollection>(_eleToken);
    consumes<pat::TauCollection>(_tauToken);
    consumes<reco::VertexCollection>(_pvToken);
    consumes<edm::TriggerResults>(_trigResToken);
    consumes<pat::TriggerObjectStandAloneCollection>(_trigObjToken);
    consumes<pat::METCollection>(_metToken);
    consumes<pat::JetCollection>(_jetToken);
    consumes<double>(_rhoToken);
    consumes<reco::GenJetCollection>(_genJetToken);
    // consumes<edm::ValueMap<bool>>(_eleVetoToken);
    // consumes<edm::ValueMap<bool>>(_eleLooseToken);
    // consumes<edm::ValueMap<bool>>(_eleMediumToken);
    // consumes<edm::ValueMap<bool>>(_eleTightToken);
    consumes<reco::BeamSpot>(_bsToken);
    consumes<edm::TriggerResults>(_metFilterToken);
    consumes<reco::GenParticleCollection>(_prunedGenParticlesToken);
    consumes<pat::PackedGenParticleCollection>(_packedGenParticlesToken);


    _genInfoToken = consumes<GenEventInfoProduct>(edm::InputTag("generator"));
    _lheToken = consumes<LHEEventProduct>(edm::InputTag("externalLHEProducer"));
    _puToken = consumes<std::vector<PileupSummaryInfo>>(edm::InputTag("slimmedAddPileupInfo"));
    tokenFSRphotons = consumes<std::vector<pat::PFParticle>>(edm::InputTag("FSRRecovery", "selectedFSRphotons"));
    _candToken = consumes<pat::PackedCandidateCollection>(ps.getParameter<edm::InputTag>("tagCands"));
    qg_token = consumes<edm::ValueMap<float>>(edm::InputTag("QGTagger", "qgLikelihood"));

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

    _meta._deepLooseWP = ps.getUntrackedParameter<double>("deepCSVL");
    _meta._deepMediumWP = ps.getUntrackedParameter<double>("deepCSVM");
    _meta._deepTightWP = ps.getUntrackedParameter<double>("deepCSVT");

    if (_meta._isMC)
    {
        // muon scale factor files
        muon_trigSF_root = new TFile(muon_trigSF_file.fullPath().c_str());
        muon_trigSF_histo = (TH2F *)muon_trigSF_root->Get("IsoMu24_PtEtaBins/abseta_pt_ratio");

        std::ifstream muon_isoSF_file_json(muon_isoSF_file.fullPath().c_str());
        std::ifstream muon_idSF_file_json(muon_idSF_file.fullPath().c_str());
        std::ifstream btagFile(btag_file.fullPath().c_str());

        boost::property_tree::json_parser::read_json(muon_isoSF_file_json, _muon_isoSF_ptree);
        boost::property_tree::json_parser::read_json(muon_idSF_file_json, _muon_idSF_ptree);

        calib = new BTagCalibration("DeepCSV", btag_file.fullPath().c_str());
        btreader = new BTagCalibrationReader(BTagEntry::OP_RESHAPING, "central", {"up_jes", "down_jes", "up_lf", "down_lf", "up_hf", "down_hf", "up_hfstats1", "down_hfstats1", "up_hfstats2", "down_hfstats2", "up_lfstats1", "down_lfstats1", "up_lfstats2", "down_lfstats2", "up_cferr1", "down_cferr1", "up_cferr2", "down_cferr2"});

        btreader->load(*calib, BTagEntry::FLAV_B, "iterativefit");
        btreader->load(*calib, BTagEntry::FLAV_C, "iterativefit");
        btreader->load(*calib, BTagEntry::FLAV_UDSG, "iterativefit");

    }
    // BTagCalibration calib("DeepCSV", btag_file.fullPath().c_str());
    // BTagCalibrationReader btreader(BTagEntry::OP_MEDIUM, "central", {"up", "down"});
    // btreader.load(calib, BTagEntry::FLAV_B, "comb");

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
    m_jecuAK4 = NULL;
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
    _electrons.clear();
    _taus.clear();
    m_aux.reset();

    //
    //	Event Weights
    //
    if (!_meta._isMC)
        _meta._sumEventWeights += 1;
    else
    {
        edm::Handle<GenEventInfoProduct> hGenEvtInfo;
        e.getByToken(_genInfoToken, hGenEvtInfo);
        _eaux._bareMCWeight = hGenEvtInfo->weight();
        _eaux._genWeight = (hGenEvtInfo->weight() > 0) ? 1 : -1;
        _meta._sumEventWeights += _eaux._genWeight;

        // edm::Handle<double> theprefweight;
        // e.getByToken(prefweight_token, theprefweight);
        // _eaux._prefiringweight = (*theprefweight);

        // edm::Handle<double> theprefweightup;
        // e.getByToken(prefweightup_token, theprefweightup);
        // _eaux._prefiringweightup = (*theprefweightup);

        // edm::Handle<double> theprefweightdown;
        // e.getByToken(prefweightdown_token, theprefweightdown);
        // _eaux._prefiringweightdown = (*theprefweightdown);
    }

    //
    //	HLT
    //	Skip the event if HLT has not fired
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

    edm::Handle<double> hRho;
    e.getByLabel(_rhoToken, hRho);

    // Get Jet Energy Corrections Uncertainties
    esetup.get<JetCorrectionsRecord>().get("AK4PF", m_hJetCParametersAK4);
    JetCorrectorParameters const &jetParametersAK4 = (*m_hJetCParametersAK4)["Uncertainty"];
    if (m_jecuAK4 != NULL)
        delete m_jecuAK4;
    m_jecuAK4 = new JetCorrectionUncertainty(jetParametersAK4);

    // JER SF and Unc
    JME::JetResolution resolution = JME::JetResolution::get(esetup, "AK4PFchs_pt");
    JME::JetResolutionScaleFactor resolution_sf = JME::JetResolutionScaleFactor::get(esetup, "AK4PFchs");

    // BTagCalibration calib("DeepCSV", btag_file.fullPath().c_str());
    // BTagCalibrationReader btreader(BTagEntry::OP_MEDIUM, "central", {"up", "down"});
    // btreader.load(calib, BTagEntry::FLAV_B, "comb");
    // MetFilterResults
    //
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

    if (_meta._isMC)
    {

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
        //
        edm::Handle<std::vector<PileupSummaryInfo>> hPUInfo;
        e.getByToken(_puToken, hPUInfo);
        std::vector<PileupSummaryInfo>::const_iterator pus;
        for (pus = hPUInfo->begin(); pus != hPUInfo->end(); ++pus)
        {
            int bx = pus->getBunchCrossing();
            if (bx == 0)
                _eaux._nPU = pus->getTrueNumInteractions();
        }

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
        _eaux._nvtx = hVertices->size();
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
    edm::Handle<edm::ValueMap<float>> qg_handle;
    e.getByToken(qg_token,qg_handle);

    if (!hJets.isValid())
    {
        std::cout << "Jet Product is not found" << std::endl;
    }
    else
    {
        int ijetRef = -1;
        for (uint32_t i = 0; i < hJets->size(); i++)
        {
            ijetRef++;

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
            myjet._hadronFlavour = jet.hadronFlavour();

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
            edm::RefToBase<pat::Jet> jetRef(edm::Ref<pat::JetCollection>(hJets, ijetRef) );
            myjet._qgLikelihood = (*qg_handle)[jetRef];

            //  b-tagging information
            float btagDisc = 0.0;
            for (std::vector<std::string>::const_iterator btt = _meta._btagNames.begin();
                 btt != _meta._btagNames.end(); ++btt)
            {
                btagDisc += jet.bDiscriminator(*btt);
            }
            myjet._btag = btagDisc;

            myjet._dscvLoose = btagDisc >= _meta._deepLooseWP;
            myjet._dcsvMedium = btagDisc >= _meta._deepMediumWP;
            myjet._dcsvTight = btagDisc >= _meta._deepTightWP;

            if (_meta._isMC)
            {
                if (abs(myjet._hadronFlavour) == 5){
                    myjet._btag_sf = btreader->eval_auto_bounds("central", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_jes_up = btreader->eval_auto_bounds("up_jes", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_jes_down = btreader->eval_auto_bounds("down_jes", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lf_up = btreader->eval_auto_bounds("up_lf", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lf_down = btreader->eval_auto_bounds("down_lf", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hf_up = btreader->eval_auto_bounds("up_hf", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hf_down = btreader->eval_auto_bounds("down_hf", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats1_up = btreader->eval_auto_bounds("up_hfstats1", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats1_down = btreader->eval_auto_bounds("down_hfstats1", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats2_up = btreader->eval_auto_bounds("up_hfstats2", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats2_down = btreader->eval_auto_bounds("down_hfstats2", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats1_up = btreader->eval_auto_bounds("up_lfstats1", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats1_down = btreader->eval_auto_bounds("down_lfstats1", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats2_up = btreader->eval_auto_bounds("up_lfstats2", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats2_down = btreader->eval_auto_bounds("down_lfstats2", BTagEntry::FLAV_B, fabs(jet.eta()), jet.pt(), myjet._btag);

                    
                }
                else if ( abs(myjet._hadronFlavour) == 4){
                    myjet._btag_sf = btreader->eval_auto_bounds("central", BTagEntry::FLAV_C, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_cferr1_up = btreader->eval_auto_bounds("up_cferr1", BTagEntry::FLAV_C, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_cferr1_down = btreader->eval_auto_bounds("down_cferr1", BTagEntry::FLAV_C, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_cferr2_up = btreader->eval_auto_bounds("up_cferr2", BTagEntry::FLAV_C, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_cferr2_down = btreader->eval_auto_bounds("down_cferr2", BTagEntry::FLAV_C, fabs(jet.eta()), jet.pt(), myjet._btag);
                    
                }
                else {
                    myjet._btag_sf = btreader->eval_auto_bounds("central", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag); 
                    myjet._btag_sf_jes_up = btreader->eval_auto_bounds("up_jes", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_jes_down = btreader->eval_auto_bounds("down_jes", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lf_up = btreader->eval_auto_bounds("up_lf", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lf_down = btreader->eval_auto_bounds("down_lf", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hf_up = btreader->eval_auto_bounds("up_hf", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hf_down = btreader->eval_auto_bounds("down_hf", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag); 
                    myjet._btag_sf_hfstats1_up = btreader->eval_auto_bounds("up_hfstats1", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats1_down = btreader->eval_auto_bounds("down_hfstats1", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats2_up = btreader->eval_auto_bounds("up_hfstats2", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_hfstats2_down = btreader->eval_auto_bounds("down_hfstats2", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats1_up = btreader->eval_auto_bounds("up_lfstats1", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats1_down = btreader->eval_auto_bounds("down_lfstats1", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats2_up = btreader->eval_auto_bounds("up_lfstats2", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag);
                    myjet._btag_sf_lfstats2_down = btreader->eval_auto_bounds("down_lfstats2", BTagEntry::FLAV_UDSG, fabs(jet.eta()), jet.pt(), myjet._btag); 
                }
            }

            // energy correction uncertainty
            m_jecuAK4->setJetEta(jet.eta());
            m_jecuAK4->setJetPt(jet.pt());

            double uncAK4 = m_jecuAK4->getUncertainty(true);
            double pt_upAK4 = jet.pt() * (1 + uncAK4);
            double pt_downAK4 = jet.pt() * (1 - uncAK4);

            myjet._uncAK4 = uncAK4;
            myjet._pt_upAK4 = pt_upAK4;
            myjet._pt_downAK4 = pt_downAK4;

            if (_meta._isMC)
            {
                JME::JetParameters jetResParams;
                jetResParams.setJetPt(jet.pt());
                jetResParams.setJetEta(jet.eta());
                jetResParams.setRho(*hRho); // add rho

                myjet._jer = resolution.getResolution(jetResParams);
                myjet._jerSF = resolution_sf.getScaleFactor(jetResParams);
                myjet._jerSF_up = resolution_sf.getScaleFactor(jetResParams, Variation::UP);
                myjet._jerSF_down = resolution_sf.getScaleFactor(jetResParams, Variation::DOWN);
            }

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

    edm::Handle<pat::PackedCandidateCollection> hCandidates;
    e.getByToken(_candToken, hCandidates);

    //
    //  Electrons
    //
    if (_useElectrons)
    {
        // edm::Handle<edm::ValueMap<bool>> hId_veto, hId_loose, hId_medium, hId_tight;
        // e.getByLabel(_eleVetoToken, hId_veto);
        // e.getByLabel(_eleLooseToken, hId_loose);
        // e.getByLabel(_eleMediumToken, hId_medium);
        // e.getByLabel(_eleTightToken, hId_tight);

        edm::Handle<pat::ElectronCollection> hElectrons;
        e.getByLabel(_eleToken, hElectrons);

        edm::Handle<reco::ConversionCollection> hConversions;
        e.getByLabel(_convToken, hConversions);

        /*
        
        
         for (pat::MuonCollection::const_iterator it = muonsSelected.begin();
             it != muonsSelected.end(); ++it)
        {
            pat::Muon mu1 = *it;
    for (pat::MuonCollection::const_iterator it = hMuons->begin();
         it != hMuons->end(); ++it)
    {
         */

        for (pat::ElectronCollection::const_iterator ele = hElectrons->begin();
            ele != hElectrons->end(); ++ele)
        {
            //  >= 10GeV for electrons
            if (ele->pt() < 10)
                continue;

            analysis::core::Electron mye;
            mye._charge = ele->charge();
            mye._pt = ele->pt();
            mye._eta = ele->eta();
            mye._phi = ele->phi();

            mye._sumChargedHadronPt = ele->pfIsolationVariables().sumChargedHadronPt;
            mye._sumNeutralHadronEt = ele->pfIsolationVariables().sumNeutralHadronEt;
            mye._sumPhotonEt = ele->pfIsolationVariables().sumPhotonEt;
            mye._sumPUPt = ele->pfIsolationVariables().sumPUPt;
            mye._sumChargedParticlePt = ele->pfIsolationVariables().sumChargedParticlePt;
            mye._isPF = ele->isPF();
            // mye._convVeto = !ConversionTools::hasMatchedConversion(*ele,
            //                                                        hConversions, hBS->position());
            mye._convVeto = ele->passConversionVeto();
            reco::Vertex bestVtx1;
            for (reco::VertexCollection::const_iterator vt = hVertices->begin();
                 vt != hVertices->end(); ++vt)
            {
                if (!vt->isValid())
                    continue;
                mye._d0PV = ele->gsfTrack()->dxy(vt->position());
                mye._dzPV = ele->gsfTrack()->dz(vt->position());
                bestVtx1 = *vt;
                break;
            }

            mye._ip3d = ele->dB(pat::Electron::PV3D);
            mye._sip3d = fabs(ele->dB(pat::Electron::PV3D)) / ele->edB(pat::Electron::PV3D);

            // float _relCombIso;
            mye._miniIso = getPFMiniIsolation(hCandidates, dynamic_cast<const reco::Candidate *>(&*ele), 0.05, 0.2, 10., false, false, *hRho);

            mye._isTight = ele->electronID("cutBasedElectronID-Fall17-94X-V1-tight") and mye._convVeto;
            mye._isMedium = ele->electronID("cutBasedElectronID-Fall17-94X-V1-medium") and mye._convVeto;
            mye._isLoose = ele->electronID("cutBasedElectronID-Fall17-94X-V1-loose") and mye._convVeto;
            mye._isVeto = ele->electronID("cutBasedElectronID-Fall17-94X-V1-veto") and mye._convVeto;

            // cut based id

            // bool id_veto = (*hId_veto)[ele];
            // mye._ids.push_back(id_veto);
            // bool id_loose = (*hId_loose)[ele];
            // mye._ids.push_back(id_loose);
            // bool id_medium = (*hId_medium)[ele];
            // mye._ids.push_back(id_medium);
            // bool id_tight = (*hId_tight)[ele];
            // mye._ids.push_back(id_tight);

            _electrons.push_back(mye);
        }
    }

    //
    //  Taus
    //

    // if (_useTaus)
    // {
    //     edm::Handle<pat::TauCollection> hTaus;
    //     e.getByLabel(_tauToken, hTaus);
    //     for (pat::TauCollection::const_iterator it = hTaus->begin();
    //          it != hTaus->end(); ++it)
    //     {
    //         //  >=20GeV for Taus only
    //         if (it->pt() < 20)
    //             continue;

    //         analysis::core::Tau mytau;
    //         mytau._pt = it->pt();
    //         mytau._eta = it->eta();
    //         mytau._phi = it->phi();
    //         mytau._isPF = it->isPFTau();
    //         mytau._charge = it->charge();

    //         for (std::vector<std::string>::const_iterator tt = _meta._tauIDNames.begin();
    //              tt != _meta._tauIDNames.end(); ++tt)
    //             mytau._ids.push_back(it->tauID(*tt));

    //         _taus.push_back(mytau);
    //     }
    // }

    // FSR photons
    edm::Handle<std::vector<pat::PFParticle>> selectedFSRphotons;
    e.getByToken(tokenFSRphotons, selectedFSRphotons);

    double fsrDrEt2Cut = 0.012;
    double fsrIsoCut = 1.8;

    for (unsigned int i = 0; i < selectedFSRphotons->size(); i++)
    {
        pat::PFParticle photon = selectedFSRphotons->at(i);
        pat::Muon *associatedMuon = (pat::Muon *)(photon.userCand("associatedMuon").get());
	if (photon.userFloat("PFphotonIso03") < fsrIsoCut && photon.userFloat("ETgammadeltaR") < fsrDrEt2Cut)
        {
            reco::CandidatePtr cutBasedFsrPhoton(selectedFSRphotons, i);
            if (associatedMuon->hasUserCand("cutBasedFsrPhoton"))
            {
                pat::PFParticle *tmpPhoton = (pat::PFParticle *)(associatedMuon->userCand("cutBasedFsrPhoton").get());
                if (photon.userFloat("ETgammadeltaR") < tmpPhoton->userFloat("ETgammadeltaR"))
                {
                    associatedMuon->addUserCand("cutBasedFsrPhoton", cutBasedFsrPhoton, true);
                }
            }
            else
            {
                associatedMuon->addUserCand("cutBasedFsrPhoton", cutBasedFsrPhoton);
            }
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
    // initilize the rochester correcter
    RoccoR rc;
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
    //	Muon Pre-Selection
    //

    else // 2 or more muons
    {
        // make sure Muons are sorted..
        sort(muonsSelected.begin(), muonsSelected.end(), [](pat::Muon it, pat::Muon jt) -> bool { return it.pt() > jt.pt(); });

        float _idSF = 1.;
        float _idSF_up = 1.;
        float _idSF_down = 1.;
        float _isoSF = 1.;
        float _isoSF_up = 1.;
        float _isoSF_down = 1.;
        float ineff = 1.;
        float ineff_up = 1.;
        float ineff_down = 1.;
        // Testing Kinematic fit : Needs to be integrated in the Ntupliser data format - PB 10.09.2018

        TLorentzVector mu1_tlv;
        TLorentzVector mu2_tlv;

        Double_t mu1_ptErr_kinfit;
        mu1_ptErr_kinfit = 0.;
        Double_t mu2_ptErr_kinfit;
        mu2_ptErr_kinfit = 0.;

        RefCountedKinematicVertex dimu_vertex;

        // TODO: Handle higher order effecrs when the events has more than 2 selected muons. For the moment the kinematic fit is run on all possible muons in the collections selectedMuons.
        // The result is store for the first fit and for the first two muons. For ggH and VBF this should be enough, but ttH or VH might need to cover higher order effects.
        // Ideally we should run it only for opposite signed couple of muons and store the pt_kinfit as a vector/array per each muons with an index to the pair related to it.
        if (muonsSelected.size() > 1)
        {
            //Instatiate KinematicVertexFitter object
            KinematicVertexFitter kinfit;
            //Fit and retrieve the tree
            RefCountedKinematicTree kinfittree = kinfit.Fit(muonsSelected);

            if (kinfittree->isEmpty() == 1 || kinfittree->isConsistent() == 0)
                std::cout << "Kinematic Fit unsuccesfull" << std::endl;
            else
            {
                //accessing the tree components
                kinfittree->movePointerToTheTop();
                //We are now at the top of the decay tree getting the dimuon reconstructed KinematicPartlcle
                RefCountedKinematicParticle dimu_kinfit = kinfittree->currentParticle();

                //getting the dimuon decay vertex
                //RefCountedKinematicVertex
                dimu_vertex = kinfittree->currentDecayVertex();

                //Now navigating down the tree
                bool child = kinfittree->movePointerToTheFirstChild();
                //TLorentzVector mu1_tlv;

                if (child)
                {
                    RefCountedKinematicParticle mu1_kinfit = kinfittree->currentParticle();
                    AlgebraicVector7 mu1_kinfit_par = mu1_kinfit->currentState().kinematicParameters().vector();
                    AlgebraicSymMatrix77 mu1_kinfit_cov = mu1_kinfit->currentState().kinematicParametersError().matrix();
                    mu1_ptErr_kinfit = sqrt(mu1_kinfit_cov(3, 3) + mu1_kinfit_cov(4, 4));
                    mu1_tlv.SetXYZM(mu1_kinfit_par.At(3), mu1_kinfit_par.At(4), mu1_kinfit_par.At(5), mu1_kinfit_par.At(6));
                    //        std::cout << "Mu1 chi2 = " << mu1_kinfit->chiSquared() << std::endl;
                    //        std::cout << "Mu1 ndf = " << mu1_kinfit->degreesOfFreedom() << std::endl;
                    //        std::cout << "Covariant matrix" << std::endl;
                    //        std::cout << mu1_kinfit_cov(3,3) << std::endl;
                    //        std::cout << " - " << mu1_kinfit_cov(4,4) << std::endl;
                    //        std::cout << " -      -    " << mu1_kinfit_cov(5,5) << std::endl;
                    //        std::cout << "Muon pt uncertainty = " << sqrt(mu1_kinfit_cov(3,3) + mu1_kinfit_cov(4,4)) << std::endl;
                }

                //Now navigating down the tree
                bool nextchild = kinfittree->movePointerToTheNextChild();

                if (nextchild)
                {
                    RefCountedKinematicParticle mu2_kinfit = kinfittree->currentParticle();
                    AlgebraicVector7 mu2_kinfit_par = mu2_kinfit->currentState().kinematicParameters().vector();
                    AlgebraicSymMatrix77 mu2_kinfit_cov = mu2_kinfit->currentState().kinematicParametersError().matrix();
                    mu2_ptErr_kinfit = sqrt(mu2_kinfit_cov(3, 3) + mu2_kinfit_cov(4, 4));
                    mu2_tlv.SetXYZM(mu2_kinfit_par.At(3), mu2_kinfit_par.At(4), mu2_kinfit_par.At(5), mu2_kinfit_par.At(6));
                }

            } // end else - isEmpty()

            //std::cout << "Kin Fitted muons 1 :" << mu1_tlv.Pt() << "  -- Pat muons : " << muonsSelected.at(0).pt() << std::endl;
            //std::cout << "Kin Fitted muons 2 :" << mu2_tlv.Pt() << "  -- Pat muons : " << muonsSelected.at(1).pt() << std::endl;
            //std::cout << "Kin fit mass from kinfit: " << higgs_tlv.M()  << " - Kin fit mass from tlv: " << (mu1_tlv+mu2_tlv).M()<< std::endl;

        } //if nMuons>1

        int iMuon = 0;
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
                // reco::Candidate::LorentzVector pfm = mu1.pfP4();
                _muon1._pt_PF = mu1.pfP4().Pt();
                _muon1._pterr_PF = mu1.muonBestTrack()->ptError();
                _muon1._eta_PF = mu1.pfP4().eta();
                _muon1._phi_PF = mu1.pfP4().phi();
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
            _muon1._ip3d = mu1.dB(pat::Muon::PV3D);
            _muon1._sip3d = fabs(mu1.dB(pat::Muon::PV3D)) / mu1.edB(pat::Muon::PV3D);

            _muon1._pfIso = (_muon1._sumChargedHadronPtR04 + std::max(0., _muon1._sumNeutralHadronEtR04 + _muon1._sumPhotonEtR04 - 0.5 * _muon1._sumPUPtR04)) / _muon1._pt;
            _muon1._miniIso = getPFMiniIsolation(hCandidates, dynamic_cast<const reco::Candidate *>(&*it), 0.05, 0.2, 10., false, false, *hRho);

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

            // FSR recovery muon
            if (mu1.hasUserCand("cutBasedFsrPhoton"))
            {
                pat::PFParticle *pho = (pat::PFParticle *)(mu1.userCand("cutBasedFsrPhoton").get());
                _muon1.fsrP4.SetPtEtaPhiM(pho->pt(), pho->eta(), pho->phi(), 0.);
            }
            // Kinematic Fit corrections and vertex
            if (dimu_vertex != NULL)
            {
                GlobalVector IPVec(dimu_vertex->position().x() - bestVtx1.position().x(), dimu_vertex->position().y() - bestVtx1.position().y(), dimu_vertex->position().z() - bestVtx1.position().z());
                _muon1._d0PV_kinfit = sqrt(pow(dimu_vertex->position().x() - bestVtx1.position().x(), 2) + pow(dimu_vertex->position().y() - bestVtx1.position().y(), 2));
                _muon1._dzPV_kinfit = fabs(dimu_vertex->position().z() - bestVtx1.position().z());
                _muon1._chi2_kinfit = dimu_vertex->chiSquared();
                _muon1._ndf_kinfit = dimu_vertex->degreesOfFreedom();
                if (iMuon == 0)
                { //first muon
                    GlobalVector direction(mu1_tlv.Px(), mu1_tlv.Py(), mu1_tlv.Pz());
                    float prod = IPVec.dot(direction);
                    int sign = (prod >= 0) ? 1. : -1.;
                    _muon1._d0PV_kinfit *= sign;
                    _muon1._dzPV_kinfit *= sign;
                    _muon1._pt_kinfit = mu1_tlv.Pt();
                    _muon1._ptErr_kinfit = mu1_ptErr_kinfit;
                }
                if (iMuon == 1)
                { //second muon
                    GlobalVector direction(mu2_tlv.Px(), mu2_tlv.Py(), mu2_tlv.Pz());
                    float prod = IPVec.dot(direction);
                    int sign = (prod >= 0) ? 1. : -1.;
                    _muon1._d0PV_kinfit *= sign;
                    _muon1._dzPV_kinfit *= sign;
                    _muon1._pt_kinfit = mu2_tlv.Pt();
                    _muon1._ptErr_kinfit = mu2_ptErr_kinfit;
                }
            }
            else
            { // if the kinfit was not succesful for this muon use the muonBestTrack
                _muon1._pt_kinfit = mu1.muonBestTrack()->pt();
                _muon1._ptErr_kinfit = mu1.muonBestTrack()->ptError();
            }

            // Apply Rochester Correction

            double roccCor = 1.0;
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
                roccCor = rc.kScaleDT(_muon1._charge, _muon1._pt_kinfit, _muon1._eta, _muon1._phi, 0, 0);
            else if (_meta._isMC && genPT > 0.0)
                roccCor = rc.kSpreadMC(_muon1._charge, _muon1._pt_kinfit, _muon1._eta, _muon1._phi, genPT, 0, 0);
            else if (_meta._isMC && genPT <= 0.0)
                roccCor = rc.kSmearMC(_muon1._charge, _muon1._pt_kinfit, _muon1._eta, _muon1._phi, _muon1._nTLs, f_rand, 0, 0);
            _muon1._roccCor = roccCor;
            _muon1._corrPT = roccCor * _muon1._pt_kinfit;

            // Scale Factor Calculation
            // for some reason this is killing muons that hmuon_trigSF_histomuon_trigSF_histomuon_trigSF_histoave pt > 120 GeV??

            if (_meta._isMC)
            {
                float mu_pt = std::min((Double_t)_muon1._pt,
                                       muon_trigSF_histo->GetYaxis()->GetBinLowEdge(muon_trigSF_histo->GetNbinsY()) +
                                           muon_trigSF_histo->GetYaxis()->GetBinWidth(muon_trigSF_histo->GetNbinsY()) - 0.01);
                float mu_eta = std::min(fabs((Double_t)_muon1._eta),
                                        muon_trigSF_histo->GetXaxis()->GetBinLowEdge(muon_trigSF_histo->GetNbinsX()) +
                                            muon_trigSF_histo->GetXaxis()->GetBinWidth(muon_trigSF_histo->GetNbinsX()) - 0.01);
                bool found_mu = false;

                if (mu_pt > muon_trigSF_histo->GetYaxis()->GetBinLowEdge(1))
                {
                    for (int iPt = 1; iPt <= muon_trigSF_histo->GetNbinsY(); iPt++)
                    {
                        if (found_mu)
                            continue;
                        if (mu_pt < muon_trigSF_histo->GetYaxis()->GetBinLowEdge(iPt))
                            continue;
                        if (mu_pt > muon_trigSF_histo->GetYaxis()->GetBinLowEdge(iPt) + muon_trigSF_histo->GetYaxis()->GetBinWidth(iPt))
                            continue;

                        for (int iEta = 1; iEta <= muon_trigSF_histo->GetNbinsX(); iEta++)
                        {
                            if (found_mu)
                                continue;
                            if (mu_eta < muon_trigSF_histo->GetXaxis()->GetBinLowEdge(iEta))
                                continue;
                            if (mu_eta > muon_trigSF_histo->GetXaxis()->GetBinLowEdge(iEta) + muon_trigSF_histo->GetXaxis()->GetBinWidth(iEta))
                                continue;

                            found_mu = true;

                            ineff *= (1. - muon_trigSF_histo->GetBinContent(iEta, iPt));
                            ineff_up *= (1. - muon_trigSF_histo->GetBinContent(iEta, iPt) - muon_trigSF_histo->GetBinError(iEta, iPt));
                            ineff_down *= (1. - muon_trigSF_histo->GetBinContent(iEta, iPt) + muon_trigSF_histo->GetBinError(iEta, iPt));

                        } // End loop: for (int iEta = 1; iEta <= muon_trigSF_histo->GetNbinsX(); iEta++)
                    }     // End loop: for (int iPt = 1; iPt <= muon_trigSF_histo->GetNbinsY(); iPt++)
                }
                typedef boost::property_tree::ptree::path_type path;
                //eta bins for SF
                std::vector<float> absetabins{0.00, 0.90, 1.20, 2.10, 2.40};
                //pt bins for SF
                std::vector<float> ptbins{20.00, 25.00, 30.00, 40.00, 50.00, 60.00, 120.00};
                std::string _value_string, _err_string;
                std::ostringstream _min_eta, _max_eta, _min_pt, _max_pt;
                bool foundEta = true;
                bool foundPt = true;
                _min_pt.str("");
                _min_eta.str("");
                _max_pt.str("");
                _max_eta.str("");

                for (int _abseta = 0; _abseta < int(absetabins.size()) - 1; _abseta++)
                {
                    if (abs(_muon1._eta) < absetabins.at(_abseta))
                        continue;
                    if (abs(_muon1._eta) >= absetabins.at(_abseta + 1))
                        continue;
                    _min_eta << std::fixed << std::setprecision(2) << absetabins.at(_abseta);
                    _max_eta << std::fixed << std::setprecision(2) << absetabins.at(_abseta + 1);
                }
                if (_min_eta.str().compare(_max_eta.str()) == 0)
                {
                    _min_pt.str("");
                    _min_eta.str("");
                    _max_pt.str("");
                    _max_eta.str("");
                    foundEta = false;
                }
                for (int _pt = 0; _pt < int(ptbins.size()) - 1; _pt++)
                {
                    if (_muon1._pt < ptbins.at(_pt))
                        continue;
                    if (_muon1._pt >= ptbins.at(_pt + 1))
                        continue;
                    _min_pt << std::fixed << std::setprecision(2) << ptbins.at(_pt);
                    _max_pt << std::fixed << std::setprecision(2) << ptbins.at(_pt + 1);
                }
                if (_min_pt.str().compare(_max_pt.str()) == 0)
                {
                    _min_pt.str("");
                    _min_eta.str("");
                    _max_pt.str("");
                    _max_eta.str("");
                    foundPt = false;
                }

                if (foundEta && foundPt)
                { // ID
                    _value_string = "NUM_" + _id_wp_num + "_DEN_" + _id_wp_den + "/abseta_pt/abseta:[" + _min_eta.str() + "," + _max_eta.str() + "]/pt:[" + _min_pt.str() + "," + _max_pt.str() + "]/value";
                    _idSF *= _muon_idSF_ptree.get<float>(path(_value_string.c_str(), '/'));
                    _err_string = "NUM_" + _id_wp_num + "_DEN_" + _id_wp_den + "/abseta_pt/abseta:[" + _min_eta.str() + "," + _max_eta.str() + "]/pt:[" + _min_pt.str() + "," + _max_pt.str() + "]/error";
                    _idSF_up *= _idSF + _muon_idSF_ptree.get<float>(path(_err_string.c_str(), '/'));
                    _idSF_down *= _idSF - _muon_idSF_ptree.get<float>(path(_err_string.c_str(), '/'));
                    // Iso
                    _value_string = "NUM_" + _iso_wp_num + "_DEN_" + _iso_wp_den + "/abseta_pt/abseta:[" + _min_eta.str() + "," + _max_eta.str() + "]/pt:[" + _min_pt.str() + "," + _max_pt.str() + "]/value";
                    _isoSF *= _muon_isoSF_ptree.get<float>(path(_value_string.c_str(), '/'));
                    _err_string = "NUM_" + _iso_wp_num + "_DEN_" + _iso_wp_den + "/abseta_pt/abseta:[" + _min_eta.str() + "," + _max_eta.str() + "]/pt:[" + _min_pt.str() + "," + _max_pt.str() + "]/error";
                    _isoSF_up *= _isoSF + _muon_isoSF_ptree.get<float>(path(_err_string.c_str(), '/'));
                    _isoSF_down *= _isoSF - _muon_isoSF_ptree.get<float>(path(_err_string.c_str(), '/'));

                    //cleaning the strings
                    _min_pt.str("");
                    _min_eta.str("");
                    _max_pt.str("");
                    _max_eta.str("");
                }
            }

            _muons.push_back(_muon1);
            ++iMuon;
        }
        _eaux._idSF = _idSF;
        _eaux._idSF_up = _idSF_up;
        _eaux._idSF_down = _idSF_down;
        _eaux._isoSF = _isoSF;
        _eaux._isoSF_up = _isoSF_up;
        _eaux._isoSF_down = _isoSF_down;
        _eaux._trigEffSF = 1. - ineff;
        _eaux._trigEffSF_up = 1. - ineff_up;
        _eaux._trigEffSF_down = 1. - ineff_down;
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


double H2DiMuonMaker::getPFMiniIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
					const reco::Candidate* ptcl,  
					double r_iso_min, double r_iso_max, double kt_scale,
					bool use_pfweight, bool charged_only, double rho) {
    if (ptcl->pt() < 5.)
        return 99999.;

    double deadcone_nh(0.), deadcone_ch(0.), deadcone_ph(0.), deadcone_pu(0.);
    if (ptcl->isElectron())
    {
        if (fabs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 1.479)
        {
            deadcone_ch = 0.015;
            deadcone_pu = 0.015;
            deadcone_ph = 0.08;
        }
    }
    else if (ptcl->isMuon())
    {
        deadcone_ch = 0.0001;
        deadcone_pu = 0.01;
        deadcone_ph = 0.01;
        deadcone_nh = 0.01;
    }
    else
    {
    }

    double iso_nh(0.);
    double iso_ch(0.);
    double iso_ph(0.);
    double iso_pu(0.);
    double ptThresh(0.5);
    if (ptcl->isElectron())
        ptThresh = 0;
    double r_iso = std::max(r_iso_min, std::min(r_iso_max, kt_scale / ptcl->pt()));
    for (const pat::PackedCandidate &pfc : *pfcands)
    {
        if (abs(pfc.pdgId()) < 7)
            continue;

        double dr = deltaR(pfc, *ptcl);
        if (dr > r_iso)
            continue;

        //////////////////  NEUTRALS  /////////////////////////
        if (pfc.charge() == 0)
        {
            if (pfc.pt() > ptThresh)
            {
                double wpf(1.);
                /////////// PHOTONS ////////////
                if (abs(pfc.pdgId()) == 22)
                {
                    if (dr < deadcone_ph)
                        continue;
                    iso_ph += wpf * pfc.pt();
                    /////////// NEUTRAL HADRONS ////////////
                }
                else if (abs(pfc.pdgId()) == 130)
                {
                    if (dr < deadcone_nh)
                        continue;
                    iso_nh += wpf * pfc.pt();
                }
            }
            //////////////////  CHARGED from PV  /////////////////////////
        }
        else if (pfc.fromPV() > 1)
        {
            if (abs(pfc.pdgId()) == 211)
            {
                if (dr < deadcone_ch)
                    continue;
                iso_ch += pfc.pt();
            }
            //////////////////  CHARGED from PU  /////////////////////////
        }
        else
        {
            if (pfc.pt() > ptThresh)
            {
                if (dr < deadcone_pu)
                    continue;
                iso_pu += pfc.pt();
            }
        }
    }
    double iso(0.);
    int em = 0;
    if (ptcl->isMuon())
        em = 1;

    double Aeff_Moriond17[2][7] =
        {
            {0.1752, 0.1862, 0.1411, 0.1534, 0.1903, 0.2243, 0.2687}, // electrons
            {0.0735, 0.0619, 0.0465, 0.0433, 0.0577, 0.0, 0.0}        // muons
        };

    double CorrectedTerm = 0.0;
    double riso2 = r_iso * r_iso;

    if (em)
    { // muon
        if (TMath::Abs(ptcl->eta()) < 0.8)
            CorrectedTerm = rho * Aeff_Moriond17[1][0] * (riso2 / 0.09);
        else if (TMath::Abs(ptcl->eta()) > 0.8 && TMath::Abs(ptcl->eta()) < 1.3)
            CorrectedTerm = rho * Aeff_Moriond17[1][1] * (riso2 / 0.09);
        else if (TMath::Abs(ptcl->eta()) > 1.3 && TMath::Abs(ptcl->eta()) < 2.0)
            CorrectedTerm = rho * Aeff_Moriond17[1][2] * (riso2 / 0.09);
        else if (TMath::Abs(ptcl->eta()) > 2.0 && TMath::Abs(ptcl->eta()) < 2.2)
            CorrectedTerm = rho * Aeff_Moriond17[1][3] * (riso2 / 0.09);
        else if (TMath::Abs(ptcl->eta()) > 2.2 && TMath::Abs(ptcl->eta()) < 2.5)
            CorrectedTerm = rho * Aeff_Moriond17[1][4] * (riso2 / 0.09);
    }
    else
    {
        if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 1.0)
            CorrectedTerm = rho * Aeff_Moriond17[0][0] * (riso2 / 0.09);
        else if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 1.0 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 1.479)
            CorrectedTerm = rho * Aeff_Moriond17[0][1] * (riso2 / 0.09);
        else if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 1.479 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 2.0)
            CorrectedTerm = rho * Aeff_Moriond17[0][2] * (riso2 / 0.09);
        else if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 2.0 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 2.2)
            CorrectedTerm = rho * Aeff_Moriond17[0][3] * (riso2 / 0.09);
        else if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 2.2 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 2.3)
            CorrectedTerm = rho * Aeff_Moriond17[0][4] * (riso2 / 0.09);
        else if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 2.3 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 2.4)
            CorrectedTerm = rho * Aeff_Moriond17[0][5] * (riso2 / 0.09);
        else if (TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 2.4 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) > 2.4 && TMath::Abs(dynamic_cast<const pat::Electron *>(ptcl)->superCluster()->eta()) < 2.5)
            CorrectedTerm = rho * Aeff_Moriond17[0][6] * (riso2 / 0.09);
    }

    iso = iso_ch + TMath::Max(0.0, iso_ph + iso_nh - CorrectedTerm);
    iso = iso / ptcl->pt();
    return iso;
}
