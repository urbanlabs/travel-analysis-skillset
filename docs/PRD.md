# Travel Analysis Skillset - Product Requirements Document

## Vision

Make travel demand modeling expertise accessible to transportation planners through AI-assisted workflows. By encoding domain knowledge as Claude Code skills, practitioners can get reliable, practical guidance on travel modeling topics without searching through scattered documentation, textbooks, and agency reports.

## Problem Statement

Travel demand modeling knowledge is fragmented across:
- Academic textbooks (often outdated or overly theoretical)
- Agency-specific documentation and training materials
- Community resources like tfresource.org (comprehensive but hard to navigate quickly)
- Tribal knowledge held by experienced modelers

Practitioners -- especially those newer to the field or working at smaller agencies -- need quick, reliable guidance grounded in established best practices. AI assistants can help, but only if they have access to accurate, well-structured domain knowledge.

## Design Principles

1. **Reference, don't duplicate**: Point to tfresource.org and other authoritative sources for deep dives. Encode knowledge independently so Claude can reason about it, but don't try to replace existing resources.
2. **Practitioners first**: Target working transportation planners, not academics. Emphasize practical guidance, common pitfalls, and actionable recommendations.
3. **Actionable over exhaustive**: Cover what practitioners actually need to know, not every theoretical nuance. A planner should be able to get useful guidance in a single interaction.
4. **Living resource**: The skillset should evolve as practices change, new research emerges, and the community contributes.

## Scope

### Phase 1: Fundamentals Skill (`skills/fundamentals/`)

Core travel demand modeling knowledge for practitioners.

**Topics:**
- **4-Step Model Framework**: Trip generation, trip distribution, mode choice, and traffic assignment. Key methods, inputs/outputs, and practical considerations for each step.
- **Activity-Based Models**: How ABMs differ from trip-based models, key platforms (ActivitySim, CT-RAMP), when and why to use them, transition considerations.
- **Data and Surveys**: Key data sources (NHTS, household travel surveys, Census/ACS, LODES, passive/big data), what each provides, quality considerations, and common pitfalls.
- **Model Validation and Calibration**: Best practices, reasonableness checks, common thresholds, and frequent issues practitioners encounter.

**Success Criteria:**
- A planner can invoke the skill and get reliable guidance on any of the above topics
- Responses include references to tfresource.org and other sources for further reading
- Guidance reflects current best practices in the field

### Phase 2: Research Skill (`skills/research/`)

Key findings from travel forecasting and analysis research, made accessible to practitioners.

**Potential topics:**
- Important research findings that affect practice
- Emerging methods and their readiness for application
- Literature summaries on common modeling questions

### Phase 3: Coding Skill (`skills/coding/`)

Development patterns and tools for travel demand forecasting.

**Potential topics:**
- Common software platforms and their APIs
- Scripting patterns for model automation
- Data processing workflows
- Open-source tool ecosystem (ActivitySim, TransCAD scripting, EMME, Cube Voyager, etc.)

## Architecture

```
travel-analysis-skillset/
  skills/
    fundamentals/SKILL.md    # Phase 1 - domain knowledge skill
    research/                 # Phase 2 - research findings skill
    coding/                   # Phase 3 - development skill
  docs/
    PRD.md                    # This document
    CONTRIBUTING.md           # How to contribute
  README.md
  LICENSE                     # CC BY-SA 4.0
```

Each skill is a standalone `SKILL.md` file that can be installed in Claude Code independently.

## Key References

- [tfresource.org](https://tfresource.org) - Travel Forecasting Resource, TRB ADB45 committee
- [NHTS](https://nhts.ornl.gov) - National Household Travel Survey
- [ActivitySim](https://activitysim.github.io) - Open-source activity-based model platform
- [FHWA Travel Model Improvement Program](https://tmip.org) - Federal resources for travel modeling
