"""Round 5 — which region is costing us the most storage?"""
from __future__ import annotations

from typing import Any, TypeAlias

from given.catalog import Node
from given.round import check_round

Round5Prepared: TypeAlias = tuple[str, int]     # <- YOUR structural decision, in one line. Replace `Any`.


def subtree_size(node: Node) -> int:
    if node.is_file:
        return node.size or 0

    return sum(subtree_size(child) for child in node.children)

def prepare(root: Node) -> Round5Prepared:
    biggest_name = ""
    biggest_size = -1
    
    for region in root.children:
        size = subtree_size(region)

        if size > biggest_size:
            biggest_name = region.name
            biggest_size = size

    return biggest_name, biggest_size

def serve(prepared: Round5Prepared, query: None = None) -> tuple[str, int]:
    """The name of the top-level region whose subtree holds the most bytes, and how many."""
    return prepared
    


check_round(prepare, serve)
