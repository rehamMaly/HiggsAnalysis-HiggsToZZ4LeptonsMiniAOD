import FWCore.ParameterSet.Config as cms

hTozzTo4leptonsEventContentReduced = cms.PSet(
    outputCommands = cms.untracked.vstring(
'keep *_*_*_*',
'drop *_source_*_*',
'drop *_generator_*_*',
'drop *_*GenJets*_*_*',
'keep *_*genMet*_*_*',
'keep *_TriggerResults_*_*',
'keep *_hltTriggerSummaryAOD_*_*',
'drop *_clusterSummaryProducer_*_*',
'drop *_*Digi*_*_*',
'drop *_hcalnoise_*_*',
'drop *_l1*_*_*',
'drop *_fixedGridRhoAll_*_*',
'drop *_fixedGridRhoFastjetAll_*_*',
'drop *_*TrackJets_*_*',
'drop *_*BasicJets_*_*',
'drop *_ak5CaloJets_rho_*',
'drop *_ak5PFJets_rho_*',
'drop *_ak7CaloJets_rho_*',
'drop *_ak7PFJets_rho_*',
'drop *_kt4CaloJets_rho_*',
'drop *_kt4PFJets_rho_*',
'drop *_kt6CaloJets_rho_*',
'drop *_kt6CaloJetsCentral_rho_*',
'keep *_kt6PFJets_rho_*',
'drop *_kt6PFJetsCentralChargedPileUp_rho_*',
'keep *_kt6PFJetsCentralNeutral_rho_*',
'drop *_kt6PFJetsCentralNeutralTight_rho_*',
'drop *_ak5CaloJets_sigma_*',
'drop *_ak5PFJets_sigma_*',
'drop *_ak7CaloJets_sigma_*',
'drop *_ak7PFJets_sigma_*',
'drop *_kt4CaloJets_sigma_*',
'drop *_kt4PFJets_sigma_*',
'drop *_kt6CaloJets_sigma_*',
'drop *_kt6CaloJetsCentral_sigma_*',
'drop *_kt6PFJets_sigma_*',
'drop *_kt6PFJetsCentralChargedPileUp_sigma_*',
'drop *_kt6PFJetsCentralNeutral_sigma_*',
'drop *_kt6PFJetsCentralNeutralTight_sigma_*',
'drop *_*_combinedSecondaryVertexBJetTags_*',
'drop *_*_combinedSecondaryVertexMVABJetTags_*',
'drop *_combinedSecondaryVertexMVABJetTags_*_*',
'drop *_*_ghostTrackBJetTags_*',
'drop *_ghostTrackBJetTags_*_*',
'drop *_*_jetBProbabilityBJetTags_*',
'drop *_*_jetProbabilityBJetTags_*',
'drop *_jet*ProbabilityBJetTags_*_*',
'drop *_*_simpleSecondaryVertexHighEffBJetTags_*',
'drop *_*_simpleSecondaryVertexHighPurBJetTags_*',
'drop *_simpleSecondaryVertexHigh*BJetTags_*_*',
'drop *_*_softElectronByIP3dBJetTags_*',
'drop *_*_softElectronByPtBJetTags_*',
'drop *_*_softMuonB*Tags_*',
'drop *_soft*BJetTags_*_*',
'drop *_*_trackCountingHighEffBJetTags_*',
'drop *_*_trackCountingHighPurBJetTags_*',
'drop *_*_ak5JetExtender_*',
'drop *_*_ak7JetExtender_*',
'drop *_*_kt4JetExtender_*',
'drop *_*JetExtender_*_*',
'drop *_*_conditionsInEdm_*',
'drop *_conditionsInEdm_*_*',
'drop *_*_towerMaker_*',
'drop *_*_castorreco_*',
'drop *_castorreco_*_*',
'drop *_*_reducedEcalRecHitsEB_*',
'drop *_*_reducedEcalRecHitsEE_*',
'drop *_*_reducedEcalRecHitsES_*',
'drop *_*_reducedHcalRecHits_*',
'drop *_*_reducedHcalRecHits_*',
'drop *_*_reducedHcalRecHits_*',
'drop *_PhotonIDProd_*_*',
'drop *_eidLoose_*_*',
'drop *_eidRobustHighEnergy_*_*',
'drop *_eidRobustLoose_*_*',
'drop *_eidRobustTight_*_*',
'drop *_eidTight_*_*',
'drop *_ak7CastorJetID_*_*',
'drop *_dedxDiscrimASmi_*_*',
'drop *_dedxHarmonic2_*_*',
'drop *_ak5JetID_*_*',
'drop *_ak7JetID_*_*',
'drop *_kt4JetID_*_*',
'drop *_kt6JetID_*_*',
'drop *_muons_combined_*',
'drop *_muons_csc_*',
'drop *_muons_dt_*',
'drop *_BeamHaloSummary_*_*',
'keep *_offlineBeamSpot_*_*',
'drop *_GlobalHaloData_*_*',
'drop *_scalersRawToDigi_*_*',
'drop *_scalersRawToDigi_*_*',
'drop *_scalersRawToDigi_*_*',
'drop *_scalersRawToDigi_*_*',
'drop *_scalersRawToDigi_*_*',
'drop *_scalersRawToDigi_*_*',
'drop *_logErrorHarvester_*_*',
'drop *_ak7BasicJets_*_*',
'drop *_pfElectronTranslator_pf_*',
'keep *_pfElectronTranslator_pf_*',
'drop *_pfPhotonTranslator_pfphot_*',
'drop *_ak5CaloJets_*_*',
'keep *_ak5CaloJets_*_*',
'drop *_ak7CaloJets_*_*',
'drop *_kt4CaloJets_*_*',
'drop *_kt6CaloJets_*_*',
'drop *_corMetGlobalMuons_*_*',
'keep *_corMetGlobalMuons_*_*',
'drop *_met_*_*',
'keep *_met_*_*',
'drop *_metHO_*_*',
'drop *_metNoHF_*_*',
'drop *_CastorTowerReco_*_*',
'drop *_allConversions_*_*',
'drop *_conversions_*_*',
'drop *_uncleanedOnlyAllConversions_*_*',
'drop *_pfPhotonTranslator_pfphot_*',
'drop *_JetPlusTrackZSPCorJetAntiKt5_*_*',
'drop *_htMetAK5_*_*',
'drop *_htMetAK7_*_*',
'drop *_htMetIC5_*_*',
'drop *_htMetKT4_*_*',
'drop *_htMetKT6_*_*',
'drop *_tcMet_*_*',
'keep *_tcMet_*_*',
'drop *_tcMetWithPFclusters_*_*',
'drop *_muonsFromCosmics*_*_*',
'keep *_particleFlow_*_*',
'drop *_particleFlowTmp_*_*',
'drop *_ak5PFJets_*_*',
'keep *_ak5PFJets_*_*',
'drop *_ak7PFJets_*_*',
'drop *_kt4PFJets_*_*',
'keep *_kt6PFJets_rho_*',
'drop *_ak5CaloJets_sigma_*',
'drop *_ak5PFJets_sigma_*',
'drop *_ak5CaloJets_rhos_*',
'drop *_ak5PFJets_rhos_*',
'drop *_ak5TrackJets_rhos_*',
'drop *_ak7BasicJets_rhos_*',
'drop *_ak7CaloJets_rhos_*',
'drop *_ak7PFJets_rhos_*',
'drop *_kt4CaloJets_rhos_*',
'drop *_kt4PFJets_rhos_*',
'drop *_kt6CaloJets_rhos_*',
'drop *_kt6PFJets_rhos_*',
'drop *_ak5CaloJets_sigmas_*',
'drop *_ak5PFJets_sigmas_*',
'drop *_ak5TrackJets_sigmas_*',
'drop *_ak7BasicJets_sigmas_*',
'drop *_ak7CaloJets_sigmas_*',
'drop *_ak7PFJets_sigmas_*',
'drop *_kt4CaloJets_sigmas_*',
'drop *_kt4PFJets_sigmas_*',
'drop *_kt6CaloJets_sigmas_*',
'drop *_kt6PFJets_sigmas_*',
'drop *_ak5JetTracksAssociatorAtVertex_*_*',
'drop *_ak*JetTracksAssociatorAtVertex_*_*',
'drop *_pfMet_*_*',
'keep *_pfMet_*_*',
'drop *_particleFlowCluster*_Cleaned_*',
'drop *_photons_*_*',
'keep *_photons_*_*',
'drop *_pfPhotonTranslator_pfphot_*',
'drop *_photonCore_*_*',
'drop *_pfPhotonTranslator_pfphot_*',
'drop *_pfElectronTranslator_pf_*',
'keep *_pfElectronTranslator_pf_*',
'drop *_pfPhotonTranslator_pfphot_*',
'drop *_multi5x5*_*_*',
'keep *_multi5x5*_*_*',
'drop *_trackRefsForJets_*_*',
'drop *_pfElectronTranslator_pf_*',
'keep *_pfElectronTranslator_pf_*',
'drop *_pfPhotonTranslator_pfphot_*',
'drop *_ckfInOutTracksFromConversions_*_*',
'drop *_ckfOutInTracksFromConversions_*_*',
'drop *_conversionStepTracks_*_*',
'drop *_cosmicMuons_*_*',
'drop *_cosmicMuons1Leg_*_*',
'drop *_generalTracks_*_*',
'keep *_generalTracks_*_*',
'drop *_globalCosmicMuons_*_*',
'drop *_globalCosmicMuons1Leg_*_*',
'drop *_regionalCosmicTracks_*_*',
'drop *_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
'drop *_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
'keep *_refittedStandAloneMuons_UpdatedAtVtx_*',
'keep *_standAloneMuons_UpdatedAtVtx_*',
'drop *_tevMuons_*_*',
'drop *_trackExtrapolator_*_*',
'keep *_offlineSlimmedPrimaryVertices*_*_*',
'drop *_generalV0Candidates_*_*',
'drop *_*Tau*_*_*',
'drop *_*particleFlowRecHit*_*_*'
)
)
hTozzTo4leptonsEventSelection = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsPreselectionPath')
    )
)
hTozzTo4leptonsEventOffSelection = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsOfflineselectionPath')
    )
)
hTozzTo4leptonsEventCompleteSelection = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsSelectionPath')
    )
)

hTozzTo4leptonsEventCompleteSelectionTwoeTwomu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsSelectionPath2e2mu')
    )
)

hTozzTo4leptonsEventCompleteSelection4e = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsSelectionPath4e')
    )
)

hTozzTo4leptonsEventCompleteSelection4mu = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsSelectionPath4mu')
    )
)
