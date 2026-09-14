# Erdős 653 — diversity of per-vertex distance counts

For a planar configuration `X={x_1,...,x_n}`, define

`R(x_i) = #{ |x_j-x_i| : j != i }`,

the number of distinct distances seen from vertex `x_i`. Erdős #653 asks about

`g(n) = max_X #{ R(x_1),...,R(x_n) }`,

the maximum possible number of **different per-vertex distance counts** in an `n`-point configuration.

## Exact finite result: `g(4)=3`

Take the four integer-coordinate points

```text
A = (0,0)
B = (0,1)
C = (1,0)
D = (-1,0)
```

Using squared distances:

- `A` sees only `{1}`, so `R(A)=1`;
- `B` sees `{1,2}`, so `R(B)=2`;
- `C` and `D` each see `{1,2,4}`, so `R(C)=R(D)=3`.

Thus the configuration realizes the three values `{1,2,3}`. Conversely, in any four-point configuration each vertex sees between 1 and 3 distinct distances, so there can be at most three distinct `R`-values. Therefore

**`g(4)=3`.**

[`verify_g4.py`](verify_g4.py) checks the witness using exact integer squared distances.

## Critical correction: the regular-polygon route is false

An earlier Pass-6 route confused two different quantities. In a regular `n`-gon, every vertex sees `floor(n/2)` distinct distances, so every vertex has the **same** `R`-value. The set of `R`-values therefore has cardinality **1**.

That configuration cannot prove `g(n) <= floor(n/2)`: `g(n)` is a maximum over configurations, so a single example supplies only a lower bound on the maximum. The old argument suffered both a quantity mismatch and a reversal of the extremum direction.

The correction is preserved in [`SEMANTIC-CORRECTION.md`](SEMANTIC-CORRECTION.md). The asymptotic Erdős #653 problem remains open.

## Files

- [`verify_g4.py`](verify_g4.py) — exact standard-library witness check.
- [`SEMANTIC-CORRECTION.md`](SEMANTIC-CORRECTION.md) — the regular-polygon semantic audit.
- [`PROVENANCE.md`](PROVENANCE.md) — source chronology and authority boundary.

## Reproduce

```bash
python verify_g4.py
```

Author: Jared Wilder
