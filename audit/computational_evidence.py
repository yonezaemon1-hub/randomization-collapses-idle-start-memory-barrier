#!/usr/bin/env python3
"""Exact finite-size runtime curve for fair-coin BRF.

This script reconstructs the integer Bellman representation from the paper.
It is computational evidence, not a substitute for the proof.
"""

import csv
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent
EXPECTED = {
    2: 10,
    3: 58,
    4: 602,
    5: 14106,
    6: 755610,
    7: 87665306,
    8: 21246839962,
}


def q(j: int) -> int:
    ans = 1
    for r in range(1, j + 1):
        ans *= (2 ** r - 1)
    return ans


def delta(k: int) -> int:
    return sum(math.comb(k, j) * q(j) for j in range(k + 1))


def exact_e1(n: int) -> int:
    total = 2 ** n
    for i in range(1, n):
        prefix = 1 + sum(math.comb(n, x) for x in range(1, i + 1))
        total += delta(i) * prefix
    return total


def main() -> None:
    rows = []
    for n in range(2, 13):
        e = exact_e1(n)
        if n in EXPECTED:
            assert e == EXPECTED[n], (n, e, EXPECTED[n])
        leading_exp = n * (n + 1) / 2
        log2_e = math.log2(e)
        ratio = e / (2.0 ** leading_exp)
        rows.append((n, e, log2_e, leading_exp, log2_e - leading_exp, ratio))

    path = OUT / "brf_runtime_curve.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "exact_E_T", "log2_E_T", "n_nplus1_over_2", "log2_residual", "normalized_ratio"])
        w.writerows(rows)

    print("PASS_BRF_RUNTIME_CURVE_AUDIT")
    print(path.name)
    for n, e, *_ in rows[:7]:
        print(f"n={n} E={e}")


if __name__ == "__main__":
    main()
