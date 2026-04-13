# Travel Analysis Skillset

AI skills for travel demand modeling and transportation analysis, designed for use with [Claude Code](https://claude.ai/claude-code).

## What Is This?

A Claude Code skill that encodes travel demand modeling domain expertise. It adapts its responses based on your professional role:

- **Analyst/Operator** -- running models, preparing inputs, interpreting outputs
- **Developer** -- building, modifying, or scripting travel demand models
- **Researcher** -- studying travel behavior, designing surveys, developing methods
- **Reviewer** -- evaluating models and forecasts (FTA, FHWA, state DOTs, peer review)

## Topics Covered

- 4-step travel demand model framework (trip generation, distribution, mode choice, assignment)
- Activity-based models (ActivitySim, CT-RAMP, DAYSIM)
- Data and surveys (NHTS, household travel surveys, Census/ACS, passive data)
- Model validation and calibration

## Usage

To use the skill in Claude Code, install it in your project:

```bash
# Clone the repo
git clone https://github.com/urbanlabs/travel-analysis-skillset.git

# Copy the skill to your project's .claude/skills/ directory
mkdir -p .claude/skills
cp travel-analysis-skillset/skills/fundamentals/SKILL.md .claude/skills/travel-fundamentals.md
```

Once installed, Claude will automatically activate the skill when you ask about travel demand modeling topics and adapt its responses to your role.

## Key References

This skill encodes knowledge independently but references these authoritative sources:

- [tfresource.org](https://tfresource.org) -- Travel Forecasting Resource (TRB ADB45). Source: [github.com/tfresource/tfresource-website](https://github.com/tfresource/tfresource-website)
- [NHTS](https://nhts.ornl.gov) -- National Household Travel Survey
- [ActivitySim](https://activitysim.github.io) -- Open-source ABM platform
- [TMIP](https://tmip.org) -- FHWA Travel Model Improvement Program

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## License

[CC BY-SA 4.0](LICENSE) -- Creative Commons Attribution-ShareAlike 4.0 International
