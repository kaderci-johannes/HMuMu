#ifdef STANDALONE
#include "Muon.h"
#include "Electron.h"
#include "Jet.h"
#include "Vertex.h"
#include "Event.h"
#include "MET.h"
#include "Streamer.h"
#include "MetaHiggs.h"

//	ROOT headers
#include "TFile.h"
#include "TChain.h"
#include "TString.h"
#include "TMath.h"
#include "TH1D.h"
#include "TLorentzVector.h"
#include <signal.h>
#include <fstream>

std::string __inputfilename;
std::string __outputfilename;

bool __isMC = false;
bool __genPUMC;
std::string __puMCfilename;
std::string __puDATAfilename;
bool __continueRunning = true;

/*
 *  Define all the Constants
 */
double const PDG_MASS_Mu = 0.105658367;
/*
 * Define cuts
 */
double _muonMatchedPt = 30.;
double _muonMatchedEta = 2.4;
double _muonPt = 20.;
double _muonEta = 2.4;
double _muonIso = 0.25;
// double _dimuonMinMass = 80.;
// double _dimuonMaxMass = 85.;
double _leadJetPt = 40.;
double _subleadJetPt = 30.;
double _metPt = 40.;
int __nPassEventSelection = 0;
int __nContainJets = 0;
int __nContainBJets = 0;
int __nPassMjj = 0;

std::string const NTUPLEMAKER_NAME = "ntuplemaker_H2DiMuonMaker";

using namespace analysis::core;
using namespace analysis::processing;

bool passVertex(Vertices *v)
{
	if (v->size() == 0)
		return false;
	for (Vertices::const_iterator it = v->begin();
		 it != v->end(); ++it)
	{
		if (TMath::Abs(it->_z) < 24 &&
			it->_ndf > 4)
			return true;
	}

	return false;
}

bool passMuon(Muon const &m)
{
	double muonIsolation = (m._sumChargedHadronPtR04 + std::max(0.,
																m._sumNeutralHadronEtR04 + m._sumPhotonEtR04 - 0.5 * m._sumPUPtR04)) /
						   m._pt;

	if (m._isGlobal && m._isTracker &&
		m._pt > _muonPt && TMath::Abs(m._eta) < _muonEta &&
		m._isMedium && muonIsolation < _muonIso)
		return true;
	return false;
}

bool passMuonHLT(Muon const &m)
{
	if ((m._isHLTMatched[1] || m._isHLTMatched[0]) &&
		m._pt > _muonMatchedPt && TMath::Abs(m._eta) < _muonMatchedEta)
		return true;

	return false;
}

bool passMuons(Muon const &m1, Muon const &m2)
{
	if ((m1._charge != m2._charge) && passMuon(m1) && passMuon(m2))
	{
		if (passMuonHLT(m1) || passMuonHLT(m2))
		{
			// TLorentzVector p4m1, p4m2;
			// p4m1.SetPtEtaPhiM(m1._pt, m1._eta, m1._phi, PDG_MASS_Mu);
			// p4m2.SetPtEtaPhiM(m2._pt, m2._eta, m2._phi, PDG_MASS_Mu);
			// TLorentzVector p4dimuon = p4m1 + p4m2;

			// if (p4dimuon.M() > _dimuonMinMass && p4dimuon.M() < _dimuonMaxMass)
			return true;
		}
	}

	return false;
}

float jetMuondR(float jeta, float jphi, float meta, float mphi)
{
	TLorentzVector p4j, p4m;
	p4j.SetPtEtaPhiM(10, jeta, jphi, 0);
	p4m.SetPtEtaPhiM(10, meta, mphi, 0);
	return p4j.DeltaR(p4m);
}

bool passElectronVeto(Electrons *electrons, Muon m1, Muon m2)
{
	for (Electrons::const_iterator it = electrons->begin();
		 it != electrons->end(); ++it)
	{
		if (it->_ids[2] && it->_pt > 10. &&
			(TMath::Abs(it->_eta) < 1.4442 || (1.566 < TMath::Abs(it->_eta) && TMath::Abs(it->_eta) < 2.5)) && jetMuondR(it->_eta, it->_phi, m1._eta, m1._phi) > 0.4 && jetMuondR(it->_eta, it->_phi, m2._eta, m2._phi) > 0.4)
			return false;
	}

	return true;
}

bool passBTaggedJetVeto(Jets *jets)
{
	for (Jets::const_iterator it = jets->begin(); it != jets->end(); ++it)
		if (it->_pt > 30. & TMath::Abs(it->_eta) < 2.4 && it->_btag[0] > 0.4941)
			return false;
	return true;
}
bool passTightJetID(Jet const &j)
{
	bool tightID = false;
	double jeta = TMath::Abs(j._eta);
	int numConst = j._cm + j._nm;

	if (jeta <= 2.7)
	{
		tightID = (j._nhf < 0.90 && j._nef < 0.90 && numConst > 1);

		if (jeta < 2.4)
		{
			tightID &= (j._chf > 0 && j._cm > 0);
		}
	}
	else if (jeta <= 3.0)
	{
		tightID = (j._nef > 0.02 && j._nef < 0.99 && j._nm > 2);
	}
	else
	{
		tightID = (j._nef < 0.90 && j._nhf > 0.02 && j._nm > 10);
	}

	return tightID;
}

bool passLoosePUID(Jet const &j)
{
	return (j._fullid & (1 << 2));
}
void categorize(ofstream &out, Jets *jets, Muon const &mu1, Muon const &mu2,
				MET const &met, Event const &event)
{

	out << " * " << event._run << " * " << event._lumi << " * " << event._event << " * ";
	out << mu1._pt << " * " << mu1._eta << " * " << mu1._phi << " * ";
	out << mu2._pt << " * " << mu2._eta << " * " << mu2._phi << " * ";

	TLorentzVector p4m1, p4m2;
	p4m1.SetPtEtaPhiM(mu1._pt, mu1._eta,
					  mu1._phi, PDG_MASS_Mu);
	p4m2.SetPtEtaPhiM(mu2._pt, mu2._eta,
					  mu2._phi, PDG_MASS_Mu);
	TLorentzVector p4dimuon = p4m1 + p4m2;

	out << p4dimuon.M() << " * ";

	// jets selection
	std::vector<TLorentzVector> p4jets;

	int _btagJets = 0;
	for (Jets::const_iterator it = jets->begin(); it != jets->end(); ++it)
	{
		if (it->_pt > 30 && TMath::Abs(it->_eta) < 4.7 && passTightJetID(*it) && passLoosePUID(*it))
		{
			if ((jetMuondR(it->_eta, it->_phi, mu1._eta, mu1._phi) > 0.4) &&
				(jetMuondR(it->_eta, it->_phi, mu2._eta, mu2._phi) > 0.4))
			{
				if (it->_btag[0] > 0.4941)
					_btagJets++;
				TLorentzVector p4;
				p4.SetPtEtaPhiM(it->_pt, it->_eta, it->_phi, it->_mass);
				p4jets.push_back(p4);
			}
		}
	}

	out << p4jets.size() << " * ";

	float leadpt = 0;
	float leadeta = 0;
	float leadphi = 0;
	float subpt = 0;
	float subeta = 0;
	float subphi = 0;
	float mjj = 0;
	TLorentzVector p4lead, p4sub, dijet;
	if (p4jets.size() > 0)
	{
		__nContainJets++;
		p4lead = p4jets[0];
		leadpt = p4lead.Pt();
		leadeta = p4lead.Eta();
		leadphi = p4lead.Phi();
	}
	if (p4jets.size() > 1)
	{
		p4sub = p4jets[1];
		dijet = p4lead + p4sub;
		if (dijet.M() > 100)
			__nPassMjj++;
		subpt = p4sub.Pt();
		subeta = p4sub.Eta();
		subphi = p4sub.Phi();
		mjj = dijet.M();
	}
	out << leadpt << " * " << leadeta << " * " << leadphi << " * ";
	out << subpt << " * " << subeta << " * " << subphi << " * ";
	out << mjj << " * ";
	if (_btagJets > 0)
		__nContainBJets++;
	out << _btagJets << " * " << std::endl;
	return;
}

float sampleinfo(std::string const &inputFiles)
{
	Streamer samples(inputFiles, NTUPLEMAKER_NAME + "/Meta");
	samples.chainup();

	using namespace analysis::dimuon;
	MetaHiggs *meta = NULL;

	samples._chain->SetBranchAddress("Meta", &meta);
	long long int numEvents = 0;
	long long int numEventsWeighted = 0;
	for (int i = 0; i < samples._chain->GetEntries(); i++)
	{
		samples._chain->GetEntry(i);
		numEvents += meta->_nEventsProcessed;
		numEventsWeighted += meta->_sumEventWeights;
	}
	std::cout
		<< "# events processed total = " << numEvents << std::endl
		<< "# events weighted total = " << numEventsWeighted << std::endl;

	return numEventsWeighted;
}
void process()
{
	//	out ...
	// TFile *outroot = new TFile(__outputfilename.c_str(), "recreate");

	// Streamer streamer(__inputfilename, "Events");
	Streamer streamer(__inputfilename, NTUPLEMAKER_NAME + "/Events");
	streamer.chainup();

	Muons *muons = NULL;
	Muons muons1;
	Muons muons2;
	Jets *jets = NULL;
	Electrons *electrons = NULL;
	Vertices *vertices = NULL;
	Event *event = NULL;
	EventAuxiliary *aux = NULL;
	MET *met = NULL;
	streamer._chain->SetBranchAddress("Muons", &muons);
	streamer._chain->SetBranchAddress("Jets", &jets);
	streamer._chain->SetBranchAddress("Vertices", &vertices);
	streamer._chain->SetBranchAddress("Event", &event);
	streamer._chain->SetBranchAddress("Electrons", &electrons);
	streamer._chain->SetBranchAddress("EventAuxiliary", &aux);
	streamer._chain->SetBranchAddress("MET", &met);

	ofstream eventData;
	eventData.open("synch_data_eventDump.txt");
	eventData << "* run * lumi * event * m1pt * m1eta * m1phi * m2pt * m2eta * m2phi * mass * njets * j1pt * j1eta * j1phi * j2pt * j2eta * j2phi * mjj * nbjets *" << std::endl;

	//	Main Loop
	uint32_t numEntries = streamer._chain->GetEntries();
	for (uint32_t i = 0; i < numEntries && __continueRunning; i++)
	{
		muons1.clear();
		muons2.clear();
		streamer._chain->GetEntry(i);
		if (i % 1000 == 0)
			std::cout << "### Event " << i << " / " << numEntries
					  << std::endl;

		//
		//	Selections
		//
		if (!passVertex(vertices))
			continue;
		if (!(aux->_hasHLTFired[0] || aux->_hasHLTFired[1]))
			continue;
		if (!aux->_passedMetFilters)
			continue;

		std::vector<std::pair<Muon, Muon>> muonPairs;
		for (Muons::iterator it = muons->begin(); it != muons->end(); ++it)
			for (Muons::iterator jt = (it + 1); jt != muons->end(); ++jt)
				if (passMuons(*it, *jt))
					muonPairs.push_back(std::make_pair(*it, *jt));
		if (muonPairs.size() == 0)
			continue;

		float highestPtSum = 0;
		std::pair<Muon, Muon> highestPtMuons;
		for (const std::pair<Muon, Muon> &twoMuons : muonPairs)
		{
			TLorentzVector p4m1, p4m2;
			p4m1.SetPtEtaPhiM(twoMuons.first._pt, twoMuons.first._eta, twoMuons.first._phi, PDG_MASS_Mu);
			p4m2.SetPtEtaPhiM(twoMuons.second._pt, twoMuons.second._eta, twoMuons.second._phi, PDG_MASS_Mu);
			TLorentzVector p4dimuon = p4m1 + p4m2;

			if (p4dimuon.Pt() > highestPtSum)
			{
				highestPtSum = p4dimuon.Pt();
				highestPtMuons = twoMuons;
			}
		}
		__nPassEventSelection++;

		categorize(eventData, jets, highestPtMuons.first, highestPtMuons.second, *met, *event);
	}

	std::cout << "Inclusive : " << __nPassEventSelection << std::endl;
	std::cout << "Njets > 0 : " << __nContainJets << std::endl;
	std::cout << "Nbjets > 0 : " << __nContainBJets << std::endl;
	std::cout << "Mjj > 100 GeV : " << __nPassMjj << std::endl;

	// outroot->Write();
	// outroot->Close();
	return;
}

void sigHandler(int sig)
{
	cout << "### Signal: " << sig << " caughter. Exiting..." << endl;
	__continueRunning = false;
}

void printCuts()
{
	std::cout << "Cuts:" << std::endl
			  << "_muonMatchedPt = " << _muonMatchedPt << std::endl
			  << "_muonMatchedEta = " << _muonMatchedEta << std::endl
			  << "_muonPt = " << _muonPt << std::endl
			  << "_muonEta = " << _muonEta << std::endl
			  << "_muonIso = " << _muonIso << std::endl
			  << "_leadJetPt = " << _leadJetPt << std::endl
			  << "_subleadJetPt = " << _subleadJetPt << std::endl
			  << "_metPt = " << _metPt << std::endl;
}

int main(int argc, char **argv)
{
	/*
	 *	Register signals
	 */
	signal(SIGABRT, &sigHandler);
	signal(SIGTERM, &sigHandler);
	signal(SIGINT, &sigHandler);

	std::string none;
	bool genPUMC = false;

	// Assign globals
	if (argc > 2)
	{
		__inputfilename = argv[1];
		__outputfilename = argv[2];
	}
	else
	{
		exit(EXIT_FAILURE);
	}
	printCuts();
	process();
	return 0;
}

#endif
