#ifndef Analysis_Core_Jet_h
#define Analysis_Core_Jet_h

#ifndef STANDALONE
#include "HMuMu/Core/interface/GenJet.h"
#else
#include "GenJet.h"
#endif

#include <math.h>       /* fabs */

namespace analysis
{
namespace core
{
class Jet : public Object
{
  public:
	Jet() : Object() { this->reset(); }

	virtual void reset()
	{
		_px = 0;
		_py = 0;
		_pz = 0;
		_pt = 0;
		_eta = 0;
		_phi = 0;
		_mass = 0;
		_charge = 0;
		_partonFlavour = 0;
		_hadronFlavour = 0;
		_chf = 0;
		_nhf = 0;
		_cef = 0;
		_nef = 0;
		_muf = 0;
		_hfhf = 0;
		_hfef = 0;
		_cm = 0;
		_nm = 0;
		_chm = 0;
		_nhm = 0;
		_cem = 0;
		_nem = 0;
		_mum = 0;
		_hfhm = 0;
		_hfem = 0;
		_jecf = 0;
		_jecu = 0;
		_btag = 0;
		_dscvLoose = false;
		_dcsvMedium = false;
		_dcsvTight = false;

		_btag_sf = 1;
		_btag_sf_up = 0;
		_btag_sf_down = 0;

		_puid = 0;
		_fullid = 0;
		_passLoosePU = false;
		_qgLikelihood = 0;
		
		_uncAK4 = 0;
		_pt_upAK4 = 0;
		_pt_downAK4 = 0;

		_jer = 0;
		_jerSF = 0;
		_jerSF_up = 0;
		_jerSF_down = 0;

		_genjet.reset();
		_genMatched = 0;
		_genemf = 0;
		_genhadf = 0;
		_geninvf = 0;
		_genauxf = 0;
	}
	virtual ~Jet() {}

	float _px;
	float _py;
	float _pz;
	float _pt;
	float _eta;
	float _phi;
	float _mass;
	float _charge;
	float _partonFlavour;
	float _hadronFlavour;

	float _chf;
	float _nhf;
	float _cef;
	float _nef;
	float _muf;
	float _hfhf;
	float _hfef;
	float _cm;
	float _nm;
	float _chm;
	float _nhm;
	float _cem;
	float _nem;
	float _mum;
	float _hfhm;
	float _hfem;
	float _jecf;
	float _jecu;
	float _btag;
	bool _dscvLoose;
	bool _dcsvMedium;
	bool _dcsvTight;

	double _btag_sf;
	double _btag_sf_up;
	double _btag_sf_down;

	float _puid;
	int _fullid;
	bool _passLoosePU;
	float _qgLikelihood;

	double _uncAK4;
	double _pt_upAK4;
	double _pt_downAK4;

	float _jer;
	float _jerSF;
	float _jerSF_up;
	float _jerSF_down;

	//
	GenJet _genjet;
	bool _genMatched;
	float _genemf;
	float _genhadf;
	float _geninvf;
	float _genauxf;

	bool operator==(const Jet& j2)
	{
		return (fabs(this->_pt - j2._pt) < this->_pt * .0001 && 
				fabs(this->_eta - j2._eta) < this->_eta * .0001 && 
				fabs(this->_phi - j2._phi) < this->_phi * .0001 && 
				fabs(this->_charge - j2._charge) < this->_charge * .0001 &&
				fabs(this->_mass - j2._mass) < this->_mass * .0001);
	}
	
#ifdef STANDALONE
	ClassDef(Jet, 1)
#endif
};

typedef std::vector<analysis::core::Jet> Jets;
} // namespace core
} // namespace analysis

#ifdef STANDALONE
ClassImpUnique(analysis::core::Jet, Jet)
#endif

#endif
