# Topic Ingestion Backlog

Topics queued for ingestion into `knowledge/topics/`. See
[`docs/knowledge-pipeline.md`](../docs/knowledge-pipeline.md) for how this
file is maintained.

**Structure:**
- Sections match the Skill Content Areas table in `docs/PRD.md`.
- Every topic cites at least one authoritative source (typically a
  tfresource.org page or a tier-1 source from `sources.yaml`).
- Topics without a tier-1/2 source are listed under "Gaps" and must be
  resolved (either drop the topic or find a source) before ingestion.

**Columns:**
- **Topic** — how a practitioner would ask about it
- **Source** — citation justifying inclusion (tfresource page id, or `sources.yaml` id)
- **Personas** — analyst (a), developer (d), researcher (r), reviewer (rv)
- **Priority** — P1 (PRD Phase 1 core), P2 (Phase 2 depth), P3 (Phase 3 extended)

**Last regenerated:** 2026-04-14 from tfresource.org topic index.

---

## Pilot (next up)

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Gravity Model (Trip Distribution) | tfresource/Spatial_Interaction_Models, fhwa-tmv-manual | a, d, r, rv | P1 |
| Activity-Based Models — Overview | tfresource/Activity_Based_Models | a, d, r, rv | P1 |

## Terminology & Basic Theories

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Choice Models (Random Utility) | tfresource/Choice_models | d, r | P1 |
| Utility Functions | tfresource/Utility | d, r | P1 |
| Value of Time | tfresource/Pricing_and_valuation | a, d, rv | P1 |
| Trip vs. Tour vs. Activity | tfresource/Tour-based_models (cross-ref) | a, d, r, rv | P1 |
| Production / Attraction vs. Origin / Destination | tfresource/Trip_generation | a, rv | P1 |
| Elasticities | tfresource/Elasticities | a, d, r, rv | P1 |
| Impedance | tfresource/Impedance | d | P1 |
| Spatial Interaction Fundamentals | tfresource/Spatial_interaction_models | d, r | P1 |
| Destination Choice Theory | tfresource (destination choice sub-pages) | d, r | P2 |

## Travel Model Structures

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| 4-Step Model Overview | tfresource (trip-based models category) | a, d, r, rv | P1 |
| Trip Generation | tfresource/Trip_generation | a, d, r, rv | P1 |
| Trip Distribution | tfresource/Trip_distribution | a, d, r, rv | P1 |
| Mode Choice | tfresource/Mode_choice | a, d, r, rv | P1 |
| Traffic Assignment (UE, SUE, DTA) | tfresource/Network_assignment | a, d, r, rv | P1 |
| Activity-Based Model Components | tfresource/Activity_Based_Models | d, r | P1 |
| ActivitySim Platform | activitysim-docs, tfresource | d | P2 |
| CT-RAMP Platform | tfresource/CT-RAMP | d | P2 |
| MATSim Platform | tfresource/MATSim | d, r | P3 |
| Strategic / Sketch Planning Models | tfresource/Sketch_planning | a, rv | P2 |
| Tour-Based Models | tfresource/Tour-based_models | d, r | P2 |
| Direct-Demand / Regression Models | tfresource/Regression | a, rv | P2 |
| Dynamic Traffic Assignment | tfresource/Dynamic_traffic_assignment | d, r | P2 |

## Networks

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Traffic Analysis Zones (TAZ/MAZ) | tfresource/Traffic_analysis_zones | a, d, r, rv | P1 |
| Highway Network Coding | tfresource/Highway_networks | d | P1 |
| Transit Network Coding | tfresource/Transit_networks | d | P1 |
| Volume-Delay Functions | tfresource/User_equilibrium (speed-flow) | d, rv | P1 |
| Path Finding | tfresource/Path_finding | d | P2 |
| Managed / HOT / HOV Lanes | tfresource/Tolling_and_pricing | a, d | P2 |
| Transit Service & Frequency | tfresource/Transit_service | d | P2 |
| Network Scenarios & Versioning | tfresource (no dedicated page — gap) | a, d | P2 |

## Surveys & Data

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Household Travel Surveys — Overview | tfresource/Household_travel_surveys | a, d, r, rv | P1 |
| GPS-Enabled Surveys | tfresource/GPS-enabled_surveys | d, r | P1 |
| NHTS | tfresource + nhts | a, d, r, rv | P1 |
| On-Board Transit Surveys | tfresource/On-board_surveys | d, r | P2 |
| Commercial Vehicle / Establishment Surveys | tfresource/Establishment_surveys | d, r | P2 |
| Passive / Big Data | tfresource/Big_data, tfresource/Cellular_data | a, d, r, rv | P1 |
| Stated Preference Surveys | tfresource/Stated_preference | r | P2 |
| Traffic & Transit Counts | tfresource/Traffic_counts | a, d, rv | P1 |
| Parking Surveys | tfresource/Parking_surveys | d, r | P3 |
| Census / ACS / CTPP / LODES | tfresource (limited) + US Census | a, d, rv | P1 |

## Validation & Calibration

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Model Validation & Reasonableness Checking — Overview | tfresource/Model_Validation_and_Reasonableness_Checking, fhwa-tmv-manual | a, d, r, rv | P1 |
| Calibration Methods | tfresource/Model_calibration | d, r | P1 |
| Screenline Validation | tfresource (validation sub-pages) | a, d, rv | P1 |
| RMSE / %RMSE / GEH Statistics | tfresource (empirical accuracy) | d, rv | P1 |
| Trip Length Frequency Distribution Validation | tfresource (validation sub-pages) | d, rv | P1 |
| Transit Boarding Validation | tfresource (validation sub-pages) | a, d, rv | P1 |
| Convergence Criteria | tfresource/User_equilibrium | d, rv | P1 |
| Sensitivity Testing | tfresource/Plausibility_assessment | a, d, rv | P1 |
| Quality Assurance | tfresource/Quality_assurance | d, rv | P2 |
| Backcasting / Trend Validation | tfresource/Empirical_accuracy | rv | P2 |

## Forecasting & Application

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Project-Level Traffic Forecasting | tfresource/Project-level_traffic_forecasting | a, rv | P1 |
| Scenario Analysis & Alternatives | tfresource/Scenario_analysis | a, d, rv | P1 |
| FTA New Starts — Travel Forecast Requirements | tfresource/New_Starts, fta-new-starts | a, rv | P1 |
| Forecasting under Uncertainty | tfresource/Uncertainty_modeling | a, d, r, rv | P2 |
| Statewide Models | tfresource/Statewide_models | a, rv | P2 |
| NEPA / Environmental Review | tfresource (limited — partial gap) | a, rv | P2 |
| Model Transferability | tfresource/Model_transferability | d, r | P2 |
| Long-Distance / Intercity Travel | tfresource/Long-distance_travel | d, r | P2 |

## Phase 3 / Extended Topics

| Topic | Source | Personas | Priority |
|-------|--------|----------|----------|
| Freight & Commercial Vehicle Modeling | tfresource/Freight_modeling (multi-page) | a, d, r, rv | P3 |
| Land Use / Transport Integration | tfresource/Land_use-transport_integration | d, r | P3 |
| Pricing & Tolling Analysis | tfresource/Tolling_and_pricing | a, d, rv | P3 |
| Active Transportation Modeling | tfresource/Active_transport | a, d, r, rv | P3 |
| Autonomous / Connected Vehicles | tfresource/Autonomous_vehicles (multi-page) | a, d, r, rv | P3 |
| Equity Analysis in Travel Models | tfresource/Equity_analysis | a, rv | P3 |
| Synthetic Populations | tfresource/Synthetic_populations | d, r | P3 |
| Dynamic Network Integration | tfresource/Dynamic_network_integration | d, r | P3 |

## Gaps

Topics or PRD subtopics that lack a clear tier-1 source in the current
manifest. Each must either be dropped or paired with a source before
ingestion.

| Topic | Why it's a gap | Resolution path |
|-------|----------------|-----------------|
| Network scenarios & versioning | No dedicated tfresource page; practice varies by software vendor | Pull from vendor docs (Cube, EMME, TransCAD) as tier-2 sources |
| Census / ACS / CTPP / LODES detail | tfresource coverage is thin | Cite US Census Bureau directly as a tier-1 government source |
| NEPA / environmental review | Limited tfresource material | Cite FHWA NEPA guidance as tier-1 source |
| Managed lanes coding practice | tfresource covers pricing theory, not coding | Likely agency-specific; possibly gap until a source is identified |

## Cross-cutting tfresource content not yet categorized

The 2026-04-14 tfresource enumeration surfaced additional pages worth
considering in future passes:

- Advanced theoretical extensions (joint travel behavior, market
  segmentation, Markov models, iterative proportional fitting)
- Software / tool pages (commercial packages, estimation software)
- Case studies (Dallas, Georgia, Maryland)
- Reference material (glossary, curriculum, webinars)

These may be incorporated as supplementary material on specific topic notes
rather than standalone topics.

## Done

Move approved topics here with the commit SHA or PR that approved them.
