"""Round 1 — how many trips started at each station?"""
from __future__ import annotations

from typing import Any, Sequence, TypeAlias

from given.probe import Station, Trip
from given.round import check_round

Round1Prepared: TypeAlias = dict[Station: int]     # <- YOUR structural decision, in one line. Replace `Any`.


def prepare(trips: Sequence[Trip]) -> Round1Prepared:
    station_dict =  {}
    for trip in trips:
        if trip.station not in station_dict:
            station_dict[trip.station]=1
        else:
            station_dict[trip.station]+=1
            
    return station_dict


def serve(prepared: Round1Prepared, station: Station) -> int:

    return prepared[station]


check_round(prepare, serve)   # keep this line; mypy fails here if the two ends disagree
