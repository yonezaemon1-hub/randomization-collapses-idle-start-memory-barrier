# BRF exact runtime table

- `brf_runtime_curve.csv` — exact adaptive-worst-case expectations for fair-coin BRF for `n=2..12`, together with `log2(E[T])` and normalization by `2^(n(n+1)/2)`.
- `../audit/brf_exact_runtime_check.py` — frozen exact-integer audit from the published paper.
- `../audit/computational_evidence.py` — independent reconstruction used for the extended finite table.

The runtime table is specific to the causal state-adaptive adversary analyzed in the paper. It does not certify a tight oblivious-adversary bound.
