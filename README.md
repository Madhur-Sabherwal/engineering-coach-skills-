# Engineering Coach Skills

A set of [Claude Code](https://claude.com/claude-code) skills that **coach you instead of doing the work for you**. Pick a discipline, from data engineering to plumbing, and the coach teaches you step by step while you do the actual work.

## What makes these different

- **You do the work.** The coach explains, asks questions and reviews. It does not write your solution.
- **4-year-old explanations.** Every new concept comes as a simple picture first, then the real word, then an example from your project.
- **No repeats.** Taught concepts are logged in a ledger; the coach will not re-explain one unless you ask ("explain again", "remind me").
- **Predict, do, explain back.** Built to keep your own thinking sharp.
- **Safety first.** Trades and high-risk fields (electrical, gas, heights, lifting, chemicals, health) carry explicit safety notes and push you to qualified supervision.
- **Honest.** Standards and licensing differ by country; the coach asks where you are and points to official sources instead of inventing clauses.

## Install

Requires Claude Code. Clone this repo, then copy the skills into your skills folder.

```bash
# macOS / Linux / Git Bash: everything
bash scripts/install.sh
# or just some
bash scripts/install.sh coach-data-engineering coach-robotics engineering-coach
```

```powershell
# Windows
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
powershell -ExecutionPolicy Bypass -File scripts/install.ps1 -Only coach-data-engineering,engineering-coach
```

Restart Claude Code, then run `/engineering-coach` to be matched to a discipline, or start one directly, for example `/coach-data-engineering` or `/coach-electrician-trade`.

## Where your progress is stored

Each coach keeps two small files on your machine only, at `~/.claude/coach-state/<discipline>/`:

- `taught-concepts.md`: what you have already been taught
- `progress.md`: your project, next step and open questions

These are never part of this repo.

## Disciplines

See [DISCIPLINES.md](DISCIPLINES.md) for the full generated list (software and data, electrical and control, mechanical and manufacturing, civil and built environment, process and life sciences, skilled trades, cross-cutting engineering), plus the `engineering-coach` router.

## How it is built

`data/*.py` holds one entry per discipline. `scripts/build.py` turns them, plus one shared coaching template, into `skills/<name>/SKILL.md`. `scripts/validate.py` checks the output. See [CONTRIBUTING.md](CONTRIBUTING.md) to add a discipline.

## Disclaimer

These skills are learning aids. They are not a substitute for qualified instruction, licensing, apprenticeships or professional sign-off. Never rely on them for safety-critical decisions, and never do licensed or dangerous work without proper authorisation and training.

## Licence

MIT. See [LICENSE](LICENSE); Madhur Sabherwal 
