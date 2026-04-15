# Travel Analysis Skillset - Product Requirements Document

## Vision

Make travel demand modeling and analysis expertise accessible through AI-assisted workflows. By encoding domain knowledge as a Claude Code skill with role-aware guidance, practitioners across the transportation profession can get reliable, practical help -- whether they're running a model, building one, studying travel behavior, or reviewing forecasts.

## Problem Statement

Travel demand modeling knowledge is fragmented across:

- Academic textbooks (often outdated or overly theoretical)
- Agency-specific documentation and training materials
- Community resources like tfresource.org (comprehensive but hard to navigate quickly)
- Tacit knowledge held by experienced modelers
- Research papers behind paywalls or written for narrow academic audiences

Different roles need different things from the same body of knowledge. An analyst debugging a convergence problem needs different guidance than a reviewer assessing whether a model's mode shares are reasonable, or a researcher designing a stated preference survey. Today, all of them search the same scattered sources and filter for relevance themselves.

## Target Personas

The skill serves four distinct roles. It should detect or ask which role the user is operating in and tailor its responses accordingly.

### 1. Analyst / Operator

People who run existing travel demand models, prepare inputs, interpret outputs, and communicate insights to the public and decision-makers and planners.

**Typical questions:**

- "How should I structure my model networks and manage them using scenarios?"
- "How do I analyze a project such that I am responding to the obvious uncertainty of the future, but also consistent with FTA and environmental legislation requirements?"
- "How do I code a managed lane, auxilliary lane, represent transit reliability, etc?"
- "What tool should i use to answer a question about..."

**What they need:** Practical troubleshooting, step-by-step procedures, parameter ranges, rules of thumb, and validation targets.

### 2. Developer

People who build, modify, calibrate, validate or extend travel demand models and related tools.

**Typical questions:**

- "How should I structure a mode choice utility function for a region with BRT such that I can reflect the improved reliability and brand marketing that comes with BRT over regular bus service?"
- "My gravity model is producing trip lengths that are too short -- what should I check?"
- "What's a reasonable RMSE target for screenline validation? How do I balance base-year validation with future year flexibility/model sensistivity?"
- "What sensitiviy tests should i use and what are reasonable results?"
- "What's the best way to implement feedback between assignment and distribution?"
- "How do I set up an ActivitySim run with custom extensions?"
- "How do I handle external trips in my model?"
- "What are current best practices for GPS-assisted household travel surveys?"
- "What are the most resource-efficient methods for developing a new travel model toolset?"

**What they need:** Technical depth on model mechanics, software platform guidance, coding patterns, and architectural decisions.

### 3. Researcher

Academics and research staff studying travel behavior, developing new methods, or designing surveys.

**Typical questions:**

- "What are some qualitative methods from the field of social sciences that can help improve travel analysis"
- "How do latent class models compare to mixed logit for mode choice estimation?"
- "What sample size do I need to detect a 5% shift in transit mode share?"

**What they need:** Methodological rigor, statistical guidance, survey design best practices, connections to the research literature, and awareness of emerging approaches.

### 4. Reviewer

People at FTA, FHWA, state DOTs, MPO boards, or peer review panels who evaluate model results and forecasts.

**Typical questions:**

- "Are these results reasonable?"
- "What validation checks should I expect to see in a model documentation report?"
- "How do I assess whether an ABM is producing credible results for an FTA New Starts analysis?"

**What they need:** Reasonableness benchmarks, standard validation criteria, red flags to watch for, regulatory requirements, and guidance on what questions to ask modelers.

## Design Principles

1. **Role-aware responses**: Adapt depth, emphasis, and framing based on the user's role. An analyst gets troubleshooting steps; a reviewer gets evaluation criteria; a researcher gets methodological nuance.
2. **Reference, don't duplicate**: Point to tfresource.org and other authoritative sources for deep dives. Encode knowledge independently so Claude can reason about it, but don't replace existing resources.
3. **Practitioners first**: Emphasize practical guidance, common pitfalls, and actionable recommendations over theoretical completeness.
4. **Living resource**: The skillset should evolve as practices change, new research emerges, and the community contributes.

## Architecture

### Single Skill, Multiple Personas

Rather than separate skills per role, the project uses one unified skill that adapts its responses based on the user's context. This avoids duplication of foundational knowledge and lets the skill draw connections across roles.

```
travel-analysis-skillset/
  skills/
    fundamentals/
      SKILL.md              # The main skill -- role-aware travel modeling expertise
  docs/
    PRD.md                   # This document
    CONTRIBUTING.md          # How to contribute
  README.md
  LICENSE                    # CC BY-SA 4.0
```

### Skill Content Areas

The skill covers these topic areas, with each persona receiving tailored
treatment. Indented rows are subareas. Each area or subarea is composed of
smaller topic notes kept in `knowledge/topics/`; see hierarchy rules in
`docs/knowledge-pipeline.md`.


| Topic Area | Analyst Focus | Developer Focus | Researcher Focus | Reviewer Focus |
|-----------|---------------|-----------------|------------------|----------------|
| **Terminology and Basic Theories** | Learning at the outset if I don't have a background in this area | Reminder of underlying theories | Theories and terminology for adjacent or related fields | Lookup for when I have a question |
| **Travel Model Structures** | What questions match with which model type, and the caveats and decision-making boundaries for each question/model-type combination | Associated theories with each model type and what they imply; which model type to propose for a given question | Behavioral foundations, estimation methods | Decision-making boundaries for each model type based on the question and decision context |
| &nbsp;&nbsp;↳ Strategic Planning Models | - | - | - | - |
| &nbsp;&nbsp;↳ Network Metric Models (accessibility, congestion, reliability) | - | - | - | - |
| &nbsp;&nbsp;↳ Direct-Demand Models (e.g. regressions) | - | - | - | - |
| &nbsp;&nbsp;↳ Aggregate Demand Models (e.g. 4-step) | - | - | - | - |
| &nbsp;&nbsp;↳ Microsimulated Demand Models (e.g. activity-based) | - | - | - | - |
| **Network Data and Structures** | - | - | - | - |
| **Surveys** | Data sources, preparation, quality checks | Data pipelines, APIs, processing tools | Survey design, sampling, statistical methods | Data sufficiency, representativeness |
| **Validation & Calibration** | Hitting targets, diagnosing problems | Convergence, algorithm settings | Statistical tests, goodness-of-fit | Standards, benchmarks, red flags |
| **Forecasting** | Scenario setup, sensitivity testing | Automation, batch processing | Uncertainty quantification, model transferability | Forecast reasonableness, risk assessment |

## Scope

### Phase 1: Core Skill (Current)

Build the unified skill with foundational coverage of all topic areas from tfresource.org. Analyst and reviewer personas are highest priority since they have the most immediate practical need.

**Deliverables:**

- SKILL.md with role-detection and persona-adapted responses
- Structured repo of knowledge which SKILL.md can/should point to

**Success Criteria:**

- A user can state their role and receive appropriately tailored guidance
- Responses are accurate and reflect current best practices
- References point to relevant, accessible resources

### Phase 2: Depth Expansion

- Deepen coverage in areas where Phase 1 is thin and from other sources.
- Refine Behavior when there are multiple conflicting or differing points of view in the field.

### Phase 3: Extended Topics

Add coverage for specialized areas:

- Freight and commercial vehicle modeling
- Land use / transport integration
- Pricing and tolling analysis
- Active transportation modeling
- Autonomous/connected vehicle modeling
- Equity analysis in travel modeling

## Key References

- [tfresource.org](https://tfresource.org) - Travel Forecasting Resource, TRB ADB45 committee. Source: [github.com/tfresource/tfresource-website](https://github.com/tfresource/tfresource-website)
- [NHTS](https://nhts.ornl.gov) - National Household Travel Survey
- [ActivitySim](https://activitysim.github.io) - Open-source activity-based model platform
- [FHWA Travel Model Improvement Program](https://tmip.org) - Federal resources for travel modeling
- NCHRP Report 716: Travel Demand Forecasting: Parameters and Techniques
- FHWA Travel Model Validation and Reasonableness Checking Manual
- FTA New Starts guidance on travel forecasting
- [Transportation Network Analysis by Steve Boyles et al.](https://sboyles.github.io/book.pdf)

