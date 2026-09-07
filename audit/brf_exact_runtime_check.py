from math import comb

EXPECTED = {
    2: 10,
    3: 58,
    4: 602,
    5: 14106,
    6: 755610,
    7: 87665306,
    8: 21246839962,
}


def q_product(j: int) -> int:
    q = 1
    for r in range(1, j + 1):
        q *= (2**r - 1)
    return q


def delta(k: int) -> int:
    return sum(comb(k, j) * q_product(j) for j in range(k + 1))


def e1_exact(n: int) -> int:
    return 2**n + sum(
        delta(i) * (1 + sum(comb(n, x) for x in range(1, i + 1)))
        for i in range(1, n)
    )


def main() -> None:
    for n, expected in EXPECTED.items():
        got = e1_exact(n)
        assert got == expected, (n, got, expected)
        print(f"n={n}: E1={got} PASS")
    print("VERDICT=PASS_EXACT_INTEGER_RUNTIME_CHECK")


if __name__ == "__main__":
    main()
