# Proof Audit

Paper: **Randomization Collapses the Idle-Start Memory Barrier for Anonymous Dynamic Broadcast**

Status: preprint v1.0.0 candidate / not peer reviewed.

## Audited claims

### Active nodes remain informed

Only the broadcaster is initially active. A node can subsequently be active only by surviving from the previous active state or by receiving `INF` while idle. Thus every active node is informed.

### No false extinction

Let `S_t` be the active set at the start of round `t`. If `S_t` is a nonempty proper subset of `V`, connectivity of the current snapshot gives an edge crossing from an active node to an idle node. The active endpoint broadcasts before its private coin is used, so the idle endpoint receives `INF` and is active at `t+1`.

Therefore

```text
S_{t+1} = empty  =>  S_t = V.
```

Since every active node is informed, extinction can occur only after all nodes are already informed. The empty active set is absorbing, so the protocol is zero-error with respect to premature stabilization.

### Uniform finite-horizon success event

Fix `p in (0,1)`. From any nonterminal history, consider the event that every active node survives while the active set is proper, and once all `n` nodes are active, all `n` become idle simultaneously.

On the survival portion, connectivity ensures that at least one idle node is activated per round, so the active-set size strictly increases and reaches `n` within at most `n-1` rounds. The total number of required survival outcomes before full activation is at most

```text
1 + 2 + ... + (n-1) = n(n-1)/2.
```

Hence the event has probability at least

```text
q_n(p) = p^(n(n-1)/2) * (1-p)^n > 0
```

and completes within at most `n` rounds. Repeating this uniform conditional bound gives a geometric tail bound and therefore almost-sure stabilization with finite expectation.

### Memory statement

BRF has exactly two persistent protocol-control states, `ACTIVE` and `IDLE`, i.e. one persistent control bit. If an arbitrary `B`-bit application payload is modeled explicitly, informed nodes additionally retain those payload bits.

The paper therefore states the result as **one persistent control bit plus payload**. It does not claim that one bit is the randomized minimum.

### Adaptive worst-case runtime

For fair coins and the causal state-adaptive adversary of Section 6, if `K_t=k<n` and `b` idle nodes are exposed to the active set, then

```text
K_{t+1} = b + Bin(k, 1/2).
```

The one-frontier policy `b=1` is shown Bellman-optimal using the strict monotonicity of the one-frontier continuation values. With

```text
Q_j = product_{r=1}^j (2^r - 1)
Delta_k = sum_{j=0}^k C(k,j) Q_j,
```

the exact representation is

```text
E_1 = 2^n + sum_{i=1}^{n-1} Delta_i * (1 + sum_{x=1}^i C(n,x)).
```

The included exact-integer script reproduces the manuscript values

```text
n=2 -> 10
n=3 -> 58
n=4 -> 602
n=5 -> 14106
n=6 -> 755610
n=7 -> 87665306
n=8 -> 21246839962.
```

Using

```text
Q_k = 2^(k(k+1)/2) * product_{r=1}^k (1-2^(-r)),
```

the manuscript derives

```text
E[T] ~ c0 * 2^(n(n+1)/2),
c0 = product_{r>=1}(1-2^(-r)).
```

This tight asymptotic is claimed only for the stated causal state-adaptive adversary. The oblivious-schedule tight worst case remains open.

## Verdict

No internal contradiction was found in the theorem chain above. The small-`n` exact runtime values were independently reproduced by the included standard-library Python check. This audit is supplementary and is not peer review.
