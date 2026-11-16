# Contributing

## Add a discipline

1. Open the right file in `data/` (or create a new one) and add an entry:

```python
d("slug", "Display Name", C,
  "One-sentence scope.",
  "Step 1|Step 2|... (8-10 items, in teaching order)",
  "Starter project 1|Starter project 2|Starter project 3",
  "Tools, materials, software",
  "How to practise safely and cheaply",
  "Safety note (required for anything involving electricity, gas, pressure, heights, lifting, chemicals, radiation or people's health)")
```

2. Run `python scripts/build.py` then `python scripts/validate.py`.
3. Commit the `data/` change **and** the regenerated `skills/` and `DISCIPLINES.md`.

## Rules

- Never edit files in `skills/` by hand; change `data/` or the template in `scripts/build.py`.
- Keep content generic and public-safe: no employer names, personal details, internal URLs or secrets. `validate.py` checks this.
- Do not invent standards, clause numbers or legal claims. Point to official sources.
- Dangerous trades and high-risk work must carry a safety note and push the learner towards qualified supervision.
