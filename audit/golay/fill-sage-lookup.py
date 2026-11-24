"""Bounded, matrix-free lookup for the original 38 orders."""
import csv
import sys
from pathlib import Path

from sage.combinat.designs.difference_family import spin_goethals_seidel_difference_family
from sage.combinat.matrices.hadamard_matrix import williamson_type_quadruples_smallcases


assert sys.prefix != sys.base_prefix
with Path(__file__).with_name("claude-fill.tsv").open() as stream:
    orders = [int(row["order"]) for row in csv.DictReader(stream, delimiter="\t")]
assert len(orders) == len(set(orders)) == 38
assert williamson_type_quadruples_smallcases(3, existence=True)
for lookup in (williamson_type_quadruples_smallcases, spin_goethals_seidel_difference_family):
    hits = [n for n in orders if lookup(n // 4, existence=True)]
    print(lookup.__name__, len(orders), "queries", hits)
