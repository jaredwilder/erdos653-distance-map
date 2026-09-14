#!/usr/bin/env python3
"""Exact witness for Erdős #653: g(4)=3.

Only integer squared distances are used; no floating-point geometry is needed.
"""
from collections import defaultdict

POINTS = {
    "A": (0, 0),
    "B": (0, 1),
    "C": (1, 0),
    "D": (-1, 0),
}


def sqdist(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def r_value(name):
    p = POINTS[name]
    return len({sqdist(p, q) for other, q in POINTS.items() if other != name})


def main():
    values = {name: r_value(name) for name in POINTS}
    print("R-values:", values)
    assert values == {"A": 1, "B": 2, "C": 3, "D": 3}

    distinct = set(values.values())
    print("distinct R-values:", sorted(distinct))
    assert distinct == {1, 2, 3}

    # Universal four-point upper bound: each vertex has exactly three other
    # vertices, hence its number of distinct positive distances is in {1,2,3}.
    possible_r_values = {1, 2, 3}
    assert len(possible_r_values) == 3
    print("universal upper bound for four points: at most 3 distinct R-values")
    print("g(4)=3 PASS")


if __name__ == "__main__":
    main()
