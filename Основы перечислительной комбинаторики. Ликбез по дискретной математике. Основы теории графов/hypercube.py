"""Hypercube."""


def main():
    """My function."""
    str_a, str_b = input().split()
    k, ind, change = len(str_a), 0, {"1": "0", "0": "1"}
    cycle = [i for i in range(k) if str_a[i] != str_b[i]]
    lst = [[str_a] for _ in range(k)]
    for i, path in enumerate(lst):
        num, diff = path[-1], str_a[i] != str_b[i]
        path.append(num[:i] + change[num[i]] + num[i + 1:])
        ind += 1 - diff
        for j in cycle[i + diff - ind:] + cycle[:i - ind]:
            num = path[-1]
            path.append(num[:j] + change[num[j]] + num[j + 1:])
        if not diff:
            path.append(str_b)
    print(*(" ".join(p) for p in lst), sep="\n")


if __name__ == "__main__":
    main()
