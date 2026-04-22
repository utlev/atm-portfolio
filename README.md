# ATM Portfolio

Hands-on portfolio exploring European Air Traffic Management (ATM) with open flight data.
Built alongside a structured 10-week study plan covering SKYbrary theory, the OpenSky Network,
and the `traffic` Python library.

**About me:** BSc Aerospace Engineering, TU Delft. Targeting the
[EUROCONTROL Skyline traineeship](https://jobs.eurocontrol.int/) — October 2026 intake.

---

## Projects

| # | Project | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 1 | [Schiphol live traffic flows](projects/01-schiphol-live-traffic/) | OpenSky live API, `traffic` basics, arrival/departure visualisation | 🟡 Planned |
| 2 | [FIR flight count](projects/02-fir-flight-count/) | Airspace geometry, point-in-polygon over real FIR boundaries | 🟡 Planned |
| 3 | [Separation pair detection](projects/03-separation-pairs/) | Trajectory analysis, lateral/vertical separation, safety concepts | 🟡 Planned |
| 4 | [OpenAP fuel burn study](projects/04-openap-fuelburn/) | Aircraft performance modelling with OpenAP | 🟡 Planned |
| 5 | [ATFM delay patterns](projects/05-atfm-delays/) | EUROCONTROL open performance data, pandas + seaborn | 🟡 Planned |
| 6 | [CDO compliance analysis](projects/06-cdo-compliance/) | Continuous Descent Operations — a real SESAR KPI | 🟡 Planned |
| ⭐ | [**Capstone: A Week in the Life of Dutch Airspace**](capstone/) | End-to-end analysis combining volume, delays, fuel, environment | 🟡 Planned |

Status legend: 🟡 Planned · 🔵 In progress · 🟢 Complete

## Tech stack

- **Python 3.11+**
- [`traffic`](https://traffic-viz.github.io/) — air traffic data processing and visualisation (Xavier Olive, ONERA)
- [`pyModeS`](https://github.com/junzis/pyModeS) — ADS-B / Mode S decoding
- [`openap`](https://github.com/junzis/openap) — Open Aircraft Performance model (Junzi Sun, TU Delft)
- [`cartopy`](https://scitools.org.uk/cartopy/) — geographic plotting
- Standard data stack: `pandas`, `numpy`, `matplotlib`, `seaborn`, Jupyter

## Repository layout

```
projects/        One folder per mini-project, self-contained.
capstone/        End-of-plan integrated analysis.
shared/atm_utils/  Utilities shared across projects (OpenSky wrappers, plotting helpers).
notes/           Reading notes from SKYbrary and other references.
```

## Getting started

```bash
# Clone
git clone https://github.com/<your-username>/atm-portfolio.git
cd atm-portfolio

# Install dependencies (uv recommended, pip works too)
uv sync
# or:  pip install -e .

# Launch Jupyter
jupyter lab
```

An [OpenSky Network](https://opensky-network.org/) account is required for historical
data access. Create one for free, then add your credentials as described in the
[`traffic` configuration guide](https://traffic-viz.github.io/installation.html#network-configuration).

## References

- **SKYbrary** — <https://skybrary.aero/> — EUROCONTROL's ATM knowledge base
- **OpenSky Network** — <https://opensky-network.org/>
- **EUROCONTROL Aviation Intelligence Portal** — <https://ansperformance.eu/>
- **SESAR 3 JU** — <https://www.sesarju.eu/>

## License

MIT — see [LICENSE](LICENSE).
