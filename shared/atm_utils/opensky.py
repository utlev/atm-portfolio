"""Thin wrappers around the `traffic` + OpenSky Network APIs.

Keep repetitive query boilerplate here so each project notebook stays focused
on analysis, not plumbing.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from traffic.core import Traffic


def fetch_state_vectors(
    start: datetime,
    stop: datetime,
    bounds: tuple[float, float, float, float] | None = None,
) -> "Traffic":
    """Fetch historical state vectors from OpenSky for a bounded area.

    Parameters
    ----------
    start, stop : datetime
        Time range in UTC.
    bounds : (west, south, east, north), optional
        Lon/lat bounding box. Defaults to the Netherlands FIR (EHAA) rough box.

    Returns
    -------
    traffic.core.Traffic
        A Traffic object ready for analysis.

    Notes
    -----
    Requires OpenSky credentials configured via the `traffic` library.
    See: https://traffic-viz.github.io/installation.html
    """
    from traffic.data import opensky

    if bounds is None:
        # Rough Netherlands FIR box — tune per project
        bounds = (2.0, 50.5, 7.5, 54.0)

    return opensky.history(
        start=start,
        stop=stop,
        bounds=bounds,
    )
