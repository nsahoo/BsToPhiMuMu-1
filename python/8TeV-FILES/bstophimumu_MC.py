
################
#  variables
################
runMC               = True
run2012not2011      = True  # True for 2012 and False for 2011

print "\n@@@ CMSSW run configuration flags @@@"

if (runMC == True):
    print " running MC : ", runMC
else:
    print " not running MC, please xCheck !!"

if (run2012not2011 == True):
    print "---> 2012 MC running"
else:
    print "---> 2011 MC running"

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"

##################
# cmssw configs
##################

import FWCore.ParameterSet.Config as cms
from bstophimumu_cfi import process 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
#'/store/mc/Summer12/BsToPhiMuMu_BPhiFilter_TuneZ2star_8TeV-Pythia6-evtgen/GEN-SIM/START53_V7C-v1/10000/00850D59-FB5E-E511-8DA3-047D7B881D90.root')
#'/BsToJpsiPhiV2_BFilter_TuneZ2star_8TeV-pythia6-evtgen/Summer12_DR53X-PU_RD2_START53_V19F-v3/AODSIM')
'/store/mc/Summer12_DR53X/BsToJPsiPhi_2K2MuFilter_8TeV-pythia6-evtgen/AODSIM/PU_S10_START53_V7A-v1/0000/0820A261-BEDC-E111-8748-00259073E3CE.root')
                        )

if (run2012not2011 == True):
#	process.GlobalTag.globaltag = cms.string('START53_V7C::All')
    process.GlobalTag.globaltag = cms.string('START53_V19F::All') # run dependent MC: START53_V19F , Jpsi X MC: START53_V7G
    print "\n=> Global Tag : START53_V19F::All\n"
else:
    process.GlobalTag.globaltag = cms.string('START53_LV6A1::All') # GT for 7TeV legacy samples reprocessed in cmssw_5_3_X
    print "\n=> Global Tag : START53_LV6A1::All\n"


# do trigger matching for muons
triggerProcessName = 'HLT'


if (run2012not2011 == True):
    process.cleanMuonTriggerMatchHLT  = cms.EDProducer(
            # match by DeltaR only (best match by DeltaR)
            'PATTriggerMatcherDRLessByR',
                src                   = cms.InputTag('cleanPatMuons'),
                # default producer label as defined in
                # PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
                matched               = cms.InputTag('patTrigger'),
                matchedCuts           = cms.string('path("HLT_DoubleMu3p5_LowMass_Displaced*",0,0)'),
                maxDeltaR             = cms.double(0.1),
                # only one match per trigger object
                resolveAmbiguities    = cms.bool(True),
                # take best match found per reco object (by DeltaR here, see above)
                resolveByMatchQuality = cms.bool(False))
else:
    process.cleanMuonTriggerMatchHLT1 = cms.EDProducer(
            'PATTriggerMatcherDRLessByR',
                src = cms.InputTag('cleanPatMuons'),
                # default producer label as defined in                                                                                                               
                # PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py 
                matched = cms.InputTag('patTrigger'),
                matchedCuts = cms.string('path("HLT_Dimuon7_LowMass_Displaced_v*")'),
                maxDeltaR = cms.double(0.1),
                # only one match per trigger object
                resolveAmbiguities = cms.bool(True),
                # take best match found per reco object (by DeltaR here, see above) 
                resolveByMatchQuality = cms.bool(False))

    process.cleanMuonTriggerMatchHLT2 = cms.EDProducer(
            'PATTriggerMatcherDRLessByR',
                src = cms.InputTag('cleanPatMuons'),
                matched = cms.InputTag('patTrigger'),
                matchedCuts = cms.string('path("HLT_DoubleMu4_LowMass_Displaced_v*")'),
                maxDeltaR = cms.double(0.1),
                resolveAmbiguities = cms.bool(True),
                resolveByMatchQuality = cms.bool(False))

    process.cleanMuonTriggerMatchHLT3 = cms.EDProducer(
            'PATTriggerMatcherDRLessByR',
                src = cms.InputTag('cleanPatMuons'),
                matched = cms.InputTag('patTrigger'),
                matchedCuts = cms.string('path("HLT_DoubleMu4p5_LowMass_Displaced_v*")'),
                maxDeltaR = cms.double(0.1),
                resolveAmbiguities = cms.bool(True),
                resolveByMatchQuality = cms.bool(False))

    process.cleanMuonTriggerMatchHLT4 = cms.EDProducer(
            'PATTriggerMatcherDRLessByR',
                src = cms.InputTag('cleanPatMuons'),
                matched = cms.InputTag('patTrigger'),
                matchedCuts = cms.string('path("HLT_DoubleMu5_LowMass_Displaced_v*")'),
                maxDeltaR = cms.double(0.1),
                resolveAmbiguities = cms.bool(True),
                resolveByMatchQuality = cms.bool(False))
    
    

from PhysicsTools.PatAlgos.tools.trigTools import *

if (run2012not2011 == True):
    switchOnTriggerMatchEmbedding(process, triggerMatchers = ['cleanMuonTriggerMatchHLT'], hltProcess = triggerProcessName, outputModule = '')
    
    g_TriggerNames_LastFilterNames = [
        ('HLT_DoubleMu3p5_LowMass_Displaced',  'hltDisplacedmumuFilterDoubleMu3p5LowMass')  #5E32, v8.1-v8.3
        ]
    
else:
    switchOnTriggerMatchEmbedding(process, triggerMatchers = ['cleanMuonTriggerMatchHLT1','cleanMuonTriggerMatchHLT2','cleanMuonTriggerMatchHLT3','cleanMuonTriggerMatchHLT4'], hltProcess = triggerProcessName, outputModule = '')
    
    g_TriggerNames_LastFilterNames = [
            ('HLT_Dimuon7_LowMass_Displaced',
             'hltDisplacedmumuFilterLowMass'), #1E33, 1.4E33

            ('HLT_DoubleMu4_LowMass_Displaced',
             'hltDisplacedmumuFilterLowMass'), #2E33

            ('HLT_DoubleMu4p5_LowMass_Displaced',
             'hltDisplacedmumuFilterDoubleMu4p5LowMass'), #3E33, 5E33

            ('HLT_DoubleMu5_LowMass_Displaced',
             'hltDisplacedmumuFilterDoubleMu5LowMass'), #3E33, 5E33
            ]
    


    
g_TriggerNames = [i[0] for i in g_TriggerNames_LastFilterNames]
g_LastFilterNames = [i[1] for i in g_TriggerNames_LastFilterNames]

process.ntuple.TriggerNames = cms.vstring(g_TriggerNames)
process.ntuple.LastFilterNames = cms.vstring(g_LastFilterNames)
process.ntuple.IsMonteCarlo = cms.untracked.bool(True)
