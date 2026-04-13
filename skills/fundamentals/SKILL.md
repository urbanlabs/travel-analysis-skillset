---
name: travel-demand-fundamentals
description: Travel demand modeling fundamentals for transportation planners
trigger: When the user asks about travel demand models, trip-based models, activity-based models, travel surveys, model validation, calibration, traffic assignment, mode choice, trip generation, trip distribution, or related transportation planning and forecasting topics.
---

You are an expert in travel demand modeling with deep knowledge of both traditional 4-step models and modern activity-based approaches. You provide practical, practitioner-oriented guidance for transportation planners.

When responding, be direct and actionable. Reference tfresource.org pages for deeper reading where relevant (use the format `https://tfresource.org/topics/PAGE_NAME.html`).

## 4-Step Travel Demand Model Framework

The 4-step (trip-based) model is the foundational framework used by most metropolitan planning organizations (MPOs) for regional travel forecasting.

### Step 1: Trip Generation

Determines how many trips are produced by and attracted to each traffic analysis zone (TAZ).

**Productions** are typically modeled at the household level using:
- Cross-classification (household size x vehicles x workers) - most common
- Regression models
- Rates from ITE Trip Generation (site-level, not regional)

**Attractions** are modeled based on employment and land use:
- Employment by type (retail, office, industrial, etc.)
- School enrollment
- Households (for home-based trips returning home)

**Key concepts:**
- Productions are at the home end; attractions at the non-home end (for home-based trips)
- Trip purposes: Home-Based Work (HBW), Home-Based Other (HBO), Non-Home-Based (NHB) at minimum; many models add Home-Based Shopping, Home-Based School, etc.
- Balance productions and attractions (typically adjust attractions to match production totals)
- External trips and special generators (airports, universities, military bases) are handled separately

**Common pitfalls:**
- Confusing productions/attractions with origins/destinations
- Not properly accounting for special generators
- Using trip rates from a different region without local validation

**Reference:** https://tfresource.org/topics/Trip_Generation.html

### Step 2: Trip Distribution

Connects trip productions to trip attractions -- determines where trips go.

**Primary method: Gravity model**
- Trips between zones are proportional to productions and attractions, inversely proportional to impedance (travel time/cost)
- Friction factors (or gamma functions) calibrated from observed trip length frequency distributions
- Doubly constrained for HBW; singly constrained (production-constrained) for other purposes is common

**Alternative: Destination choice models**
- Logit-based, more behaviorally rich
- Can incorporate more variables (land use mix, accessibility measures)
- Increasingly used in newer models

**Key concepts:**
- K-factors (adjustment factors for specific zone pairs) should be used sparingly -- they indicate model specification issues
- Intrazonal trips need special handling (estimate intrazonal travel time)
- Trip length frequency distributions are the primary calibration target

**Common pitfalls:**
- Over-reliance on K-factors to force a match
- Not validating district-to-district flow patterns
- Friction factors that don't produce reasonable trip length distributions

**Reference:** https://tfresource.org/topics/Spatial_Interaction_Models.html

### Step 3: Mode Choice

Determines what mode of transportation (drive alone, carpool, transit, walk, bike, etc.) travelers use.

**Primary method: Nested logit models**
- Utility functions based on travel time, cost, and traveler characteristics
- Nesting structure typically: auto vs. transit vs. non-motorized, with sub-nests (drive alone vs. shared ride; walk access vs. drive access to transit)
- Coefficients should reflect reasonable values of time (typically $8-25/hr for work trips in 2020 dollars, varying by income)

**Key concepts:**
- Mode-specific constants capture unobserved attributes of each mode
- Value of time (VOT) is the ratio of time and cost coefficients -- critical to get right
- Transit submode detail matters: local bus, express bus, rail behave differently
- Highway level of service (LOS) and transit LOS are key inputs

**Common pitfalls:**
- Unreasonable values of time (too high overpredicts transit; too low underpredicts)
- Ignoring walk/bike modes or treating them as residual
- Not properly representing transit access/egress
- Applying mode choice before or after time-of-day factoring inconsistently

**Reference:** https://tfresource.org/topics/Mode_Choice.html

### Step 4: Traffic Assignment

Loads vehicle trips onto the highway network to determine link volumes and travel times.

**Primary methods:**
- **User Equilibrium (UE)**: Iterative process where no traveler can reduce their travel time by switching routes. Standard for planning applications.
- **Stochastic User Equilibrium (SUE)**: Adds perception error to path costs. More realistic but computationally heavier.
- **Static vs. Dynamic Traffic Assignment (DTA)**: Static is standard for regional models; DTA captures time-varying congestion and is used for corridor/subarea studies.

**Key concepts:**
- Volume-delay functions (BPR curves or conical functions) define speed-flow relationships
- Convergence criteria matter: relative gap < 0.01 is a minimum; < 0.001 is preferred
- Generalized cost can include tolls, distance, and reliability
- Capacity and free-flow speed coding are critical inputs

**Common pitfalls:**
- Insufficient convergence (loose convergence produces unstable link volumes)
- Wrong capacity/speed values for facility types
- Not validating against traffic counts by facility type and geographic area
- Centroid connector placement affecting nearby link volumes

**Reference:** https://tfresource.org/topics/Network_assignment.html

## Activity-Based Models (ABMs)

ABMs represent travel as derived from activity participation decisions rather than as isolated trips.

### How ABMs Differ from Trip-Based Models

| Aspect | Trip-Based | Activity-Based |
|--------|-----------|----------------|
| Unit of analysis | Trip | Tour / activity pattern |
| Population | Aggregate (zonal) | Disaggregate (synthetic persons/households) |
| Time representation | Aggregate periods | Continuous time of day |
| Consistency | Limited (steps are sequential) | Activities and travel are jointly modeled |
| Sensitivity | Limited policy sensitivity | Better sensitivity to complex policies |

### Key ABM Platforms

- **ActivitySim**: Open-source, Python-based. Growing adoption by MPOs. Consortium-governed. https://activitysim.github.io
- **CT-RAMP**: Java-based, used by several large MPOs (MTC, SANDAG, others). Developed by Parsons Brinckerhoff/WSP.
- **DAYSIM**: C++-based, microsimulation. Used by PSRC and others.

### When to Consider an ABM

- Policy questions requiring behavioral sensitivity (pricing, TDM, land use scenarios)
- Need to represent intra-household interactions
- Equity analysis requiring person-level results
- Agency has sufficient data, staff capacity, and institutional support
- Model update cycle can accommodate longer development timeline

### Practical Considerations for ABM Implementation

- Requires a robust household travel survey (minimum ~4,000-5,000 households)
- Synthetic population generation is a critical early step
- Longer run times than trip-based models (minutes vs. seconds per iteration)
- Staff training and institutional knowledge transfer are essential
- Consider a phased transition: maintain trip-based model during ABM development

**Reference:** https://tfresource.org/topics/Activity_Based_Models.html

## Data and Surveys

### Household Travel Surveys (HTS)

The foundation of travel demand model estimation and calibration.

**Key design considerations:**
- Sample size: minimum ~4,000 completed households for a regional model; more for subgroup analysis
- Survey methods: increasingly GPS-assisted smartphone surveys (rMove, RSG) supplement or replace traditional diary methods
- Survey period: typically weekday; weekend data increasingly collected
- Response rates have declined significantly; weighting and expansion are critical

**Common issues:**
- Trip underreporting (especially short trips, walk trips, and non-mandatory travel)
- GPS data needs prompted recall or imputation for trip purpose
- Seasonal variation may not be captured
- Small sample sizes for specific market segments (e.g., transit riders, low-income)

**Reference:** https://tfresource.org/topics/Household_Travel_Surveys.html

### National Household Travel Survey (NHTS)

Federal survey conducted periodically (most recent: 2022 NHTS; prior: 2017, 2009, 2001).

**Uses in practice:**
- Supplement local surveys with national data (transferable parameters)
- Benchmark local travel patterns against national trends
- Add-on program allows agencies to purchase additional local sample
- Long-distance travel data

**Reference:** https://nhts.ornl.gov

### Census and American Community Survey (ACS)

- **ACS Journey to Work**: Commute mode share, travel time, workplace flows (CTPP/LODES)
- **LODES/LEHD**: Employer-employee linked data for work trip distribution validation
- **Decennial Census**: Population and housing unit counts for base year validation

### Passive/Big Data Sources

Increasingly used to supplement traditional surveys:
- **Replica, StreetLight Data**: Trip tables and origin-destination patterns derived from mobile device data
- **Transit smart card / GTFS data**: Boarding/alighting counts and transfer patterns
- **Traffic counts (permanent and short-term)**: Highway volume validation
- **Toll/ETC data**: Facility-specific volumes and travel time

**Considerations for big data:**
- Sampling bias (not all demographic groups equally represented in mobile data)
- Validation against known ground truth is essential
- Privacy and data governance requirements
- Expansion factors and methodology transparency vary by vendor

## Model Validation and Calibration

### Calibration vs. Validation

- **Calibration**: Adjusting model parameters to reproduce observed conditions (base year)
- **Validation**: Testing whether the calibrated model produces reasonable results for data not used in calibration

### Key Validation Checks by Model Step

**Trip Generation:**
- Compare modeled trip rates to survey and NHTS benchmarks
- Check total regional productions/attractions against reasonableness

**Trip Distribution:**
- Trip length frequency distributions by purpose
- District-to-district flows against survey/ACS data
- Average trip lengths and coincidence ratios

**Mode Choice:**
- Mode shares by purpose, geography, and market segment
- Transit ridership against observed boardings by route/line
- Highway vehicle-trips against count-based vehicle-trip estimates

**Traffic Assignment:**
- Screenline volumes (modeled vs. counted)
- Percent RMSE by volume group and facility type (target: <30% for links with >10,000 AADT)
- VMT by facility type and geographic area
- Travel time validation on key corridors

### Common Validation Standards

Key references for validation targets:
- FHWA Travel Model Validation and Reasonableness Checking Manual
- State DOT model validation guidelines
- NCHRP Report 716: Travel Demand Forecasting: Parameters and Techniques

**General targets (vary by context):**
- Screenline: modeled volumes within 10% of observed totals
- Link-level percent RMSE < 40% overall, < 30% for high-volume links
- Mode shares within 1-2 percentage points of observed for major modes
- Trip length distributions should visually match observed patterns

**Common pitfalls:**
- Over-calibrating to one metric at the expense of others
- Using K-factors or link-specific adjustments that reduce transferability
- Not validating temporal distribution (AM/PM/off-peak)
- Ignoring validation of non-motorized and transit modes

**Reference:** https://tfresource.org/topics/Model_Validation_and_Reasonableness_Checking.html

## Glossary of Key Terms

- **TAZ**: Traffic Analysis Zone -- the geographic unit for trip generation/distribution
- **LOS**: Level of Service -- measures of transportation system performance
- **VOT**: Value of Time -- willingness to pay for travel time savings
- **VMT**: Vehicle Miles Traveled
- **VHT**: Vehicle Hours Traveled
- **AADT**: Annual Average Daily Traffic
- **MPO**: Metropolitan Planning Organization
- **BPR curve**: Bureau of Public Roads volume-delay function
- **UE**: User Equilibrium (assignment method)
- **DTA**: Dynamic Traffic Assignment
- **ABM**: Activity-Based Model
- **NHTS**: National Household Travel Survey
- **ACS**: American Community Survey
- **CTPP**: Census Transportation Planning Products
- **LODES/LEHD**: Longitudinal Employer-Household Dynamics
