"""Combinations."""


def combine(num_n: int, num_k: int) -> list[list[int]]:
    """Combine."""
    current = list(range(num_k))
    result = [current.copy()]
    start = num_k - 1
    while start >= 0:
        while num_n - current[start] - (num_k - start) <= 0:
            start -= 1
            if start == -1:
                break
        else:
            current[start] += 1
            for i in range(start + 1, num_k):
                current[i] = current[i - 1] + 1
            result.append(current.copy())
            start = num_k - 1
    return result


def main():
    """My function."""
    num_k, num_n = map(int, input().split())
    print(*(" ".join(map(str, c)) for c in combine(num_n, num_k)), sep="\n")


if __name__ == "__main__":
    main()
