#include "HMuMu/Core/interface/Object.h"
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
		analysis::core::Events dumm1;
		analysis::core::GenParticles dumm2;
		analysis::core::Jets dumm3;
		analysis::core::Muons dumm4;
		analysis::core::Vertices dumm5;
		analysis::core::GenJets dumm6;
		analysis::core::METs dumm7;
		analysis::core::Tracks dumm8;
		analysis::dimuon::MetaHiggs dumm9;
        analysis::core::Taus dumm10;
        analysis::core::Electrons dumm11;
	};
}
