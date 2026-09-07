# Prior-Art and Claim-Boundary Audit

Paper: **Randomization Collapses the Idle-Start Memory Barrier for Anonymous Dynamic Broadcast**

Audit date: 2026-09-07.

## Closest direct literature

1. **Parzych and Daymude, DISC 2024 / Distributed Computing 2026** — deterministic anonymous dynamic broadcast. For idle-start stabilizing termination they prove a superconstant (`omega(1)`) local-memory lower bound and give the `O(log n)`-memory Countdown algorithm. Their lower bound is deterministic.

2. **Turau, SAND 2026** — randomized anonymous dynamic broadcast. The positive `O(log log n)`-memory result is non-idle-start and assumes knowledge of `n`. The termination-detection impossibility results concern the stronger task of detecting completion, not merely stabilizing termination.

3. **Austin, Gadouleau, Mertzios, and Trehan, DISC 2025** — Random Flooding on a static connected graph. It randomizes between Amnesiac Flooding and forwarding to all neighbors, broadcasts with certainty, and terminates almost surely. Its forwarding rule relies on fixed-graph per-neighbor/port structure unavailable in the port-indistinguishable adversarial dynamic model used here. This is the closest randomized low-state flooding result located in the targeted audit.

4. **Hussak and Trehan, Distributed Computing 2023** — Amnesiac Flooding on static graphs, again using per-neighbor information not present in the BRF model.

5. Other randomized low-memory dissemination results in phone-call, population, or PULL-type models use substantially different interaction primitives and do not directly instantiate anonymous adversarial 1-interval-connected local broadcast without ports.

## Narrow novelty claim

The manuscript does **not** claim novelty for randomized flooding, probabilistic forwarding, epidemic processes, infection-recovery dynamics, or random reactivation as generic mechanisms.

The model-specific claim is that, in anonymous, port-indistinguishable, synchronous, adversarially 1-interval-connected **idle-start** broadcast with unknown `n` and stabilizing termination, private Bernoulli reactivation yields a Las Vegas protocol with one persistent control bit plus payload. Combined with the known deterministic superconstant lower bound, this gives a qualitative deterministic-randomized control-memory separation.

The manuscript does not claim a randomized one-bit lower bound or exact randomized state complexity.

## Claims deliberately not made

The paper does **not** claim:

- that one control bit is necessary for randomized broadcast;
- termination detection;
- a polynomial-time randomized algorithm;
- the adaptive worst-case runtime theorem for oblivious topology schedules;
- novelty for Random Flooding or Amnesiac Flooding mechanisms;
- novelty for probabilistic epidemic/reactivation processes in general.

## Verdict

The novelty claim is intentionally model-specific and qualitative. A targeted literature audit through 2026-09-07 did not identify a prior one-control-bit private-coin Las Vegas idle-start stabilizing-broadcast upper bound in the same anonymous, port-indistinguishable, adversarially 1-interval-connected, unknown-`n` model. This is not a guarantee against undiscovered prior art and is not peer review.
