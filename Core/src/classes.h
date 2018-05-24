#include "HMuMu/Core/interface/Object.h"
#include "HMuMu/Core/interface/QIE10Frame.h"
#include "HMuMu/Core/interface/QIE8Frame.h"
#include "HMuMu/Core/interface/Event.h"
#include "HMuMu/Core/interface/GenParticle.h"
#include "HMuMu/Core/interface/Jet.h"
#include "HMuMu/Core/interface/Muon.h"
#include "HMuMu/Core/interface/Vertex.h"
#include "HMuMu/Core/interface/GenJet.h"
#include "HMuMu/Core/interface/MET.h"
#include "HMuMu/Core/interface/Track.h"
#include "HMuMu/Core/interface/Tau.h"
#include "HMuMu/Core/interface/Electron.h"
#include "HMuMu/Core/interface/MetaHiggs.h"
#include "DataFormats/Common/interface/Wrapper.h"

namespace
{
	struct dictionary
	{
		analysis::core::Objects dumm0;
		analysis::core::QIE10Digis dumm1;
		analysis::core::QIE8Digis dumm2;
		analysis::core::Events dumm3;
		analysis::core::GenParticles dumm4;
		analysis::core::Jets dumm5;
		analysis::core::Muons dumm6;
		analysis::core::Vertices dumm7;
		analysis::core::GenJets dumm8;
		analysis::core::METs dumm9;
		analysis::core::Tracks dumm10;
		analysis::dimuon::MetaHiggs dumm12;
		analysis::core::EventAuxiliaries dumm13;
        analysis::core::Taus dumm14;
        analysis::core::Electrons dumm15;
		analysis::dimuon::Auxiliary dumm16;
	};
}
