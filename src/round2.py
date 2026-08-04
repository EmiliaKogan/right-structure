"""Round 2 — the support desk has a receipt, and the dashboard has not gone away."""
from __future__ import annotations

from typing import Any, Sequence, TypeAlias

from given.probe import Trip, TripId, Station
from given.round import ByReceipt, ByStation, Query2, check_round

Round2Prepared: TypeAlias =  tuple[dict[Station, int],dict[tuple[Station, TripId], Trip]]      # <- YOUR structural decision, in one line. Replace `Any`.


def prepare(trips: Sequence[Trip]) -> Round2Prepared:
    # by_station, by_receipt = {},{}
    by_station: dict[Station, int] = {}
    by_receipt = {}
    for trip in trips:
        by_station[trip.station] = by_station.get(trip.station, 0) + 1
        by_receipt[(trip.station, trip.trip_id)] = trip
            
    return by_station, by_receipt

def serve(prepared: Round2Prepared, query: Query2) -> int | Trip:
    """`ByStation` -> the trip count. `ByReceipt` -> the trip itself."""
    by_station, by_receipt = prepared
    if isinstance(query, ByStation):
        return by_station.get(query.station, 0)
    elif isinstance(query, ByReceipt):
        return by_receipt[(query.station, query.trip_id)]


check_round(prepare, serve)
