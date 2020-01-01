#!/bin/bash

#	for CMSSW use it's the CMSSW/src/Analysis
#	for STANDALONE use it's the build directory or for testing purposes repo
#export ANALYSISHOME=/afs/cern.ch/work/m/malhusse/private/h2mu/CMSSW_9_4_9_cand2/src/HMuMu
#export ANALYSISHOME=/afs/cern.ch/work/m/malhusse/private/higgsmumu/h2mu17/CMSSW_9_4_13/src/HMuMu
export ANALYSISHOME=/uscms/home/malhusse/nobackup/CMSSW_9_4_13/src/HMuMu
#/afs/cern.ch/work/m/malhusse/private/h2mu/CMSSW_9_4_13/src/HMuMu
#export PYTHONPATH=$ANALYSISHOME:$PYTHONPATH
echo "ANALYSIS HOME is now at $ANALYSISHOME"
#echo $PYTHONPATH
