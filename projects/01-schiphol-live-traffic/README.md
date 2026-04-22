# Project 01 — Schiphol Live Traffic Flows

> Visualise arrival and departure flows at Schiphol (EHAM) using live OpenSky data.

**Planned for Week 2 of the learning plan.**

## Goal

Build a first end-to-end pipeline: pull live state vectors over the Netherlands,
filter to flights interacting with EHAM, and visualise arrival vs. departure flows
on a map. This project establishes the baseline tooling used in all later projects.

## Data

- **Source:** OpenSky Network — live state vector API (no account required for live data)
- **Scope:** All aircraft within a box around EHAM, one snapshot window

## Method (planned)

1. Query OpenSky live API via `traffic.data.opensky.livetraffic()`.
2. Classify each flight as arrival / departure / overflight using altitude and vertical rate.
3. Plot trajectories on a Cartopy map, coloured by flow category.

## Key findings

_To be filled in after running the analysis._

## Reproduce

```bash
cd projects/01-schiphol-live-traffic
jupyter lab notebook.ipynb
```

## References

- SKYbrary: [ADS-B](https://skybrary.aero/articles/automatic-dependent-surveillance-broadcast-ads-b)
- `traffic` quickstart: <https://traffic-viz.github.io/quickstart.html>
