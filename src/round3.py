"""Round 3 — the k busiest stations, live on the wall display."""
from __future__ import annotations

from typing import Any, Sequence, TypeAlias

from given.probe import Station, Trip, Distance
from given.round import check_round

Round3Prepared: TypeAlias = dict[Station: int]         # <- YOUR structural decision, in one line. Replace `Any`.


def prepare(trips: Sequence[Trip]) -> Round3Prepared:
    station_dist = {}
    for trip in trips:
        if trip.station in station_dist:
            station_dist[trip.station] = station_dist[trip.station] + trip.distance_m
        else:
            station_dist[trip.station] = trip.distance_m
    return station_dist


def insert_sorted(top_k: list[tuple[Station, Distance]], check: tuple[Station, Distance],):
    distance_check = check[1]

    for index, (_, distance) in enumerate(top_k):
        if distance_check > distance:
            top_k.insert(index, check)
            return

    top_k.append(check)


def serve(prepared: Round3Prepared, k: int) -> list[Station]:
    """The `k` stations with the most metres ridden from them, most-first."""
    top_k = []

    for station, distance in prepared.items():

        if len(top_k) < k:
            insert_sorted(top_k, (station, distance))

        elif distance > top_k[-1][1]:
            top_k.pop()
            insert_sorted(top_k, (station, distance))

    return [station for station, _ in top_k]


check_round(prepare, serve)
