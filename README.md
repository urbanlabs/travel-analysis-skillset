# Travel Analysis Skillset

AI skills for travel demand modeling and transportation analysis, designed for use with [Claude Code](https://claude.ai/claude-code).

## What Is This?

A collection of Claude Code skills that encode travel demand modeling domain expertise for transportation planners. Instead of searching through textbooks and documentation, planners can get reliable, practical guidance through AI-assisted workflows.

## Skills

| Skill | Status | Description |
|-------|--------|-------------|
| [Fundamentals](skills/fundamentals/SKILL.md) | Active | 4-step models, ABMs, data/surveys, validation |
| [Research](skills/research/) | Planned | Key research findings for practitioners |
| [Coding](skills/coding/) | Planned | Development patterns for travel forecasting tools |

## Usage

To use a skill in Claude Code, install it as a custom skill:

```bash
# Clone the repo
git clone https://github.com/urbanlabs/travel-analysis-skillset.git

# Install the fundamentals skill (from your project directory)
# Copy or symlink the SKILL.md to your project's .claude/skills/ directory
mkdir -p .claude/skills
cp travel-analysis-skillset/skills/fundamentals/SKILL.md .claude/skills/travel-fundamentals.md
```

Once installed, Claude will automatically activate the skill when you ask about travel demand modeling topics.

## Key References

This skillset encodes knowledge independently but references these authoritative sources:

- [tfresource.org](https://tfresource.org) - Travel Forecasting Resource (TRB ADB45)
- [NHTS](https://nhts.ornl.gov) - National Household Travel Survey
- [ActivitySim](https://activitysim.github.io) - Open-source ABM platform
- [TMIP](https://tmip.org) - FHWA Travel Model Improvement Program

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## License

[CC BY-SA 4.0](LICENSE) - Creative Commons Attribution-ShareAlike 4.0 International
