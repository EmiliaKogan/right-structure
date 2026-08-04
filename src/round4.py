"""Round 4 — total distance of trips that started between 09:00 and 11:00."""
from __future__ import annotations

from typing import Any, Sequence, TypeAlias

from given.probe import Distance, Timestamp, Trip
from given.round import check_round

Round4Prepared: TypeAlias = tuple[list[Timestamp],list[Distance],]      # <- YOUR structural decision, in one line. Replace `Any`.

def binary_search(timestamps: list[Timestamp], target: Timestamp) -> int:
    left = 0
    right = len(timestamps)

    while left < right:
        mid = (left + right) // 2
        if timestamps[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def prepare(trips: Sequence[Trip]) -> Round4Prepared:
    timestamp_list, distance_sum = [], [Distance(0)]
    total = Distance(0)
    sorted_trips = sorted(trips, key=lambda trip: trip.started_at)
    for trip in sorted_trips:
        timestamp_list.append(trip.started_at)
        total = total+trip.distance_m
        distance_sum.append(total)
    return timestamp_list, distance_sum


def serve(prepared: Round4Prepared, span: tuple[Timestamp, Timestamp]) -> Distance:
    """Total metres ridden on trips that started in the half-open range [lo, hi)."""
    low = binary_search(prepared[0], span[0])
    high = binary_search(prepared[0], span[1])
    distance = prepared[1][high]-prepared[1][low]
    return distance


check_round(prepare, serve)
