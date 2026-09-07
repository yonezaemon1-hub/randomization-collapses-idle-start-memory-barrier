# Computational evidence backfill

Status: candidate for a future manuscript version; the published v1.0.0 Zenodo PDF and release tag remain unchanged.

The manuscript already contains an exact-integer audit of the fair-coin BRF Bellman formula. This backfill turns that audit into reusable finite-size data suitable for a manuscript table or runtime figure.

## Added runtime curve audit

Run:

```bash
python audit/computational_evidence.py
```

The script independently reconstructs

- `Q_j = product_{r=1}^j (2^r-1)`;
- `Delta_k = sum_{j=0}^k binom(k,j) Q_j`;
- the exact one-frontier / adaptive-worst-case expectation
  `E_1 = 2^n + sum_i Delta_i (1 + sum_{x=1}^i binom(n,x))`.

It writes `audit/brf_runtime_curve.csv` with exact integer expectations, `log2(E[T])`, the leading exponent `n(n+1)/2`, and the normalized ratio `E[T] / 2^(n(n+1)/2)`.

The first rows must reproduce the frozen exact audit values:

- n=2: 10
- n=3: 58
- n=4: 602
- n=5: 14106
- n=6: 755610
- n=7: 87665306
- n=8: 21246839962

## Interpretation

The finite curve makes the `2^{Theta(n^2)}` time cost visible without changing the theorem. It is especially useful beside the size-aware follow-up, where the corresponding tuned fixed-bias family has `2^{Theta(n log n)}` worst-case expectation.

## Scope

This is an exact finite computation for the causal state-adaptive adversary analyzed in the paper. It is not evidence for a tight oblivious-adversary bound and does not strengthen the one-bit result from an upper bound to an exact randomized minimum.
