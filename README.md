# Randomization Collapses the Idle-Start Memory Barrier

Preprint v1.0.0 by **Ryutaro Yonezu (Independent Researcher)**.

Full title:

**Randomization Collapses the Idle-Start Memory Barrier for Anonymous Dynamic Broadcast**

## Main result

In anonymous, port-indistinguishable, synchronous, 1-interval-connected dynamic networks with idle start, unknown `n`, private independent random bits, and stabilizing termination (without termination detection), **Bernoulli Reactivation Flooding (BRF)** solves broadcast with exactly two persistent protocol states.

Equivalently, BRF uses:

```text
1 persistent control bit + the broadcast payload
```

and no knowledge of `n`.

This gives a qualitative deterministic-randomized memory separation: the known deterministic idle-start lower bound is `omega(1)` local memory, whereas a private-coin Las Vegas upper bound uses one persistent control bit.

## Protocol

Each informed node is either `ACTIVE` or `IDLE`.

- `ACTIVE`: broadcast `INF` (or `INF(M)` for an explicit payload), then remain active with probability `1/2` and become idle otherwise.
- `IDLE`: remain silent; if at least one `INF` is received, become active in the next round.

An active node does not renew its active state merely because it receives `INF`; its current-round private coin decides the next control state.

## Correctness

If the active set is a nonempty proper subset of the network, 1-interval connectivity guarantees an active-idle cut edge. Because active nodes transmit before their coin update, at least one idle node is reactivated in the next round. Therefore false extinction is impossible.

A finite success event of positive probability grows the active set to all `n` nodes and then makes all `n` nodes become idle simultaneously. Hence BRF is zero-error, terminates almost surely, and has finite expected stabilization time.

## Worst-case expected time

For fair-coin BRF against the causal state-adaptive topology adversary defined in the paper, the Bellman-optimal adversary exposes exactly one idle node to the active set whenever the active set is proper. The resulting worst-case expectation satisfies

```text
E[T] ~ c0 * 2^(n(n+1)/2)
c0 = product_{r>=1} (1 - 2^(-r)) ~= 0.288788095
```

so `E[T] = 2^{Theta(n^2)}` in that adversary model.

The tight worst-case expectation against oblivious topology schedules is not claimed and remains open.

## Scope

The result concerns **stabilizing termination**, not termination detection. The paper does not claim that randomized flooding, epidemic spreading, or random reactivation is novel in general. The contribution is the control-memory consequence of Bernoulli reactivation in this specific anonymous, port-indistinguishable, adversarially dynamic, idle-start model.

The statement `one bit` is an upper bound for randomized protocol control; the paper does not prove that one bit is the randomized minimum.

## Files

- `Yonezu_2026_Randomization_Collapses_Idle_Start_Memory_Barrier.pdf` — authoritative v1.0.0 manuscript PDF.
- `paper.tex` — LaTeX manuscript source.
- `PROOF_AUDIT.md` — theorem-chain and claim-boundary audit.
- `PRIOR_ART_AUDIT.md` — targeted novelty audit.
- `audit/brf_exact_runtime_check.py` — exact-integer check for the small-`n` runtime values reported in the paper.
- `audit/runtime_check_output.txt` — recorded output of that check.
- `CITATION.cff` — citation metadata.
- `.zenodo.json` — source/software deposit metadata.
- `paper.publish.json` — paper-deposit metadata checklist.
- `LICENSE` — MIT license for source/package materials.
- `LICENSE_PAPER.txt` — CC BY 4.0 notice for the manuscript text/PDF.

## Reproduction

A standard LaTeX installation can compile the manuscript directly:

```bash
pdflatex paper.tex
pdflatex paper.tex
```

The runtime sanity check uses only the Python standard library:

```bash
python audit/brf_exact_runtime_check.py
```

## Current status

**PREPRINT v1.0.0 / NOT PEER REVIEWED.**

## Repository

GitHub: https://github.com/yonezaemon1-hub/randomization-collapses-idle-start-memory-barrier

## DOI

Paper DOI: **10.5281/zenodo.22643897**  
Software/source-package DOI: **10.5281/zenodo.22643729**
