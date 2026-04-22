"""Shared plotting helpers — maps and common ATM figures.

Conventions used across projects:
- Cartopy with PlateCarree by default
- Dark-neutral background, single accent colour per figure
- All figures saved at 150 DPI into each project's `figures/` directory
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from traffic.core import Traffic


def new_map(figsize: tuple[float, float] = (10, 8)):
    """Create a Cartopy map with sensible defaults for European airspace."""
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature

    fig, ax = plt.subplots(
        figsize=figsize,
        subplot_kw={"projection": ccrs.PlateCarree()},
    )
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.3, linestyle=":")
    ax.gridlines(draw_labels=True, linewidth=0.2, alpha=0.5)
    return fig, ax


def save_figure(fig, project_dir: str | Path, name: str) -> Path:
    """Save a figure to <project_dir>/figures/<name>.png at 150 DPI."""
    out_dir = Path(project_dir) / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{name}.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    return out_path
