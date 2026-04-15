# Topic Ingestion Backlog

Topics queued for ingestion into `knowledge/topics/`. See
[`docs/knowledge-pipeline.md`](../docs/knowledge-pipeline.md) for how this
file is maintained and how topics nest.

**Structure:**

- Sections match the PRD's Skill Content Areas (see `docs/PRD.md`).
- The **Parent** column shows the parent topic's id (or `—` if this topic
  is top-level within its area). This lets the file encode hierarchy
  while staying scannable.
- Every topic cites at least one authoritative source. Topics without a
  tier-1/2 source live under "Gaps" and must be resolved before ingestion.

**Columns:**

- **Topic** — how a practitioner would ask about it; `↳` prefixes are visual cues
- **Id** — kebab-case identifier used as frontmatter `id` and citation token
- **Parent** — parent topic id, or `—` for area-top-level
- **Source** — citation justifying inclusion
- **Personas** — a=analyst, d=developer, r=researcher, rv=reviewer
- **Pri** — P1 (PRD Phase 1), P2 (Phase 2), P3 (Phase 3)

**Last regenerated:** 2026-04-14 from tfresource.org topic index and PRD v2.

**Legacy starting material:** `knowledge/_unverified/legacy-skill-content.md`
holds the pre-pipeline SKILL.md body. It is NOT approved knowledge.
Drafters may use it as a starting draft but must verify every claim against
tier-1 sources before the new topic note can reach `status: approved`.

---

## Pilot (next up)

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Trip Distribution | `trip-distribution` | `aggregate-demand-overview` | tfresource/Spatial_Interaction_Models, fhwa-tmv-manual | a, d, r, rv | P1 |
| Activity-Based Models — Overview | `microsimulated-demand-overview` | — | tfresource/Activity_Based_Models | a, d, r, rv | P1 |

## Terminology and Basic Theories

Area: `terminology`. All rows here have `topic_area: terminology`.

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Econometric Choice Models | `econometric-choice-models` | — | tfresource/Choice_models | d, r | P1 |
| &nbsp;&nbsp;↳ Utility Functions | `utility-functions` | `econometric-choice-models` | tfresource/Utility | d, r | P1 |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ Value of Time | `value-of-time` | `utility-functions` | tfresource/Pricing_and_valuation | a, d, rv | P1 |
| Spatial Interaction Fundamentals | `spatial-interaction-fundamentals` | — | tfresource/Spatial_interaction_models | d, r | P1 |
| &nbsp;&nbsp;↳ Destination Choice Theory | `destination-choice-theory` | `spatial-interaction-fundamentals` | tfresource (destination choice sub-pages) | d, r | P2 |
| Production / Attraction vs. Origin / Destination | `production-vs-origin` | — | tfresource/Trip_generation | a, rv | P1 |
| Trip vs. Tour vs. Activity | `trip-tour-activity` | `microsimulated-demand-overview` | tfresource/Tour-based_models (cross-ref) | a, d, r, rv | P1 |
| Elasticities | `elasticities` | — | tfresource/Elasticities | a, d, r, rv | P1 |
| Impedance | `impedance` | — | tfresource/Impedance | d | P1 |

## Travel Model Structures

Area: `model-structures`. Has five subareas (model types), each ingested
as its own top-level-within-area umbrella note plus child notes.

### Umbrella

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Travel Model Structures — Overview | `model-structures-overview` | — | tfresource (model types index) | a, d, r, rv | P1 |

### Strategic Planning Models

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Strategic / Sketch Planning Models | `strategic-planning` | `model-structures-overview` | tfresource/Sketch_planning | a, rv | P2 |

### Network Metric Models

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Network Metric Models — Overview | `network-metric-models` | `model-structures-overview` | tfresource (accessibility, reliability topics) | a, rv | P2 |
| &nbsp;&nbsp;↳ Accessibility Metrics | `accessibility-metrics` | `network-metric-models` | tfresource/Accessibility | a, r, rv | P2 |
| &nbsp;&nbsp;↳ Congestion Metrics | `congestion-metrics` | `network-metric-models` | tfresource (congestion-related pages) | a, rv | P2 |
| &nbsp;&nbsp;↳ Reliability Metrics | `reliability-metrics` | `network-metric-models` | tfresource (reliability-related pages) | a, d, rv | P2 |

### Direct-Demand Models

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Direct-Demand / Regression Models | `direct-demand-models` | `model-structures-overview` | tfresource/Regression | a, rv | P2 |

### Aggregate Demand Models (4-Step)

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| 4-Step Model — Overview | `aggregate-demand-overview` | `model-structures-overview` | tfresource (trip-based models category) | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ Trip Generation | `trip-generation` | `aggregate-demand-overview` | tfresource/Trip_generation | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ Trip Distribution | `trip-distribution` | `aggregate-demand-overview` | tfresource/Trip_distribution, fhwa-tmv-manual | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ Mode Choice | `mode-choice` | `aggregate-demand-overview` | tfresource/Mode_choice | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ Traffic Assignment | `traffic-assignment` | `aggregate-demand-overview` | tfresource/Network_assignment | a, d, r, rv | P1 |

### Microsimulated Demand Models (Activity-Based)

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Activity-Based Models — Overview | `microsimulated-demand-overview` | `model-structures-overview` | tfresource/Activity_Based_Models | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ ABM Components | `abm-components` | `microsimulated-demand-overview` | tfresource (ABM sub-pages) | d, r | P1 |
| &nbsp;&nbsp;↳ Tour-Based Modeling | `tour-based-modeling` | `microsimulated-demand-overview` | tfresource/Tour-based_models | d, r | P2 |
| &nbsp;&nbsp;↳ Dynamic Traffic Assignment | `dynamic-traffic-assignment` | `microsimulated-demand-overview` | tfresource/Dynamic_traffic_assignment | d, r | P2 |
| &nbsp;&nbsp;↳ ActivitySim Platform | `activitysim-platform` | `microsimulated-demand-overview` | activitysim-docs, tfresource | d | P2 |
| &nbsp;&nbsp;↳ CT-RAMP Platform | `ct-ramp-platform` | `microsimulated-demand-overview` | tfresource/CT-RAMP | d | P2 |
| &nbsp;&nbsp;↳ MATSim Platform | `matsim-platform` | `microsimulated-demand-overview` | tfresource/MATSim | d, r | P3 |

## Network Data and Structures

Area: `networks`.

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| TAZ / MAZ Systems | `taz-maz-systems` | — | tfresource/Traffic_analysis_zones | a, d, r, rv | P1 |
| Highway Network Coding | `highway-networks` | — | tfresource/Highway_networks | d | P1 |
| &nbsp;&nbsp;↳ Volume-Delay Functions | `volume-delay-functions` | `highway-networks` | tfresource/User_equilibrium | d, rv | P1 |
| &nbsp;&nbsp;↳ Managed / HOT / HOV Lanes | `managed-lanes` | `highway-networks` | tfresource/Tolling_and_pricing | a, d | P2 |
| Transit Network Coding | `transit-networks` | — | tfresource/Transit_networks | d | P1 |
| &nbsp;&nbsp;↳ Transit Service & Frequency | `transit-service` | `transit-networks` | tfresource/Transit_service | d | P2 |
| Path Finding | `path-finding` | — | tfresource/Path_finding | d | P2 |
| Network Scenarios & Versioning | `network-scenarios` | — | **GAP** — no dedicated tfresource page | a, d | P2 |

## Surveys

Area: `surveys`.

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Household Travel Surveys — Overview | `household-travel-surveys` | — | tfresource/Household_travel_surveys | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ GPS-Enabled Surveys | `gps-enabled-surveys` | `household-travel-surveys` | tfresource/GPS-enabled_surveys | d, r | P1 |
| &nbsp;&nbsp;↳ NHTS | `nhts` | `household-travel-surveys` | tfresource + nhts | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ Stated Preference | `stated-preference` | `household-travel-surveys` | tfresource/Stated_preference | r | P2 |
| On-Board Transit Surveys | `onboard-surveys` | — | tfresource/On-board_surveys | d, r | P2 |
| Commercial Vehicle / Establishment Surveys | `establishment-surveys` | — | tfresource/Establishment_surveys | d, r | P2 |
| Passive / Big Data | `passive-big-data` | — | tfresource/Big_data, tfresource/Cellular_data | a, d, r, rv | P1 |
| Traffic & Transit Counts | `traffic-counts` | — | tfresource/Traffic_counts | a, d, rv | P1 |
| Census / ACS / CTPP / LODES | `census-acs-lodes` | — | tfresource (limited) + US Census | a, d, rv | P1 |
| Parking Surveys | `parking-surveys` | — | tfresource/Parking_surveys | d, r | P3 |

## Validation & Calibration

Area: `validation`.

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Validation & Reasonableness — Overview | `validation-overview` | — | tfresource/Model_Validation_and_Reasonableness_Checking, fhwa-tmv-manual | a, d, r, rv | P1 |
| &nbsp;&nbsp;↳ Calibration Methods | `calibration-methods` | `validation-overview` | tfresource/Model_calibration | d, r | P1 |
| &nbsp;&nbsp;↳ Screenline Validation | `screenline-validation` | `validation-overview` | tfresource (validation sub-pages) | a, d, rv | P1 |
| &nbsp;&nbsp;↳ RMSE / %RMSE / GEH | `rmse-geh-statistics` | `validation-overview` | tfresource (empirical accuracy) | d, rv | P1 |
| &nbsp;&nbsp;↳ Trip Length Frequency Validation | `trip-length-validation` | `validation-overview` | tfresource (validation sub-pages) | d, rv | P1 |
| &nbsp;&nbsp;↳ Transit Boarding Validation | `transit-boarding-validation` | `validation-overview` | tfresource (validation sub-pages) | a, d, rv | P1 |
| &nbsp;&nbsp;↳ Convergence Criteria | `convergence-criteria` | `validation-overview` | tfresource/User_equilibrium | d, rv | P1 |
| &nbsp;&nbsp;↳ Sensitivity Testing | `sensitivity-testing` | `validation-overview` | tfresource/Plausibility_assessment | a, d, rv | P1 |
| &nbsp;&nbsp;↳ Quality Assurance | `quality-assurance` | `validation-overview` | tfresource/Quality_assurance | d, rv | P2 |
| &nbsp;&nbsp;↳ Backcasting / Trend Validation | `backcasting` | `validation-overview` | tfresource/Empirical_accuracy | rv | P2 |

## Forecasting

Area: `forecasting`.

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Project-Level Traffic Forecasting | `project-level-forecasting` | — | tfresource/Project-level_traffic_forecasting | a, rv | P1 |
| Scenario Analysis & Alternatives | `scenario-analysis` | — | tfresource/Scenario_analysis | a, d, rv | P1 |
| FTA New Starts Requirements | `fta-new-starts-requirements` | — | tfresource/New_Starts, fta-new-starts | a, rv | P1 |
| Forecasting under Uncertainty | `forecasting-uncertainty` | — | tfresource/Uncertainty_modeling | a, d, r, rv | P2 |
| Statewide Models | `statewide-models` | — | tfresource/Statewide_models | a, rv | P2 |
| NEPA / Environmental Review | `nepa-review` | — | **PARTIAL GAP** — cite FHWA NEPA guidance | a, rv | P2 |
| Model Transferability | `model-transferability` | — | tfresource/Model_transferability | d, r | P2 |
| Long-Distance / Intercity Travel | `long-distance-travel` | — | tfresource/Long-distance_travel | d, r | P2 |

## Extended Topics (Phase 3)

Area: `extended`.

| Topic | Id | Parent | Source | Personas | Pri |
|-------|----|--------|--------|----------|-----|
| Freight & Commercial Vehicle Modeling | `freight-modeling` | — | tfresource/Freight_modeling | a, d, r, rv | P3 |
| Land Use / Transport Integration | `land-use-transport` | — | tfresource/Land_use-transport_integration | d, r | P3 |
| Pricing & Tolling Analysis | `pricing-tolling` | — | tfresource/Tolling_and_pricing | a, d, rv | P3 |
| Active Transportation Modeling | `active-transportation` | — | tfresource/Active_transport | a, d, r, rv | P3 |
| Autonomous / Connected Vehicles | `autonomous-vehicles` | — | tfresource/Autonomous_vehicles | a, d, r, rv | P3 |
| Equity Analysis | `equity-analysis` | — | tfresource/Equity_analysis | a, rv | P3 |
| Synthetic Populations | `synthetic-populations` | — | tfresource/Synthetic_populations | d, r | P3 |
| Dynamic Network Integration | `dynamic-network-integration` | — | tfresource/Dynamic_network_integration | d, r | P3 |

## Gaps

Topics that lack a clear tier-1 source and need resolution before ingestion.

| Topic Id | Why it's a gap | Resolution path |
|----------|----------------|-----------------|
| `network-scenarios` | No dedicated tfresource page; practice varies by software | Pull from vendor docs (Cube, EMME, TransCAD) as tier-2 sources |
| `census-acs-lodes` (partial) | tfresource coverage is thin | Cite US Census Bureau directly as tier-1 |
| `nepa-review` | Limited tfresource material | Cite FHWA NEPA guidance as tier-1 |
| `managed-lanes` (coding practice) | tfresource covers pricing theory, not network coding | Likely agency-specific; possibly gap until a source is identified |

## Cross-cutting tfresource content not yet categorized

The 2026-04-14 tfresource enumeration surfaced 119 pages that don't fit
cleanly into the PRD areas. They may be incorporated as supplementary
material on specific topic notes rather than standalone topics:

- Advanced theoretical extensions (joint travel behavior, market
  segmentation, iterative proportional fitting)
- Software / tool pages (commercial packages, estimation software)
- Case studies (Dallas, Georgia, Maryland)
- Reference material (glossary, curriculum, webinars)

## Done

Move approved topics here with the commit SHA or PR that approved them.
