# Project NN — [Project Title]

> One-line tagline: what this project shows in a single sentence.

![Key figure](figures/placeholder.png)

## Goal

What question does this project answer? Why does it matter for ATM?
Keep this to 2–4 sentences. State the question as concretely as possible.

## Data

- **Source:** OpenSky Network / EUROCONTROL Aviation Intelligence Portal / ...
- **Time range:** e.g. 2026-04-22, 06:00–22:00 UTC
- **Scope:** e.g. all flights within the EHAA FIR
- **Volume:** approx. N flights / M state vectors

Any sample data committed to `data/` is intentionally small.
Large files are gitignored — see the instructions below to reproduce.

## Method

1. Download raw state vectors using `traffic.data.opensky`.
2. Clean and resample trajectories to 1 Hz.
3. ... (step by step — keep it brief but precise)
4. Produce the figures in `figures/`.

The main logic lives in [`src/`](src/); the notebook
[`notebook.ipynb`](notebook.ipynb) walks through it with commentary.

## Key findings

- Finding 1 — one line, with a number if possible.
- Finding 2 — ...
- Finding 3 — ...

## Reproduce

```bash
# From the repo root
cd projects/NN-project-name
jupyter lab notebook.ipynb
```

Or to run the headless pipeline:

```bash
python -m src.main
```

## What I'd do next

- Extension 1: e.g. extend to a full week of traffic instead of one day.
- Extension 2: e.g. compare against the equivalent period in 2019.
- Open question: ...

## References

- SKYbrary article(s) used: [Link](https://skybrary.aero/)
- Related paper / blog post: ...
