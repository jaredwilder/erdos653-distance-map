# Erdős #653 — per-vertex distance counts

For a planar configuration `X={x_1,...,x_n}`, define

\[
R(x_i)=\#\{\lvert x_j-x_i\rvert:j\ne i\},
\]

the number of distinct distances seen from vertex `x_i`. Erdős #653 asks about

\[
g(n)=\max_X \#\{R(x_1),...,R(x_n)\}.
\]

## Exact result: `g(4)=3`

Take

```text
A = (0,0)
B = (0,1)
C = (1,0)
D = (-1,0)
```

Using squared distances:

- `A` sees `{1}`, so `R(A)=1`;
- `B` sees `{1,2}`, so `R(B)=2`;
- `C` and `D` see `{1,2,4}`, so `R(C)=R(D)=3`.

Thus the configuration realizes the three values `{1,2,3}`. No four-point configuration can realize more, because every vertex sees between one and three distinct distances. Hence

\[
\boxed{g(4)=3}.
\]

[`verify_g4.py`](verify_g4.py) checks the witness exactly with integer squared distances.

## A useful correction

A regular `n`-gon has only one per-vertex count: every vertex sees exactly `floor(n/2)` distinct distances. It therefore gives

```text
#{R(x_1),...,R(x_n)} = 1,
```

not an upper bound on `g(n)`. An earlier route conflated the number of distances in the polygon with the number of distinct values of `R`, and also reversed the direction of the extremum. The details are in [`SEMANTIC-CORRECTION.md`](SEMANTIC-CORRECTION.md).

## Files

- [`verify_g4.py`](verify_g4.py) — exact witness check.
- [`SEMANTIC-CORRECTION.md`](SEMANTIC-CORRECTION.md) — regular-polygon correction.
- [`PROVENANCE.md`](PROVENANCE.md) — source history.

```bash
python verify_g4.py
```

The asymptotic Erdős #653 problem remains open.

Author: Jared Wilder.
