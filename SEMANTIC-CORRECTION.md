# Semantic correction — the regular-polygon route does not bound `g(n)` above

An earlier Pass-6 paragraph attached the regular-polygon chord count `floor(n/2)` to Erdős #653 and concluded

`g(n) <= floor(n/2)`.

That conclusion is false.

For a configuration `X={x_1,...,x_n}`, `R(x_i)` is the number of distinct distances from `x_i` to the other vertices. The function `g(n)` is the **maximum over configurations** of the number of distinct values among `R(x_1),...,R(x_n)`.

In a regular `n`-gon every vertex is symmetry-equivalent and has

`R(x_i)=floor(n/2)`.

Therefore the set of `R`-values is the singleton `{floor(n/2)}` and has cardinality 1.

Two independent errors were present in the old inference:

1. `floor(n/2)` is the value of `R(x_i)`, not the number of different `R`-values across vertices;
2. exhibiting one configuration cannot upper-bound a quantity defined as a maximum over all configurations.

The regular-polygon chord computation belongs to a different distance problem (#655) and was incorrectly transplanted here.

What survives independently is `g(4)=3`, proved by the explicit four-point witness in this repository. The asymptotic Erdős #653 problem remains open.
