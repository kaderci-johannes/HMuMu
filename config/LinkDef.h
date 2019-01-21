#ifdef __CINT__

#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;

#pragma link C++ class analysis::core::Object+;
#pragma link C++ class analysis::core::Muon+;
#pragma link C++ class analysis::core::Tau+;
#pragma link C++ class analysis::core::Electron+;
#pragma link C++ class analysis::core::Track+;
#pragma link C++ class analysis::core::GenJet+;
#pragma link C++ class analysis::core::Jet+;
#pragma link C++ class analysis::core::GenParticle+;
#pragma link C++ class analysis::core::MET+;
#pragma link C++ class analysis::core::Vertex+;
#pragma link C++ class analysis::core::Event+;
#pragma link C++ class analysis::core::EventAuxiliary+;
#pragma link C++ class analysis::dimuon::MetaHiggs+;
#pragma link C++ class analysis::processing::Streamer+;
#pragma link C++ class analysis::dimuon::Auxiliary+;
#pragma link C++ class reweight::LumiReWeighting+;

#pragma link C++ class std::bitset<256>+;
#pragma link C++ class std::map<int, bool>+;

#pragma link C++ class std::vector<analysis::core::Object>+;
#pragma link C++ class std::vector<analysis::core:Muon>+;
#pragma link C++ class std::vector<analysis::core:Electron>+;
#pragma link C++ class std::vector<analysis::core:Tau>+;
#pragma link C++ class std::vector<analysis::core::Track>+;
#pragma link C++ class std::vector<analysis::core::GenJet>+;
#pragma link C++ class std::vector<analysis::core::Jet>+;
#pragma link C++ class std::vector<analysis::core::GenParticle>+;
#pragma link C++ class std::vector<analysis::core::Vertex>+;

#pragma link C++ class std::vector<std::vector<int> >+;
#pragma link C++ class std::vector<std::vector<std::vector<int> > >+;
#pragma link C++ class std::vector<std::pair<int, int> >+;
#pragma link C++ class std::vector<std::vector<float> >+;
#pragma link C++ class std::vector<std::vector<double> >+;
#pragma link C++ class std::vector<std::vector<analysis::core::Muon> >+;

#pragma link C++ class std::vector<std::map<int, std::vector<int> > >+;
#pragma link C++ class std::vector<std::map<int, int> >+;
#pragma link C++ class std::vector<std::vector<std::pair<int, int> > >+;

#pragma link C++ class std::vector<TLorentzVector>+;

#pragma link C++ class std::map<int, std::map<int, analysis::core::Muon> >+;
#pragma link C++ class std::map<int, int>+;
#pragma link C++ class std::map<int, float>+;
#pragma link C++ class std::map<int, double>+;
#pragma link C++ class std::map<int, std::map<int, int> >+;
#pragma link C++ class std::map<int, std::map<int, float> >+;
#pragma link C++ class std::map<int, std::map<int, double> >+;
#pragma link C++ class std::map<int, std::map<int, std::map<int,int> > >+;

#pragma link C++ class std::map<int, std::pair<int, int> >+;

#pragma link C++ class std::unordered_map<int, int>+;
#pragma link C++ class std::unordered_map<int, float>+;
#pragma link C++ class std::unordered_map<int, double>+;
#pragma link C++ class std::unordered_map<int, std::unordered_map<int, int> >+;
#pragma link C++ class std::unordered_map<int, std::unordered_map<int, float> >+;
#pragma link C++ class std::unordered_map<int, std::unordered_map<int, double> >+;

#pragma link C++ class std::unordered_multimap<int, int>+;
#pragma link C++ class std::unordered_multimap<int, float>+;
#pragma link C++ class std::unordered_multimap<int, double>+;
#pragma link C++ class std::unordered_multimap<int, std::unordered_multimap<int, int> >+;
#pragma link C++ class std::unordered_multimap<int, std::unordered_multimap<int, float> >+;
#pragma link C++ class std::unordered_multimap<int, std::unordered_multimap<int, double> >+;

#pragma link C++ class std::multimap<int, int>+;
#pragma link C++ class std::multimap<int, float>+;
#pragma link C++ class std::multimap<int, double>+;
#pragma link C++ class std::multimap<int, std::multimap<int, int> >+;
#pragma link C++ class std::multimap<int, std::multimap<int, float> >+;
#pragma link C++ class std::multimap<int, std::multimap<int, double> >+;

#pragma link C++ struct std::pair<int, int>+;
#pragma link C++ class std::string+;

#pragma link C++ class std::list<int>+;
#pragma link C++ class std::list<float>+;
#pragma link C++ class std::list<double>+;
#pragma link C++ class std::list<std::list<int> >+;
#pragma link C++ class std::list<std::list<float> >+;
#pragma link C++ class std::list<std::list<double> >+;

#pragma link C++ class std::forward_list<int>+;
#pragma link C++ class std::forward_list<float>+;
#pragma link C++ class std::forward_list<double>+;
#pragma link C++ class std::forward_list<std::forward_list<int> >+;
#pragma link C++ class std::forward_list<std::forward_list<float> >+;
#pragma link C++ class std::forward_list<std::forward_list<double> >+;

#pragma link C++ class std::deque<int>+;
#pragma link C++ class std::deque<float>+;
#pragma link C++ class std::deque<double>+;
#pragma link C++ class std::deque<std::deque<int> >+;
#pragma link C++ class std::deque<std::deque<float> >+;
#pragma link C++ class std::deque<std::deque<double> >+;

#pragma link C++ class std::set<int>+;
#pragma link C++ class std::set<float>+;
#pragma link C++ class std::set<double>+;
#pragma link C++ class std::set<std::set<int> >+;
#pragma link C++ class std::set<std::set<float> >+;
#pragma link C++ class std::set<std::set<double> >+;

#pragma link C++ class std::unordered_set<int>+;
#pragma link C++ class std::unordered_set<float>+;
#pragma link C++ class std::unordered_set<double>+;
#pragma link C++ class std::unordered_set<std::unordered_set<int> >+;
#pragma link C++ class std::unordered_set<std::unordered_set<float> >+;
#pragma link C++ class std::unordered_set<std::unordered_set<double> >+;

#pragma link C++ class std::multiset<int>+;
#pragma link C++ class std::multiset<float>+;
#pragma link C++ class std::multiset<double>+;
#pragma link C++ class std::multiset<std::multiset<int> >+;
#pragma link C++ class std::multiset<std::multiset<float> >+;
#pragma link C++ class std::multiset<std::multiset<double> >+;

#pragma link C++ class std::unordered_multiset<int>+;
#pragma link C++ class std::unordered_multiset<float>+;
#pragma link C++ class std::unordered_multiset<double>+;
#pragma link C++ class std::unordered_multiset<std::unordered_multiset<int> >+;
#pragma link C++ class std::unordered_multiset<std::unordered_multiset<float> >+;
#pragma link C++ class std::unordered_multiset<std::unordered_multiset<double> >+;

#endif
